import subprocess
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class NodeThread(QThread):
    nueva_respuesta = pyqtSignal(list)
    salida = str
    salida_aux = list

    def __init__(self):
        super().__init__()

    def run(self):
        comando = "ros2 node list"
        self.salida = subprocess.check_output(comando, shell= True, universal_newlines= True)

    def nodeInfo(self,comando):
        cmd = "ros2 node info " + comando
        try:
            self.salida = subprocess.check_output(cmd,stderr=subprocess.STDOUT ,text=True,shell= True, universal_newlines= True)
        except subprocess.CalledProcessError as e:
            self.salida_aux = e.output
            return
        self.salida_aux = self.salida.split("\n")
    