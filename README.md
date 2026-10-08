# Práctica 01: Desarrollo de una API REST con FastAPI

## Objetivo

Crear una API REST utilizando FastAPI en Visual Studio Code, configurando un entorno virtual de Python, implementando endpoints básicos, ejecutando el servidor con Uvicorn y verificando la documentación automática generada por Swagger UI.

---

## Tecnologías utilizadas

- Python 3
- FastAPI
- Uvicorn
- Visual Studio Code
- Git

---

## 1. Creación del proyecto

Se creó una carpeta para el proyecto desde la terminal integrada de Visual Studio Code:

```powershell
mkdir taskflow-api
cd taskflow-api
```

---

## 2. Inicialización del repositorio Git

Se inicializó un repositorio Git para el control de versiones:

```powershell
git init
```

Verificación del repositorio:

```powershell
git status
```

---

## 3. Creación del entorno virtual

Se creó un entorno virtual para aislar las dependencias del proyecto:

```powershell
python -m venv .venv
```

Activación del entorno virtual:

```powershell
.venv\Scripts\Activate.ps1
```

Al activarse correctamente, la terminal muestra el prefijo:

```text
(.venv)
```

---

## 4. Instalación de dependencias

Instalación de FastAPI y Uvicorn:

```powershell
pip install fastapi uvicorn
```

Generación del archivo de dependencias:

```powershell
pip freeze > requirements.txt
```

---

## 5. Creación de la estructura del proyecto

Estructura generada:

```text
taskflow-api/
```

<!-- Completa aquí el resto de la estructura de carpetas -->

---

## 6. Implementación de los endpoints

Se implementaron tres endpoints básicos de tipo `GET`: `/health`, `/version` y `/ping`.

![Código de los endpoints /health, /version y /ping](images/01-endpoints.png)

---

## 7. Ejecución del servidor

El servidor se ejecutó con Uvicorn en modo recarga automática:

```powershell
uvicorn app.main:app --reload
```

![Servidor Uvicorn en ejecución en http://127.0.0.1:8000](images/02-uvicorn.png)

---

## 8. Documentación automática (Swagger UI)

FastAPI genera la documentación de forma automática. Se accede desde `http://127.0.0.1:8000/docs`, donde se listan los tres endpoints creados.

![Swagger UI de TaskFlow API con los endpoints /health, /version y /ping](images/03-swagger.png)
