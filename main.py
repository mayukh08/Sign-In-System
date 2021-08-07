import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine


#This is the code for connecting the UI layer with the python file

#We have created a separate python file which consists of all the required classes and functions. 
#from that file we ar importing the backend class
from func import Backend

#Initializing the GUI application
app = QGuiApplication(sys.argv)

#Setting the Application engine and loading the qml file into it
engine = QQmlApplicationEngine()
engine.load('UI/main.qml')

#Initializing the "Backend" class into the variable "back_end"
back_end = Backend()
engine.rootObjects()[0].setProperty('backend', back_end)

#quitting the application engine 
engine.quit.connect(app.quit)

sys.exit(app.exec())
