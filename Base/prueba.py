# prueba.py

import sqlite3

conn = sqlite3.connect("plantas.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    p.nombre_comun,
    p.nombre_cientifico,
    u.nombre
FROM plantas p
JOIN ubicaciones u
ON p.ubicacion_id = u.id
LIMIT 50
""")

for fila in cursor.fetchall():
    print(fila)

conn.close()