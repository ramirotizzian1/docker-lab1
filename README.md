# 🐳 Docker Lab 1 – FastAPI + PostgreSQL con Docker Compose

Laboratorio práctico para aprender Docker desde cero con un stack realista:  
API en Python (FastAPI) + Base de datos PostgreSQL, orquestados con Docker Compose.

Proyecto orientado a práctica profesional en backend, DevOps y bases para Kubernetes.

---

## 📦 Stack tecnológico

- Python 3.11  
- FastAPI  
- PostgreSQL 15  
- Docker  
- Docker Compose  

---

## 🧱 Arquitectura


- La API se comunica con la base usando red interna de Docker  
- La base de datos persiste datos usando volúmenes  
- Todo el entorno se levanta con un solo comando

---

## 🚀 Cómo ejecutar el proyecto

### Requisitos
- Docker Engine  
- Docker Compose v2  

Verificar instalación:
```bash
docker --version
docker compose version
