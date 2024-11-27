from tkinter.ttk import *
from tkinter import *
from ultralytics import YOLO
import cv2
from almacen import almacen
import serial,time

Inventario=almacen.inicioInventario()

def camara():
    # start webcam
    cap = cv2.VideoCapture(1)
    cap.set(3, 640)
    cap.set(4, 480)

    # model
    model = YOLO("yolo-Weights/best.pt")

    # object classes
    classNames = ["Bisagra","Llanta","Motor","Rin","Tornillo","Tuerca"]

    # discard 50 first frames to intialize de cam  
    for _ in range(50):  
        result, image = cap.read()

    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes

        for box in boxes:
        
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)   # objects detected write in a string
        
            cls = int(box.cls[0])
        
            if(y1<200):
                if(x1<213):
                    almacen.agregar(Inventario,2,classNames[cls])
                elif(x1>426):
                    almacen.agregar(Inventario,6,classNames[cls])
                else:
                    almacen.agregar(Inventario,4,classNames[cls])
            else:
                if(x1<213):
                    almacen.agregar(Inventario,1,classNames[cls])
                elif(x1>426):
                    almacen.agregar(Inventario,5,classNames[cls])
                else:
                    almacen.agregar(Inventario,3,classNames[cls])

def Mover(Accion,Posicion1,Posicion2):
    arduino = serial.Serial("COM4", 9600)
    time.sleep(2)
    arduino.write(Accion.decode())
    time.sleep(2)
    arduino.write(Posicion1.decode())
    time.sleep(2)
    arduino.write(Posicion2.decode())
    arduino.close()

def Extraer():
    camara()
    Objeto=VentanaPregunta1()
    Posicion=almacen.buscar(Inventario,Objeto)
    Mover(1,Posicion,0)

def Pintar():
    camara()
    Objeto=VentanaPregunta1()
    Posicion=almacen.buscar(Inventario,Objeto)
    Mover(2,Posicion,0)
        

def Ensamblar():
    camara()
    Objeto1=VentanaPregunta1()
    Objeto2=VentanaPregunta2()
    Posicion1=almacen.buscar(Inventario,Objeto1)
    Posicion2=almacen.buscar(Inventario,Objeto2)
    Mover(3,Posicion1,Posicion2)

def VentanaPregunta1():
    Pregunta=Toplevel()

    def getTxt():
        Objeto.set(txtObjeto.get())
        Pregunta.destroy()

    txtAnuncio=Label(Pregunta,text="Objetos encontrados en almacen:")
    txtAnuncio.pack()

    txtLista=Label(Pregunta,text=almacen.listar(Inventario))
    txtLista.pack()

    txtPregunta=Label(Pregunta,text="Con qué objeto desea interactuar?")
    txtPregunta.pack()
        
    miFrame=Frame(Pregunta)
    miFrame.pack()
        
    Objeto=StringVar()
    txtObjeto=Entry(miFrame,textvariable=Objeto)
    txtObjeto.pack()

    btnAceptar=Button(miFrame,text="Aceptar",command=lambda:getTxt())
    btnAceptar.pack()

    Pregunta.wait_window()
    return Objeto.get()
    
def VentanaPregunta2():
    Pregunta=Toplevel()

    def getTxt():
        Objeto.set(txtObjeto.get())
        Pregunta.destroy()
        
    txtLista=Label(Pregunta,text=almacen.listar(Inventario))
    txtLista.pack()

    txtPregunta=Label(Pregunta,text="Qué objeto deseas ensamblar?")
    txtPregunta.pack()
        
    miFrame=Frame(Pregunta)
    miFrame.pack()
        
    Objeto=StringVar()
    txtObjeto=Entry(miFrame,textvariable=Objeto)
    txtObjeto.pack()

    btnAceptar=Button(miFrame,text="Aceptar",command=lambda:getTxt())
    btnAceptar.pack()

    Pregunta.wait_window()

    return Objeto.get()

ventana = Tk()
ventana.geometry("150x100")
ventana.title("Rodolfito")

txtTitulo=Label(ventana,text='Panel de control')
txtTitulo.pack()

btnExtraer=Button(ventana,text="Extraer",command=Extraer)
btnExtraer.pack()

btnPintar=Button(ventana,text="Pintar",command=Pintar)
btnPintar.pack()

btnEnsamblar=Button(ventana,text="Ensamblar",command=Ensamblar)
btnEnsamblar.pack()

ventana.mainloop()