backend/README.md

# Backend - FastAPI

Este es el backend de la aplicación de gestión de tareas, construido con **FastAPI**, **SQLAlchemy** y **PostgreSQL**.

---

## Requisitos

- Python 3.9+
- PostgreSQL
- pipenv o virtualenv (opcional pero recomendado)

---

## Configuración

1. Clona el repositorio y accede al directorio del backend:

```bash
git clone https://github.com/tuusuario/task-app.git
cd task-app/backend
```

2. Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```
---
# requirements.txt para el backend (FastAPI + PostgreSQL + SQLAlchemy)

fastapi==0.110.0
uvicorn[standard]==0.29.0
sqlalchemy==2.0.30
psycopg2-binary==2.9.9
python-dotenv==1.0.1
boto3==1.34.103
---

4. Asegúrate de que la configuración de conexión a la base de datos esté correcta en `database.py`. Puedes usar valores hardcodeados o cargar desde Secrets Manager o variables de entorno.

5. Ejecuta la aplicación:

```bash
uvicorn main:app --reload
```

- API disponible en: http://localhost:8000  
- Documentación Swagger: http://localhost:8000/docs

---

## Estructura

```
backend/
│
├── main.py              # Punto de entrada
├── database.py          # Conexión a PostgreSQL
├── models/              # Definiciones ORM
├── schemas/             # Esquemas Pydantic
├── crud/                # Operaciones con base de datos
├── secrets.py           # (opcional) Manejo de secretos
└── requirements.txt     # Dependencias
```

---

## Tecnologías

- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn

---

