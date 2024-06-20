import sqlite3

def conectar_db():
    try:
        return sqlite3.connect('peliculas.db')
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tablas():
    conn = conectar_db()
    if conn:
        try:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS generos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL UNIQUE
                )
            ''')
            c.execute('''
                CREATE TABLE IF NOT EXISTS duraciones (
                    id INTEGER PRIMARY KEY,
                    duracion TEXT NOT NULL UNIQUE
                )
            ''')
            c.execute('''
                CREATE TABLE IF NOT EXISTS peliculas (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    genero_id INTEGER,
                    duracion_id INTEGER,
                    FOREIGN KEY (genero_id) REFERENCES generos (id),
                    FOREIGN KEY (duracion_id) REFERENCES duraciones (id)
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear tablas: {e}")
        finally:
            conn.close()
