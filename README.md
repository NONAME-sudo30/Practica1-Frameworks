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

<img width="277" height="235" alt="Captura de pantalla 2026-10-08 130507" src="https://github.com/user-attachments/assets/24c18768-de93-4d99-a71b-1e78b49ef17a" />


---

## 7. Ejecución del servidor

El servidor se ejecutó con Uvicorn en modo recarga automática:

```powershell
uvicorn app.main:app --reload
```



---

## 8. Documentación automática (Swagger UI)

FastAPI genera la documentación de forma automática. Se accede desde `http://127.0.0.1:8000/docs`, donde se listan los tres endpoints creados.

<img width="1472" height="472" alt="Captura de pantalla 2026-10-08 130652" src="https://github.com/user-attachments/assets/ec844a5b-8d96-4455-b17a-3ac136470445" />


