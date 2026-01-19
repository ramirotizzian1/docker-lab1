from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("POSTGRES_DB", "postgres")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")

@app.get("/")
def read_root():
    return {"message": "Lab Docker funcionando 🚀"}

@app.get("/db")
def test_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return {"status": "Conectado a PostgreSQL correctamente"}
    except Exception as e:
        return {"error": str(e)}
