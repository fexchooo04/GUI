from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow

from src.UI.vtnPrincipal import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self). __init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnBorrar.clicked.connect(self.borrar)
        self.ui.txtCedula.setValidator(QIntValidator())

    #def guardar(self):
        #if self.ui.txtNombre.text() == "" or self.ui.txtApellido.text() == "":
            #print('Ingrese todos los datos.')
        #else:
            #print ('Se puede guardar.')
            #print(self.ui.txtNombre.text())
            #print(self.ui.txtApellido.text())
           #print(self.ui.txtCedula.text())
            #print(self.ui.txtemail.text())
           #print(self.ui.cbsexo.currentText())
            #print('Se hizo clic en el boton guardar')

    def guardar(self):
        if (self.ui.txtNombre.text() == "" or
                self.ui.txtApellido.text() == "" or
                self.ui.txtCedula.text() == "" or
                self.ui.txtEmail.text() == "" or
                self.ui.cbSexo.currentText() not in ["Masculino", "Femenino"]):
            print('Ingrese todos los datos.')
        else:
            print('Se puede guardar.')
            print(self.ui.txtNombre.text())
            print(self.ui.txtApellido.text())
            print(self.ui.txtCedula.text())
            print(self.ui.txtEmail.text())
            print(self.ui.cbSexo.currentText())

    def borrar(self):
        self.ui.txtNombre.setText("")
        self.ui.txtApellido.setText("")
        self.ui.txtCedula.setText("")
        self.ui.txtEmail.setText("")
        self.ui.cbSexo.setCurrentText("Seleccionar")
        print('Se hizo clic en el boton borrar')
