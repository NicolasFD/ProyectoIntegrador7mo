class almacen:
    def __init__(self, posicion, objeto, ocupado):
        self.posicion=posicion
        self.objeto=objeto
        self.ocupado=ocupado
        self.numero=6
    
    def inicioInventario():
        Inventario=[]
        for i in range(6):
            Inventario.append(almacen(i+1,"N/O",False))
        return Inventario
    
    def agregar(Inventario, posicion, objeto):
        Inventario[posicion-1]=almacen(posicion,objeto,True)
    
    def eliminar(Inventario, posicion):
        Inventario[posicion-1]=almacen(posicion,"N/O",False)
    
    def listar(Inventario):
        List=""
        for obj in Inventario:
            List+=str(obj.posicion)+" "+obj.objeto+"\n"
        return List

    def buscar(Inventario, objeto):
        for obj in Inventario:
            if objeto==obj.objeto:              
                return obj.posicion