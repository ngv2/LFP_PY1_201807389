import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from lectura import lectura


class interfaz:
    def __init__(self, ventana):
        self.lexico = lectura()
        self.ventana = ventana
        self.ventana.geometry (str(720) + 'x' + str(720) + '+' + str(self.ventana.winfo_screenwidth() // 2 - 720 // 2) + '+' + str(self.ventana.winfo_screenheight() // 2 - 720 // 2))
        self.ventana.resizable (0, 0)
        self.textobox = scrolledtext.ScrolledText(self.ventana, width = 85, height = 38)
        self.textobox.place(x = 5, y = 90)
        self.boton = Button (self.ventana, text='Cargar Archivo', command=self.abrirarchivo)
        self.boton.place(x = 15, y = 25)
        self.boton2 = Button (self.ventana, text='Analizar', command=self.anarchivo)
        self.boton2.place(x = 110, y = 25)
        n = tkinter.StringVar()
        self.combox = ttk.Combobox(self.ventana, state= 'readonly', textvariable=n)
        lista = ['Reporte de tokens', 'Reporte de errores', 'Manual de usuario', 'Manual técnico']
        self.combox ['values'] = lista
        self.combox.set('Reportes')
        self.combox.bind('<<ComboboxSelected>>', self.seleccionescombo)
        self.combox.place(x= 200, y = 25)
        self.ventana.mainloop ()

    def abrirarchivo(self):
        try:
            self.archivo = askopenfilename(filetypes= [('Archivos Forms', '*.form')])
            seleccion = open(self.archivo, encoding= 'utf-8')
            contentfile = seleccion.read()
            seleccion.close()
            self.textobox.delete('1.0', END)
            self.textobox.insert(tkinter.INSERT, contentfile)
        except IOError:
            messagebox.showwarning('Proyecto 1', 'Error al cargar el archivo')


    def anarchivo(self):
        contenido = self.textobox.get('1.0', END)
        if len(contenido) -1>0:
            self.lexico.obtenerlink(self.archivo)
            self.lexico.leyendo(contenido)

        else:
            messagebox.showwarning('Proyecto 1', 'Error: No hay contenido en el archivo')

    def seleccionescombo(self, eventObject):
        if self.combox.get() == 'Reporte de tokens':
            if self.lexico.listatoken:
                self.lexico.generarhtml()
            else:
                messagebox.showwarning('Proyecto 1', 'Error: No hay contenido en la lista')
        elif self.combox.get() == 'Reporte de errores':
            self.lexico.generarhtmlE()
        elif self.combox.get() == 'Manual de usuario':
            #os.system('Manual de usuario.pdf')
            print('tres')
        elif self.combox.get() == 'Manual técnico':
            #os.system('[LFP]HT1_201807389.pdf')
            print('cuatro')
     


if __name__ == '__main__':
    envio = Tk()
    interfaz(envio)