import sqlite3

class ConeccionDB():
    def __init__(self):
        self.base_datos = 'peliculas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    
    def cerrar_con(self):
        self.conexion.commit()
        self.conexion.close()

    def __enter__(self):
        return self.conexion

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar_con()
