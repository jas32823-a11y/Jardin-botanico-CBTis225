import pandas as pd
import sqlite3

# Leer Excel
df = pd.read_excel("plantas.xlsx")

df.columns = df.columns.str.strip()

for columna in df.columns:
    if df[columna].dtype == "object":
        df[columna] = df[columna].astype(str).str.strip()

# Limpiar nombres de columnas
df.columns = df.columns.str.strip().str.lower()

# Conectar a SQLite
conn = sqlite3.connect("plantas.db")
cursor = conn.cursor()

# Borrar tablas anteriores
cursor.execute("DROP TABLE IF EXISTS plantas")
cursor.execute("DROP TABLE IF EXISTS ubicaciones")

# Crear tabla ubicaciones
cursor.execute("""
CREATE TABLE ubicaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL
)
""")

# Crear tabla plantas
cursor.execute("""
CREATE TABLE plantas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_cientifico TEXT NOT NULL,
    nombre_comun TEXT,
    usos TEXT,
    origen TEXT,
    foto IMAGE,
    ubicacion_id INTEGER,

    FOREIGN KEY (ubicacion_id)
    REFERENCES ubicaciones(id)
)
""")

# Insertar ubicaciones únicas
for ubicacion in df["ubicacion"].dropna().unique():

    cursor.execute("""
        INSERT INTO ubicaciones(nombre)
        VALUES(?)
    """, (ubicacion,))

# Insertar plantas
for _, fila in df.iterrows():

    cursor.execute("""
        SELECT id
        FROM ubicaciones
        WHERE nombre = ?
    """, (fila["ubicacion"],))

    ubicacion_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT INTO plantas (
            nombre_cientifico,
            nombre_comun,
            usos,
            origen,
            foto,
            ubicacion_id
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        str(fila["nombre_cientifico"]),
        str(fila["nombre_comun"]),
        str(fila["usos"]),
        str(fila["origen"]),
        str(fila["foto"]) if "foto" in df.columns else None,
        ubicacion_id
    ))

conn.commit()
conn.close()

print("Base de datos creada correctamente.")