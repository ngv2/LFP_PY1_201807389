from select import select
from token import token
import webbrowser


class lectura:
    listatoken = None
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
                        self.listatoken.append (token('Simbolo', "", fila, columna))
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
        simbolo = ""
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
                if tipo == "etiqueta":
                    if valor != "":
                        armar += "<label>" + valor + "</label><br>\n"
                    else :
                        armar += "<label>label</label><br>\n"
                elif tipo == "texto":
                    if valor != "" and fondo != "":
                        armar += '''<input type = "text" placeholder = "'''+ fondo +'''" value = "'''+ valor +'''"><br>\n'''
                    elif valor == "" and fondo != "":
                        armar += '''<input type = "text" placeholder = "'''+ fondo +'''"><br>\n'''
                    elif valor != "" and fondo == "":
                        armar += '''<input type = "text" value = "'''+ valor +'''"><br>\n'''
                    elif valor == "" and fondo == "":
                        armar += '''<input type = "text"><br>\n'''
                elif tipo == "grupo-radio" or tipo == "grupo-option":
                    if valor != "" and len(listacomponentes) > 0:
                        armar += "<label>" + valor + ":</label>\n"
                        if tipo == "grupo-radio":
                            for el in listacomponentes:
                                armar += '''<input type = "radio" value = "''' + el + '''" name = "''' + valor + '''"> <label>'''+ el +''' </label>\n''' 
                            armar += "<br>"
                        else:
                            armar += "<select>\n"
                            armar += '''<option selected = "true" disabled = "disabled"> Elija </option>\n'''
                            for el in listacomponentes:
                                armar += '''<option value = "''' + el + '''">''' + el + '''</option>\n'''
                            armar += "</select><br>"
                    elif valor == "" and listacomponentes > 0:
                        armar += "<label>Opciones:</label>\n"
                        if tipo == "grupo-radio":
                            for el in listacomponentes:
                                armar += '''<input type = "radio" value = "''' + el + '''" name = "opcion"> <label>'''+ el +''' </label>\n''' 
                            armar += "<br>"
                        else:
                            armar += "<select>\n"
                            armar += '''<option selected = "true" disabled = "disabled"> Elija </option>\n'''
                            for el in listacomponentes:
                                armar += '''<option value = "''' + el + '''">''' + el + '''</option>\n'''
                            armar += "</select><br>"
                elif tipo == "boton":
                    if valor != "" and evento != "":
                        if evento == "entrada":
                            armar += '''<button onclick="clickf(event)">'''+ valor + '''</button>\n'''
                        elif evento == "info":
                            armar += '''<button onclick="clickf2(event)">''' + valor + '''</button>\n'''
                    elif valor == "" and evento != "":
                        if evento == "entrada":
                            armar += '''<button onclick="clickf(event)"> Boton </button>\n'''
                        elif evento == "info":
                            armar += '''<button onclick="clickf2(event)"> Boton </button>\n'''
                    elif valor == "" and evento == "":
                        armar += '''<button> Boton </button>\n'''

                tipo = valor = evento = fondo = ""
                listacomponentes = []

        armar += '''</form>
        <div id = "contenedor"></div><br>\n'''
        armar += ''' <script>
            function clickf(ev){
                ev.preventDefault();
                var divc=document.getElementById("contenedor");
                var escribiendo=document.createElement("iframe");
                escribiendo.setAttribute("src", "''' + self.linkarchivo + '''");
                divc.appendChild(escribiendo);
            }
            function clickf2(ev){
                ev.preventDefault();
                var info="";
                var divc=document.getElementById("contenedor");
                var escribiendo=document.createElement("iframe");
                var inputI=document.getElementsByTagName("input");
                var selectI=document.getElementsByTagName("select");
                for (i=0; i<inputI.length; i++){
                    if(inputI[i].type == "radio"){
                        if(inputI[i].checked == true){
                            info += "<p>" + inputI[i].value + "</p>";
                        }
                    }else{
                        info += "<p>" + inputI[i].value + "</p>";
                    }
                }
                for (i=0; i<selectI.length; i++){
                    if(selectI[i].selectedIndex > 0){
                        info+= "<p>" + selectI[i].options[selectI[i].selectedIndex].value + "</p>";
                    }
                }                    
                escribiendo.setAttribute("srcdoc", info);
                divc.appendChild(escribiendo);
            }
        </script> 
        </body>
        </html>'''
        nuevo = open('formulario.html', 'w')
        nuevo.write(armar)
        webbrowser.open('formulario.html')

    def obtenerlink(self, obtener):
        self.linkarchivo = obtener

    def generarhtml(self):
        docHTML = open('reporteTokens.html','w')
 
        head = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
 
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        </head>
        <body>
    <table class="table">
  <thead>
    <tr>
      <th scope="col">Token</th>
      <th scope="col">Lexema</th>
      <th scope="col">Fila</th>
      <th scope="col">Columna</th>
    </tr>
  </thead>
  <tbody>
        '''
        docHTML.write(head)
        for i in self.listatoken:
            #if i.tipo != tipos.DESCONOCIDO:
                docHTML.write('\n\t\t <tr class="table-success">')
                docHTML.write('\n\t\t\t<th scope = "row">'+str(i.getTok()))
                docHTML.write('</th>')
                docHTML.write('\n\t\t\t<td>'+str(i.getValor()))
                docHTML.write('</td>')
                docHTML.write('\n\t\t\t<td>'+ str(i.getFila()))
                docHTML.write('</td>')
                docHTML.write('\n\t\t\t<td>'+ str(i.getColumna()))
                docHTML.write('</td>')
                docHTML.write('\n\t\t </tr>') 
 
        docHTML.write('\n\t </tbody>')
        docHTML.write('\n</table>')
        docHTML.write('\n</body')
        docHTML.write('\n</html>')
 
        #cerrar archivo una vez termine de escribirlo
        docHTML.close()
 
        webbrowser.open_new_tab('reporteTokens.html')

    def generarhtmlE(self):
        docHTML = open('reporteErrores.html','w')
 
        head = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
 
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        </head>
        <body>
    <table class="table">
  <thead>
    <tr>
      <th scope="col">Token</th>
      <th scope="col">Lexema</th>
      <th scope="col">Fila</th>
      <th scope="col">Columna</th>
    </tr>
  </thead>
  <tbody>
        '''
        docHTML.write(head)
        docHTML.write('\n\t\t <tr class="table-success">')
        docHTML.write('\n\t\t\t<th scope = "row">')
        docHTML.write('</th>')
        docHTML.write('\n\t\t\t<td>')
        docHTML.write('</td>')
        docHTML.write('\n\t\t\t<td>')
        docHTML.write('</td>')
        docHTML.write('\n\t\t\t<td>')
        docHTML.write('</td>')
        docHTML.write('\n\t\t </tr>') 
        docHTML.write('\n\t </tbody>')
        docHTML.write('\n</table>')
        docHTML.write('\n</body')
        docHTML.write('\n</html>')
 
        #cerrar archivo una vez termine de escribirlo
        docHTML.close()
 
        webbrowser.open_new_tab('reporteErrores.html')