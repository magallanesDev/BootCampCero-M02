from tkinter import *
from tkinter import ttk

class mainApp(Tk):  # heredamos la clase Tk (es la ventana principal de Tkinter)
    entrada = None
    tipoUnidad = None
    __temperaturaAnt = ""
    
    def __init__(self):
        Tk.__init__(self)  # al heredar hay que ponerlo así (ver ejercicio perro por ejemplo)
        
        self.geometry("210x150")  # estamos definiendo la geometría de la ventana mediante una cadena, se hace así en Tkinter
        self.title("Termómetro")  # título de la ventana
        self.configure(bg = "#ECECEC")  # definimos el color del fondo de la ventana
        self.resizable(0,0)  # esto es para que no se pueda modificar el tamaño de la ventana
        
        self.temperatura = StringVar(value = "")  # StringVar es lo que se llama variable de control en Tkinter
        self.temperatura.trace("w", self.validateTemperature)  # método trace de Tkinter, write (w) / read (r) / unset (u), invocando la función validateTemperature
        self.tipoUnidad = StringVar(value = "C")
        
        self.createLayout()  # invocamos este método que definimos más adelante, ya sabemos que Python lee todos los métodos a la vez
        
    
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable = self.temperatura).place(x=10, y=10)  # widget tipo Entry de Tkinter
        self.lblUnidad = ttk.Label(self, text="Grados:").place(x=10, y=45)  # widget tipo Label
        self.rb1 = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F", command=self.selected).place(x=20, y=70)  # widget tipo Radio Button
        self.rb2 = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C", command=self.selected).place(x=20, y=95)
        
    def start(self):
        self.mainloop()  # ciclo principal de Tkinter esperando eventos, tipo PyGame
        
    def validateTemperature(self, *args):  # la función de nivel superior trace exige unos parámetros (argumentos) por eso ponemos *args (sería una lista vacía)
        nuevoValor = self.temperatura.get()
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
        except:
            self.temperatura.set(self.__temperaturaAnt)
     
    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()  # con el get extraemos el valor de la variable de control self.tipoUnidad
        grados = float(self.temperatura.get())  # idem con self.temperatura
         
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        self.temperatura.set(resultado)  # con el set asignamos el resultado a la variable de control self.temperatura
        
        
if __name__ == '__main__':
    app = mainApp()
    app.start()
    