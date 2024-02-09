import array
import subprocess
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal,QProcess
from PyQt5.QtWidgets import QMessageBox

class TopicThread(QThread):
    nueva_respuesta = pyqtSignal(list)
    salida = str
    salida_aux = str
    salida_aux2 = list

    def __init__(self):
        super().__init__()

    def run(self):
        comando = "ros2 topic list"
        self.salida = subprocess.check_output(comando, shell= True, universal_newlines= True)

    def topicInfo(self,comando):
        self.salida_aux = subprocess.check_output(comando, shell= True, universal_newlines= True)

    def topicInfo2(self,topic):
        salida_aux = subprocess.check_output('ros2 topic info ' + topic,shell= True, universal_newlines= True)
        aux,aux1,aux2 = "","",""
        count = 0
        for line1 in salida_aux.split('\n'):
            count = count + 1
            if count == 1:
                aux = line1.split(" ")[1]
            if count == 2:
                aux1 = line1.split(" ")[2]
            if count == 3:
                aux2 = line1.split(" ")[2]
        text_array = ['ROS2 Topic',topic,aux,aux1,aux2]
        self.salida_aux2 = text_array

    def topicEcho(self,topic):
        reply = QMessageBox.question(None, 'Aviso','Al seleccionar esta opcioón se desplegará una termianl en la que visualizar la ejecucion del comando. ¿Desea continuar? \n Para finalizar ctrl+c',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            comand = 'gnome-terminal -- ros2 topic echo ' + topic
            proceso = subprocess.Popen(comand, shell=True)
            tiempo_limite = 1
            time.sleep(tiempo_limite)

            proceso.terminate()
