import tkinter as tk
from cliente.vista import Frame
from cliente.tablas import crear_tablas

def main():
    crear_tablas()  

    ventana = tk.Tk()
    ventana.title('Listado Peliculas')
    ventana.iconbitmap('img/videocamara.ico')
    ventana.resizable(0, 0)


    app = Frame(root=ventana)

    ventana.mainloop()

if __name__ == '__main__':
    main()
