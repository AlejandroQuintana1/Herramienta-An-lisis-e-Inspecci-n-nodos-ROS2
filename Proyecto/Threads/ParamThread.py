import subprocess
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox

class ParamThread(QThread):
    nueva_respuesta = pyqtSignal(list)
    salida = str
    salida_aux = str
    salida_aux2 = str
    salida_aux3 = str

    def __init__(self):
        super().__init__()

    def run(self):
        comando = "ros2 param list"
        self.salida = subprocess.check_output(comando, shell= True, universal_newlines= True)

    def paramGet(self,comando):
        cmd = "ros2 param get " + comando
        try:
            self.salida_aux = subprocess.check_output(cmd,stderr=subprocess.STDOUT ,text=True,shell= True, universal_newlines= True)
        except subprocess.CalledProcessError as e:
            self.salida_aux = e.output

    def paramDescribe(self,comando):
        cmd = "ros2 param describe " + comando
        try:
            self.salida_aux2 = subprocess.check_output(cmd,stderr=subprocess.STDOUT ,text=True,shell= True, universal_newlines= True)
        except subprocess.CalledProcessError as e:
            self.salida_aux2 = e.output

    def paramDelete(self,comando):
        cmd = "ros2 param delete " + comando
        reply = QMessageBox.question(None, 'Aviso','Estas a punto de intentar borrar un parametro. ¿Desea continuar? ',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                self.salida_aux3 = subprocess.check_output(cmd,stderr=subprocess.STDOUT ,text=True,shell= True, universal_newlines= True)
            except subprocess.CalledProcessError as e:
                self.salida_aux3 = e.output