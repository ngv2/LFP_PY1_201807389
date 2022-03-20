from token import token
from typing import TextIO


class lectura:
    def leyendo(self, contenido):
        contenido = contenido.lower()
        estado = 0
        subestado = 0
        concatenar = ""
        fila = 1
        columna = 1
        texto = False
        self.listatoken = []
        aux = ""

        for l in contenido:
            if l == "\n":
                fila += 1 
                columna = 1
            elif l == " ":
                if estado == 3 and texto == True:
                    concatenar += l
                columna += 1
            elif l == "\t":
                columna += 8
            elif l == "    ":
                columna +=4
            elif self.comprobarletras(l):
                if estado == 0:
                    if ord(l) == 97 and (subestado ==0 or subestado == 1):
                        concatenar += l
                        if concatenar == "entrada":
                            self.listatoken.append (token('Palabra reservada', concatenar, fila, columna + 1 - len(concatenar)))
                            concatenar = ""
                            subestado = 1
                            estado = 1
                    elif ord(l) == 100 and subestado == 1:
                        concatenar += l
                    elif ord(l) == 101 and subestado == 1:
                        concatenar += l
                    elif ord(l) == 102 and (subestado ==0 or subestado == 1) :
                        concatenar += l
                    elif ord(l) == 105 and (subestado ==0 or subestado == 1):
                        concatenar += l
                    elif ord(l) == 108 and (subestado ==0 or subestado == 1):
                        concatenar += l
                    elif ord(l) == 109 and subestado ==0:
                        concatenar += l
                    elif ord(l) == 110 and subestado == 1:
                        concatenar += l
                    elif ord(l) == 111 and (subestado ==0 or subestado == 1):
                        concatenar += l
                        if concatenar == "formulario":
                            self.listatoken.append (token('Palabra reservada', concatenar, fila, columna + 1 - len(concatenar)))
                            concatenar = ""
                            estado = 1
                        elif concatenar == "tipo":
                            self.listatoken.append (token('Palabra reservada', concatenar, fila, columna + 1 - len(concatenar)))
                            concatenar = ""
                            estado = 1
                        elif concatenar == "fondo":
                            self.listatoken.append (token('Palabra reservada', concatenar, fila, columna + 1 - len(concatenar)))
                            concatenar = ""
                            estado = 1
                        elif concatenar == "evento":
                            self.listatoken.append (token('Palabra reservada', concatenar, fila, columna + 1 - len(concatenar)))
                            concatenar = ""
                            estado = 1
                            subestado = 2
                        elif concatenar == "info":
                            self.listatoken.append (token('Palabra reservada', concatenar, fila, columna + 1 - len(concatenar)))
                            concatenar = ""
                            subestado = 1
                            estado = 1
                    elif ord(l) == 112 and subestado == 1:
                        concatenar += l
                    elif ord(l) == 114 and (subestado ==0 or subestado == 1):
                        concatenar += l
                        if concatenar == "valor":
                            self.listatoken.append (token('Palabra reservada', concatenar, fila, columna + 1 - len(concatenar)))
                            aux = concatenar
                            concatenar = ""
                            estado = 1
                    elif ord(l) == 115 and subestado == 1:
                        concatenar += l
                        if concatenar == "valores":
                            self.listatoken [len(self.listatoken) - 1].valor = concatenar
                            concatenar = ""
                            estado = 1
                    elif ord(l) == 116 and subestado == 1:
                        concatenar += l
                    elif ord(l) == 117 and subestado ==0:
                        concatenar += l
                    elif ord(l) == 118 and subestado == 1:
                        concatenar += l
                elif estado == 3:
                    concatenar += l
                elif estado == 1:
                    if aux == "valor":
                        concatenar = aux + l
                        estado = 0
                columna += 1
            elif self.comprobarsimbolos(l):
                if estado == 1:
                    if ord(l) == 34 and subestado == 1:
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                        estado = 3
                        texto = True
                    elif ord(l) == 39 and subestado == 2:
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                        estado = 3
                        texto = True
                    elif ord(l) == 44 and (subestado == 1 or subestado == 2):
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                        if subestado == 1:
                            estado = 1
                        else :
                            estado = 0
                            subestado = 1
                    elif ord(l) == 58 and (subestado == 1 or subestado == 2):
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                        if subestado == 2:
                            subestado = 1
                            estado = 0
                    elif ord(l) == 60 and subestado == 1: 
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                        estado = 0
                    elif ord(l) == 62 and (subestado == 0 or subestado == 1 or subestado == 2):
                        if subestado == 2:
                            self.listatoken.append (token('Simbolo', l, fila, columna))
                            subestado = 1
                        elif subestado == 0:
                            concatenar += l
                        elif subestado == 1:
                            self.listatoken.append (token('Simbolo', l, fila, columna))
                    elif ord(l) == 91 and (subestado == 0 or subestado == 1):
                        if subestado == 0:
                            self.listatoken[len(self.listatoken) - 1].valor = concatenar
                            concatenar = ""
                            subestado = 1 
                        else:
                            subestado = 2
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                    elif ord(l) == 93 and subestado == 1:
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                    elif ord(l) == 126 and subestado == 0:
                        self.listatoken.append (token('simbolo', "", fila, columna))
                        concatenar += l
                elif estado == 3:
                    if ord(l) == 34 and subestado == 1:
                        self.listatoken.append (token('Cadena', concatenar, fila, columna - len(concatenar)))
                        concatenar = ""
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                        estado = 1
                        subestado = 2
                    elif ord(l) == 39 and subestado == 2:
                        self.listatoken.append (token('Cadena', concatenar, fila, columna - len(concatenar)))
                        concatenar = ""
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                        texto = False
                    elif ord(l) == 44 and subestado == 2:
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                        estado = 1
                    elif ord(l) == 93 and subestado == 2:
                        self.listatoken.append (token('Simbolo', l, fila, columna))
                        estado = subestado = 1
                    else :
                        if subestado == 1 or subestado == 2:
                            concatenar += l

                columna += 1
        self.html()    
                

    def comprobarletras(self, caracter):
        if ord(caracter) >= 97 and ord(caracter) <= 122:
            return True 
        return False

    def comprobarsimbolos(self, caracter):
        if (ord(caracter) >= 33 and ord(caracter) <= 47) or (ord(caracter) >= 58 and ord(caracter) <= 64) or (ord(caracter) >= 91 and ord(caracter) <= 96 or (ord(caracter) >= 123 and ord(caracter) <= 126)): 
        
            return True 
        return False

    def html(self):
        armar = '''<html>
        <body> 
        <form>

        '''

        listacomponentes = []
        valor = ""
        fondo = ""
        evento = ""
        tipo = ""
        for i in range(len(self.listatoken)):
            if self.listatoken[i].valor == "tipo" and self.listatoken[i].tok == "Palabra reservada":
                tipo = self.listatoken[i+3].valor
            elif self.listatoken[i].valor == "valor" and self.listatoken[i].tok == "Palabra reservada":
                valor = self.listatoken[i+3].valor
            elif self.listatoken[i].valor == "fondo" and self.listatoken[i].tok == "Palabra reservada":
                fondo = self.listatoken[i+3].valor
            elif self.listatoken[i].valor == "evento" and self.listatoken[i].tok == "Palabra reservada":
                evento = self.listatoken[i+2].valor
            elif self.listatoken[i].valor == "valores" and self.listatoken[i].tok == "Palabra reservada":
                estado = 1
            elif (self.listatoken[i].valor == "\'" and self.listatoken[i].tok == "Simbolo" and self.listatoken[i-1].valor == "[" and self.listatoken[i-1].tok == "Simbolo") or (self.listatoken[i].valor == "\'" and self.listatoken[i].tok == "Simbolo" and self.listatoken[i-1].valor == "," and self.listatoken[i-1].tok == "Simbolo"):
                listacomponentes.append(self.listatoken[i+1].valor)
            elif self.listatoken[i].valor == ">" and self.listatoken[i].tok == "Simbolo":
                print(tipo + " " + valor + " " + fondo + " " + evento + " " + str(listacomponentes))
                if tipo == "etiqueta":
                    if valor != "":
                        armar += "<label>" + valor + "</label>\n"
                    else :
                        armar += "<label>label</label>\n"
                elif tipo == "texto":
                    if valor != "" and fondo != "":
                        armar += '''<input type = "text" placeholder = "'''+ fondo +'''">'''+ valor +'''</input>\n'''
                    elif valor == "" and fondo != "":
                        armar += '''<input type = "text" placeholder = "'''+ fondo +'''"></input>\n'''
                    elif valor != "" and fondo == "":
                        armar += '''<input type = "text">'''+ valor +'''</input>\n'''
                    elif valor == "" and fondo == "":
                        armar += '''<input type = "text"></input>\n'''
                elif tipo == "grupo-radio" or tipo == "grupo-option":
                    if valor != "":

                tipo = valor = evento = fondo = ""
                listacomponentes = []



            
     
    


                
                

