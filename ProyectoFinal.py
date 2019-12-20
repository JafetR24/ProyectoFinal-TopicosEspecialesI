from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#Creación de pantalla
windows = Tk()
windows.geometry = "500x400"
#Creación de panel contenedor de pagina principal (presentación)
ventana = PanedWindow(bg="#F47D64",height=500,width=900)
ventana.pack(padx=10,pady=10)
#Inserción de imagen de presentación
img = ImageTk.PhotoImage(Image.open("pf.jpg"))
panel = Label(ventana, image = img).place(x=0,y=0)
     
def lv():
    ventana.destroy()
    #creación de panel del programa
    venta = PanedWindow(bg="#F47D64",height=500,width=900)
    venta.pack(padx=10,pady=10)
    #Declaración de variables para la captación de datos
    ast = StringVar()
    bst = StringVar()
    k1st = StringVar()
    k2st = StringVar()
    e1st = StringVar()
    e2st = StringVar()
    mst = StringVar()
    nst = StringVar()
    #Captación de datos mediante Entry o cajas de textos
    a = Entry(venta,textvariable=ast).place(x=370,y=5)
    aL = Label(venta,text="Tasa de crecimiento de especia 1",font=("Verdana",15)).place(x=20,y=0)
    b = Entry(venta,textvariable=bst).place(x=370,y=55)
    bL = Label(venta,text="Tasa de crecimiento de especia 2",font=("Verdana",15)).place(x=20,y=50)  
    K1 = Entry(venta,textvariable=k1st).place(x=500,y=105)
    K1L = Label(venta,text="Tamaño de poblacion sostenible de especie 1",font=("Verdana",15)).place(x=20,y=100)  
    K2 = Entry(venta,textvariable=k2st).place(x=500,y=155)
    K2L = Label(venta,text="Tamaño de poblacion sostenible de especie 2",font=("Verdana",15)).place(x=20,y=150)
    E12 = Entry(venta,textvariable=e1st).place(x=725,y=205)
    E12L = Label(venta,text="Impacto competitivo por individuo que ejerce la especie 2 sobre la 1",font=("Verdana",15)).place(x=20,y=200)  
    E21 = Entry(venta,textvariable=e2st).place(x=725,y=255)
    E21L = Label(venta,text="Impacto competitivo por individuo que ejerce la especie 1 sobre la 2",font=("Verdana",15)).place(x=20,y=250)
    m = Entry(venta,textvariable=mst).place(x=340,y=305)
    mL = Label(venta,text="Valores poblacionales iniciales",font=("Verdana",15)).place(x=20,y=300) 
    n = Entry(venta,textvariable=nst).place(x=340,y=355)
    nL = Label(venta,text="Valores poblacionales iniciales",font=("Verdana",15)).place(x=20,y=350)
    def fin():
        #Recepción de datos en nuevas variables
        a2=ast.get()
        b2=bst.get()
        K12=k1st.get()
        K22=k2st.get()
        E122=e1st.get()
        E212=e2st.get()
        m2=mst.get()
        n2=nst.get()
        #**************
        plt.close('all')
        #Ecuaciones Simultaneas
        def dP_dt(P, t):
            return [float(a2)*P[0]*((float(K12)-P[0]-float(E122)*P[1])/float(K12)), float(b2)*P[1]*((float(K22)-P[1]-float(E212)*P[0])/float(K22))]

        #Definicion de Tiempo (pasos de solucion de la ecuacion)
        ts = np.linspace(0, 24, 100)

        #Valores poblacionales iniciales (especie 1 y especie2)*
        P0 = [m2, n2]

        #Resulucion matematica del modelo
        Ps = odeint(dP_dt, P0, ts)

        #Valores calculados de cada ecuacion
        esp1 = Ps[:,0]
        esp2 = Ps[:,1]

        #Grafica de las poblaciones de las especies 1 y 2
        plt.figure(1)
        plt.plot(ts, esp1, "r-", label="Especie 1")
        plt.plot(ts, esp2, "b-", label="Especie 2")
        plt.xlabel("Tiempo (meses)")
        plt.ylabel("Poblacion")
        plt.title("Sistema Competitivo de 2 Especies");
        plt.legend();

        #Grafica de poblaciones finales despues de cada paso de tiempo de la simulacion
        plt.figure(2)
        plt.plot(esp1, esp2, "b.")
        plt.xlabel("Especie 1")
        plt.ylabel("Especie 2")
        plt.title("Diagrama de Espacio de Fase");
        plt.show()
        #**************
    valores = Button(command=fin,activebackground="#F94D29",foreground="#F47D64",bg="#B3FE80",text="Captar valores",font=("Verdana",15)).place(x=240,y=460)
    
def sali():
    windows.destroy()

if __name__ == "__main__":
    programa = Button(command=lv,activebackground="#F94D29",foreground="#F47D64",bg="#B3FE80",text="Lotka-Volterra",font=("Verdana",15)).place(x=740,y=460)
    
