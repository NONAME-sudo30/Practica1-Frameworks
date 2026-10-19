from datetime import datetime

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas import TaskCreate, TaskRead

app = FastAPI(title="TaskFlow", version="0.1.0")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores = [
        {
            "campo": ".".join(str(p) for p in e["loc"] if p != "body"),
            "mensaje": e["msg"],
            "tipo": e["type"],
        }
        for e in exc.errors()
    ]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Error de validación en los datos enviados", "errores": errores},
    )


@app.post(
    "/tasks",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear tarea (temporal)",
)
def create_task(task: TaskCreate) -> TaskRead:
    return TaskRead(
        id=1,
        completed=False,
        created_at=datetime.now(),
        **task.model_dump(),
    
