from tkinter import *
from tkinter import ttk

class mainApp(Tk):  # heredamos la clase Tk (es la ventana principal de Tkinter)
    size = "1024x768"
    
    def __init__(self):
        Tk.__init__(self)  # al heredar hay que ponerlo así (ver ejercicio perro por ejemplo)
        
        self.geometry(self.size)  # pilla el atributo definido antes ("1024x768"). Estamos definiendo la geometría de la ventana mediante una cadena, se hace así en Tkinter
        self.title("Mi ventana")  # título de la ventana
        self.configure(bg = "blue")  # definimos el color del fondo de la ventana
        
    def start(self):
        self.mainloop()  # ciclo principal de Tkinter esperando eventos, tipo PyGame
        
        
if __name__ == '__main__':
    app = mainApp()
    app.start()
    

        
        
    
    



