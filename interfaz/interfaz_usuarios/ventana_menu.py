# Importaciones:
from tkinter import Frame
from tkinter import Button
from tkinter import Label

def ventana_menu(parent):
    """ Configuración de la ventana principal del menú """

    # Importaciones perezosas:
    from interfaz.interfaz_usuarios.ventana_lista_usuarios import ventana_lista_usuarios
    from interfaz.interfaz_productos.ventana_lista_productos import ventana_lista_productos

    # Configuración de la ventana
    parent.frame_left = Frame(master = parent, width = 200)
    parent.frame_left.grid(row = 0, column = 0, sticky = "NSEW")
    parent.frame_center = Frame(master = parent)
    parent.frame_center.grid(row = 0, column = 1, sticky = "NSEW")

    lbl_prueba = Label(master = parent.frame_center, text = "Este es el frame central")
    lbl_prueba.grid(row = 0, column = 0, pady = 10, padx = 10)

    # Configuración de los botones del menú
    # Boton usuarios
    btn_usuarios = Button(master = parent.frame_left, text = "Usuarios", width = 15, height = 2,
                          # Se pasan los argumentos a la función ventana_lista_usuarios
                          command = lambda: ventana_lista_usuarios(parent))
    btn_usuarios.grid(row = 0, column = 0, pady = 10, padx = 10)

    # Boton productos
    btn_productos = Button(master = parent.frame_left, text = "Productos", width = 15, height = 2,
                          # Se pasan los argumentos a la función ventana_lista_usuarios
                          command = lambda: ventana_lista_productos(parent))
    btn_productos.grid(row = 1, column = 0, pady = 10, padx = 10)

    

