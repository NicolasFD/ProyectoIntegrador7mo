from tkinter import Tk,Label,messagebox,Button
from Almacen import almacen

class Aplicacion:
    def Extraer(Inventario):
        Objeto=messagebox.askquestion(message=almacen.listar(Inventario))
        if almacen.buscar(Inventario,Objeto):
            pass
        else:
            messagebox.showinfo(message="Objeto no encontrado")

    def Pintar():
        pass

    def Ensamblar():
        pass