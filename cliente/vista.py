import tkinter as tk
from tkinter import ttk, messagebox
from cliente.db_functions import  obtener_peliculas, agregar_pelicula, actualizar_pelicula, eliminar_pelicula, obtener_generos, obtener_duraciones, agregar_genero, agregar_duracion

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pelicula_id = None
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.create_table()
        self.create_input_form()
        self.create_buttons()
        self.create_exit_button()

    def create_table(self):
        self.tree = ttk.Treeview(self, columns=('ID', 'Nombre', 'Genero', 'Duración'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Genero', text='Genero')
        self.tree.heading('Duración', text='Duración')
        self.tree.grid(row=0, column=0, columnspan=5)
        self.load_data()
        self.tree.bind('<ButtonRelease-1>', self.on_tree_select)

    def create_input_form(self):
        self.label_nombre = tk.Label(self, text="Nombre: ", font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text="Género: ", font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text="Duración: ", font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=3, column=0, padx=10, pady=10)

        self.entry_nombre = tk.Entry(self, width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        generos = obtener_generos()
        self.entry_genero = ttk.Combobox(self, values=[g[1] for g in generos], state="readonly", font=('Arial', 12), width=25)
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        duraciones = obtener_duraciones()
        self.entry_duracion = ttk.Combobox(self, values=[d[1] for d in duraciones], state="readonly", font=('Arial', 12), width=25)
        self.entry_duracion.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

    def create_buttons(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=4, column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_datos, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000', state='disabled')
        self.btn_modi.grid(row=4, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000', state='disabled')
        self.btn_cance.grid(row=4, column=2, padx=10, pady=10)

        self.btn_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_pelicula, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_eliminar.grid(row=4, column=3, padx=10, pady=10)

    def create_exit_button(self):
        self.btn_exit = tk.Button(self, text='Salir', command=self.exit_application, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#000000', cursor='hand2', activebackground='#555555', activeforeground='#FFFFFF')
        self.btn_exit.grid(row=5, column=0, columnspan=4, pady=10)

    def load_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        peliculas = obtener_peliculas()
        for pelicula in peliculas:
            self.tree.insert('', 'end', values=pelicula)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_genero.config(state='readonly')
        self.entry_duracion.config(state='readonly')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')
        self.pelicula_id = None

    def bloquear_campos(self):
        self.entry_nombre.delete(0, 'end')
        self.entry_genero.set('')
        self.entry_duracion.set('')
        self.entry_nombre.config(state='disabled')
        self.entry_genero.config(state='readonly')
        self.entry_duracion.config(state='readonly')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')

    def guardar_datos(self):

        
        nombre = self.entry_nombre.get()
        genero = self.entry_genero.get()
        duracion = self.entry_duracion.get()

        if not nombre or not genero or not duracion:
            print("Todos los campos son requeridos.")
            return

        genero_id = next((g[0] for g in obtener_generos() if g[1] == genero), None)
        duracion_id = next((d[0] for d in obtener_duraciones() if d[1] == duracion), None)

        if genero_id is None:
            agregar_genero(genero)
            genero_id = next((g[0] for g in obtener_generos() if g[1] == genero), None)

        if duracion_id is None:
            agregar_duracion(duracion)
            duracion_id = next((d[0] for d in obtener_duraciones() if d[1] == duracion), None)

        if self.pelicula_id is None:
            agregar_pelicula(nombre, genero_id, duracion_id)
        else:
            actualizar_pelicula(self.pelicula_id, nombre, genero_id, duracion_id)

        self.load_data()
        self.bloquear_campos()

    def eliminar_pelicula(self):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        pelicula_id = values[0]
        eliminar_pelicula(pelicula_id)
        self.load_data()

    def on_tree_select(self, event):
        selection = self.tree.selection()
        if not selection:
            print("No hay elemento seleccionado.")
            return

        selected_item = selection[0]
        values = self.tree.item(selected_item, 'values')
        # Update to use retrieved text for genre and duration
        self.pelicula_id = values[0]
        self.entry_nombre.delete(0, 'end')
        self.entry_nombre.insert(0, values[1])
        self.entry_genero.set(values[2])  # Use values[2] for genre text
        self.entry_duracion.set(values[3])  # Use values[3] for duration text
        self.habilitar_campos()

    def exit_application(self):
        if messagebox.askokcancel("Salir", "¿Desea salir? Se guardarán los cambios."):
            self.root.destroy()
