from PySide6.QtWidgets import QMainWindow

from src.UI.vtnPrincipal import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self). __init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnBorrar.clicked.connect(self.borrar)

    def guardar(self):
        print(self.ui.txtNombre.text())
        print(self.ui.txtApellido.text())
        print(self.ui.txtCedula.text())
        print(self.ui.txtemail.text())
        print(self.ui.cbsexo.currentText())
        print('Se hizo clic en el boton guardar')

    def borrar(self):
        self.ui.txtNombre.setText("")
        self.ui.txtApellido.setText("")
        self.ui.txtCedula.setText("")
        print('Se hizo clic en el boton borrar')