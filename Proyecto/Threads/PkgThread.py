import subprocess
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class PkgThread(QThread):
    nueva_respuesta = pyqtSignal(list)
    salida = str
    salida_aux = str
    salida_aux1 = str

    def __init__(self):
        super().__init__()

    def run(self):
        comando = "ros2 pkg list"
        self.salida = subprocess.check_output(comando, shell= True, universal_newlines= True)

    def pkgExecutable(self,comando):
        cmd = "ros2 pkg executables " + comando
        try:
            self.salida_aux = subprocess.check_output(cmd,stderr=subprocess.STDOUT ,text=True,shell= True, universal_newlines= True)
        except subprocess.CalledProcessError as e:
            self.salida_aux = e.output
    
    def pkgPrefix(self,comando):
        cmd = "ros2 pkg prefix " + comando
        try:
            self.salida_aux1 = subprocess.check_output(cmd,stderr=subprocess.STDOUT ,text=True,shell= True, universal_newlines= True)
        except subprocess.CalledProcessError as e:
            self.salida_aux1 = e.output
            