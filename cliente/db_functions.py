import sqlite3
from .conneciondb import ConeccionDB

def agregar_pelicula(nombre, genero_id, duracion_id):
    try:
        with ConeccionDB() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO peliculas (nombre, genero_id, duracion_id) VALUES (?, ?, ?)", (nombre, genero_id, duracion_id))
            conn.commit()
            print("Película agregada correctamente")
    except sqlite3.Error as e:
        print(f"Error al agregar película: {e}")

def actualizar_pelicula(pelicula_id, nombre, genero_id, duracion_id):
    try:
        with ConeccionDB() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE peliculas SET nombre = ?, genero_id = ?, duracion_id = ? WHERE id = ?", (nombre, genero_id, duracion_id, pelicula_id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al actualizar película: {e}")

def eliminar_pelicula(pelicula_id):
    try:
        with ConeccionDB() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM peliculas WHERE id = ?", (pelicula_id,))
            conn.commit()
            print(f"Se borró la película con ID {pelicula_id}")
    except sqlite3.Error as e:
        print(f"Error al eliminar película: {e}")

def obtener_peliculas():
  try:
    with ConeccionDB() as conn:
      cursor = conn.cursor()
      cursor.execute('''
          SELECT peliculas.id, peliculas.nombre, 
          generos.nombre AS genero, duraciones.duracion AS duracion
          FROM peliculas 
          JOIN generos ON peliculas.genero_id = generos.id 
          JOIN duraciones ON peliculas.duracion_id = duraciones.id
      ''')
      return cursor.fetchall()
  except sqlite3.Error as e:
    print(f"Error al obtener películas: {e}")
    return []


def obtener_generos():
    try:
        with ConeccionDB() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM generos")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener géneros: {e}")
        return []

def obtener_duraciones():
    try:
        with ConeccionDB() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM duraciones")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener duraciones: {e}")
        return []

def agregar_genero(nombre):
    try:
        with ConeccionDB() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO generos (nombre) VALUES (?)", (nombre,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al agregar género: {e}")

def agregar_duracion(duracion):
    try:
        with ConeccionDB() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO duraciones (duracion) VALUES (?)", (duracion,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al agregar duración: {e}")
