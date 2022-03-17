
from calendar import c
from re import sub


class lectura:
    def leyendo(self, contenido):
        contenido = contenido.lower()
        estado = 0
        subestado = 0
        concatenar = ""
        fila = 1
        columna = 1
        patron = 0
        
        for l in contenido:
            if l == "\n":
                fila += 1 
                columna = 1
            elif l == " ":
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
                            print(concatenar)
                            concatenar = ""
                            subestado = 1
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
                            print(concatenar)
                            concatenar = ""
                            estado = 1
                        elif concatenar == "tipo":
                            print(concatenar)
                            concatenar = ""
                            estado = 1
                        elif concatenar == "fondo":
                            print(concatenar)
                            concatenar = ""
                            estado = 1
                        elif concatenar == "evento":
                            print(concatenar)
                            concatenar = ""
                            estado = 1
                        elif concatenar == "info":
                            print(concatenar)
                            concatenar = ""
                            estado = 1
                    elif ord(l) == 112 and subestado == 1:
                        concatenar += l
                    elif ord(l) == 114 and (subestado ==0 or subestado == 1):
                        concatenar += l
                        if concatenar == "valor":
                            print(concatenar)
                            concatenar = ""
                            estado = 1
                    elif ord(l) == 115 and subestado == 1:
                        concatenar += l
                        if concatenar == "valores":
                            print(concatenar)
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
                columna += 1
            elif self.comprobarsimbolos(l):
                if estado == 1:
                    if ord(l) == 34 and subestado == 1:
                        print(l)
                        estado = 3
                    elif ord(l) == 39 and subestado == 1:
                        print(l)
                    elif ord(l) == 44 and subestado == 1:
                        print(l)
                    elif ord(l) == 58 and subestado == 1:
                        print(l)
                    elif ord(l) == 60 and subestado == 1: 
                        print(l)
                        estado = 1
                    elif ord(l) == 62 and (subestado == 0 or subestado == 1):
                        print(l)
                    elif ord(l) == 91 and (subestado == 0 or subestado == 1):
                        print(l)
                        if subestado == 0:
                            subestado = 1 
                    elif ord(l) == 93 and subestado == 1:
                        print(l)
                    elif ord(l) == 126 and subestado == 0:
                        print(l)
                elif estado == 3:
                    if ord(l) == 34 and subestado == 1:
                        print(concatenar)
                        concatenar = ""
                        print(l)
                        estado = 1
                columna += 1
                

    def comprobarletras(self, caracter):
        if ord(caracter) >= 97 and ord(caracter) <= 122:
            return True 
        return False

    def comprobarsimbolos(self, caracter):
        if (ord(caracter) >= 33 and ord(caracter) <= 47) or (ord(caracter) >= 58 and ord(caracter) <= 64) or (ord(caracter) >= 91 and ord(caracter) <= 96 or (ord(caracter) >= 123 and ord(caracter) <= 126)): 
        
            return True 
        return False
    


                
                

