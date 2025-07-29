## BACKEND – README.md

##  Versión en texto plano
Task Management API – FastAPI (Deployed on AWS App Runner)
Este es el backend para una aplicación de gestión de tareas construida con FastAPI, desplegada en AWS App Runner, conectada a una base de datos PostgreSQL (RDS) y expuesta mediante API Gateway.

## Endpoints públicos

- **App Runner (Swagger UI):**  
  https://ryjmczy9qy.us-east-1.awsapprunner.com/docs

- **API Gateway base URL:**  
  https://g6wpg9ox8i.execute-api.us-east-1.amazonaws.com/dev

## Funcionalidades
 - Registro e inicio de sesión
 - Crear, editar, eliminar y listar tareas
 - PostgreSQL en AWS RDS
 - Conexión segura usando Secrets Manager
 - Exposición pública con API Gateway
 - CORS habilitado para el frontend en S3

## Tecnologías
 - FastAPI
 - PostgreSQL (AWS RDS)
 - SQLAlchemy
 - psycopg2
 - AWS App Runner
 - AWS API Gateway
 - AWS Secrets Manager

## Cómo probar
Abre Swagger:
https://ryjmczy9qy.us-east-1.awsapprunner.com/docs

O consume directamente la API desde el API Gateway:
GET https://g6wpg9ox8i.execute-api.us-east-1.amazonaws.com/dev/tasks

## Estructura del proyecto
.
├── main.py
├── models/
├── schemas/
├── services/
├── database.py
└── requirements.txt
