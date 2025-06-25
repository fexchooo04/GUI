from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.UI.vtnPrincipal import Ui_vtnPrincipal

class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)

        # Conectamos los botones con los métodos correspondientes
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnBorrar.clicked.connect(self.accion_borrar)

        # Solo permite números en el campo de cédula
        self.ui.txtCedula.setValidator(QIntValidator())

    def guardar(self):
        if (self.ui.txtNombre.text() == "" or
            self.ui.txtApellido.text() == "" or
            self.ui.txtCedula.text() == "" or
            self.ui.txtEmail.text() == "" or
            self.ui.cbSexo.currentText() not in ["Masculino", "Femenino"]):
            QMessageBox.information(self, "Advertencia", "Ingrese todos los datos.")
            return

        if len(self.ui.txtCedula.text()) != 10:
            QMessageBox.warning(self, "Advertencia", "La cédula debe tener exactamente 10 dígitos.")
            return

        # Mostrar mensaje en la barra de estado
        self.ui.statusbar.showMessage('Se guardó la información', 3000)

        # Mostrar datos por consola
        print(self.ui.txtNombre.text())
        print(self.ui.txtApellido.text())
        print(self.ui.txtCedula.text())
        print(self.ui.txtEmail.text())
        print(self.ui.cbSexo.currentText())
        print('Se hizo clic en el botón guardar')

        # Limpiar campos sin mostrar mensaje de borrar
        self.borrar()

    def accion_borrar(self):
        self.borrar(True)

    def borrar(self, mostrar_mensaje=False):
        self.ui.txtNombre.setText("")
        self.ui.txtApellido.setText("")
        self.ui.txtCedula.setText("")
        self.ui.txtEmail.setText("")
        self.ui.cbSexo.setCurrentText("Seleccionar")

        if mostrar_mensaje:
            print('Se hizo clic en el botón borrar')