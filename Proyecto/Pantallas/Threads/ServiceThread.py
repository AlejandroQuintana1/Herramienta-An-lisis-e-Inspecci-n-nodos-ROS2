import subprocess
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class ServiceThread(QThread):
    nueva_respuesta = pyqtSignal(list)
    salida = str
    salida_aux = str
    salida_aux2 = str
    salida_aux3 = str

    def __init__(self):
        super().__init__()

    def run(self):
        comando = "ros2 service list"
        self.salida = subprocess.check_output(comando, shell= True, universal_newlines= True)

    def serviceType(self,comando):
        cmd = 'ros2 service type ' + comando
        self.salida_aux = subprocess.check_output(cmd, shell= True, universal_newlines= True)

    def serviceFind(self,comando):
        cmd = 'ros2 service find ' + comando
        self.salida_aux2 = subprocess.check_output(cmd, shell= True, universal_newlines= True)

    def serviceCall(self,comando):
        cmd = 'ros2 service call ' + comando
        self.salida_aux3 = subprocess.check_output(cmd, shell= True, universal_newlines= True)
