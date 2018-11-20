import subprocess

class MiReporte():
    def __init__(self, nombre):
        self.nombre = nombre + '.tex'
        self.archivo = open(self.nombre, 'w')
        self.contador = 1

    def iniciarReporte(self, titulo, autor, anio):
        self.archivo.write("\\documentclass{article}\n")
        self.archivo.write("\\usepackage{pgfplots}\n")
        self.archivo.write("\\usepackage[spanish]{babel}\n")
        self.archivo.write("\\usepackage[utf8]{inputenc}\n")
        self.archivo.write("\\usepackage[T1]{fontenc}\n")
        self.archivo.write("\\title{" + titulo + " \\ A\\~no " + anio + "}\n")
        self.archivo.write("\\author{Usuario: " + autor + "}\n")
        self.archivo.write("\\date{\\today}\n")
        self.archivo.write("\\begin{document}\n")
        self.archivo.write("\\maketitle\n")
    
    def iniciarCentrar(self):
        self.archivo.write("\\begin{center}\n")
    
    def terminarCentrar(self):
        self.archivo.write("\\end{center}\n")

    def setSection(self, texto):
        self.archivo.write("\\section*{" + texto + "}\n")

    def iniciarGrafica(self, NoBarras):
        tx = '{'
        for i in range(NoBarras):
            tx += '(' + str(i+1) + ')'
            if (i+1) != NoBarras:
                tx += ','
        tx += '}'

        self.archivo.write("\\begin{tikzpicture}\n")
        self.archivo.write("    \\begin{axis}[\n")
        self.archivo.write("        symbolic x coords={},\n".format(tx))
        self.archivo.write("        xtick=data\n")
        self.archivo.write("        ]\n")
        self.archivo.write("        \\addplot[ybar,fill=blue] coordinates {\n")

    def agregarBarra(self, info):
        self.archivo.write("            (({}),{})\n".format(self.contador, info))
        self.contador += 1

    def terminarGrafica(self):
        self.archivo.write("        };\n")
        self.archivo.write("    \\end{axis}\n")
        self.archivo.write("\\end{tikzpicture}\n")

    def iniciarTabla(self, NoColumnas, encabezados):
        tx = '|c'*NoColumnas
        tx += '|'
        self.archivo.write("\\begin{tabular}{" + tx + "}\n")
        self.archivo.write("\\hline \n")
        j = 0
        for e in encabezados:
            self.archivo.write(e)
            j += 1
            if j < len(encabezados):
                self.archivo.write(' & ')
            else:
                self.archivo.write(' \\\\ \n')
        self.archivo.write("\\hline \n")

    def terminarTabla(self):
        self.archivo.write("\\end{tabular}\n")
        self.contador = 1

    def escribirFila(self, info):
        j = 0
        self.archivo.write(str(self.contador))
        self.archivo.write(' & ')
        for i in info:
            self.archivo.write(i)
            j += 1
            if j < len(info):
                self.archivo.write(' & ')
            else:
                self.archivo.write(' \\\\ \n')
        self.archivo.write("\\hline \n")
        self.contador += 1

    def iniciarLista(self):
        self.archivo.write("\\begin{enumerate}\n")
    
    def agregarItem(self, texto):
        self.archivo.write("    \\item {}\n".format(texto))

    def terminarLista(self):
        self.archivo.write("\\end{enumerate}\n")

    def terminarReporte(self):
        self.archivo.write("\n")
        self.archivo.write("\\end{document} \n")
        self.archivo.close()

    def compilarReporte(self):
        subprocess.call(["pdflatex", self.nombre])
        subprocess.call(["rm", self.nombre.replace('.tex', '.log'), self.nombre.replace('.tex', '.aux')])
        #subprocess.call(["rm", self.nombre])
    
    def getNombre(self):
        return self.nombre