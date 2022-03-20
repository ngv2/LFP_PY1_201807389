
class token:
    valor = ""
    fila = 0
    columna = 0
    tok = ""

    def __init__(self, tok, valor, fila, columna):
        self.tok = tok
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def getValor(self):
        return self.valor

    def getFila (self):
        return self.fila
    
    def getColumna (self):
        return self.columna
    
    def getTok (self):
        return self.tok