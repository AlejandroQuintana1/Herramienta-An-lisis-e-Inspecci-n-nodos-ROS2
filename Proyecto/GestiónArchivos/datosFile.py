import sys
from PyQt5.QtWidgets import QFileDialog,QDialog, QMessageBox, QLineEdit, QPushButton,QFormLayout

class DatosFile():

    consultas = []
    respuestas_tbl = []
    comandos = []
    respuestas_terminal = []

    def __init__(self):
        super().__init__()

    def getConsultas(self):
        return self.consultas
    
    def getRespuestasTbl(self):
        return self.respuestas_tbl
    
    def getComandos(self):
        return self.comandos
    
    def getRespuestasTerminal(self):
        return self.respuestas_terminal

    def saveConsultas(self,file_name):
        try:
            with open(file_name, 'w') as file:
                file.write("Listado de consultas realizadas:\n")
                file.write("\n")
                count = 0
                for line in self.consultas:
                    try:
                        cadena = str(count+1) + "º" + " " + line + "\n"
                        file.write(cadena)
                        cadena = self.respuestas_tbl[count]
                        file.write(cadena)
                        count = count + 1
                        file.write("\n")
                    except Exception as e:
                        file.write("\n")
                        file.write("\n")
                        file.write(str(e))
                        file.write("\n")
                        file.write("\n")
                        continue
            QMessageBox.information(None,"Exito","Archivo guardado correctamente")
        except Exception as e:
            QMessageBox.critical(None,"Error",f"El archivo no se ha podido guardar\nError: {str(e)}")
            print(e)

    def saveComandos(self,file_name):
        try:
            with open(file_name, 'w') as file:
                file.write("Listado de comandos realizadas:\n")
                file.write("\n")
                count = 0
                for line in self.comandos:
                    try:
                        cadena = str(count+1) + "º" + " " + line + "\n"
                        file.write(cadena)
                        cadena = self.respuestas_terminal[count]
                        file.write(cadena)
                        file.write("\n")
                    except Exception as e:
                        file.write("\n")
                        file.write("\n")
                        file.write(str(e))
                        file.write("\n")
                        file.write("\n")
                        continue
            QMessageBox.information(None,"Exito","Archivo guardado correctamente")
        except Exception as e:
            QMessageBox.critical(None,"Error",f"El archivo no se ha podido guardar\nError: {str(e)}")
            print(e)
    
    def saveTodo(self,file_name):
        try:
            with open(file_name, 'w') as file:
                file.write("Listado de todas las consultas y comandos realizadas:\n")
                file.write("\n")
                count = 0
                print(len(self.consultas))
                print(len(self.respuestas_tbl))
                print(len(self.comandos))
                print(len(self.respuestas_terminal))
                for line in self.consultas:
                    try:
                        cadena = str(count+1) + "º" + " " + line + "\n"
                        file.write(cadena)
                        cadena = self.respuestas_tbl[count]
                        file.write(cadena)
                        count = count + 1
                        file.write("\n")
                    except Exception as e:
                        file.write("\n")
                        file.write("\n")
                        file.write(str(e))
                        file.write("\n")
                        file.write("\n")
                        continue
                count = 0
                for line in self.comandos:
                    try:
                        cadena = str(count+1) + "º" + " " + line + "\n"
                        file.write(cadena)
                        cadena = self.respuestas_terminal[count]
                        file.write(cadena)
                        file.write("\n")
                    except Exception as e:
                        file.write("\n")
                        file.write("\n")
                        file.write(str(e))
                        file.write("\n")
                        file.write("\n")
                        continue
            QMessageBox.information(None,"Exito","Archivo guardado correctamente")
        except Exception as e:
            QMessageBox.critical(None,"Error",f"El archivo no se ha podido guardar\nError: {str(e)}")
            print(e)
