from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.UI.vtnPrincipal import Ui_vtnPrincipal
from src.datos.personaDao import PersonaDao
from src.dominio.persona import Persona


class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnNuevo.clicked.connect(self.nuevo)
        self.ui.btnLimpiar.clicked.connect(self.accion_borrar)
        self.ui.btnBuscarCedula.clicked.connect(self.buscar)
        self.ui.txtCedula.setValidator(QIntValidator())
        self.ui.txtBuscarCedula.setValidator(QIntValidator())

    def nuevo(self):
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
        #self.ui.statusbar.showMessage('Se guardó la información', 3000)

        # Mostrar datos por consola

        persona = Persona(nombre=self.ui.txtNombre.text(),
                          apellido=self.ui.txtApellido.text(),
                          cedula=self.ui.txtCedula.text(),
                          email=self.ui.txtEmail.text(),
                          sexo=self.ui.cbSexo.currentText()[0])
        print(persona)

        if PersonaDao.insertar_persona(persona)== -1:
            QMessageBox.critical(self, 'Error', 'No se pudo guardar la persona.')

        else:
            self.ui.statusbar.showMessage('Se guardó la información', 3000)
            # Limpiar campos sin mostrar mensaje de borrar
            self.limpiar()

    def accion_borrar(self):
        self.limpiar(True)

    def limpiar(self, mostrar_mensaje=False):
        self.ui.txtNombre.setText("")
        self.ui.txtApellido.setText("")
        self.ui.txtCedula.setText("")
        self.ui.txtEmail.setText("")
        self.ui.cbSexo.setCurrentText("Seleccionar")

        if mostrar_mensaje:
            print('Se hizo clic en el botón borrar')



    def buscar(self):
        if len(self.ui.txtBuscarCedula.text()) != 10:
            QMessageBox.warning(self, "Advertencia", "La cédula debe tener exactamente 10 dígitos.")
        else:
            persona = PersonaDao.seleccionar_persona(self.ui.txtBuscarCedula.text())
            self.ui.txtNombre.setText(persona.nombre)
            self.ui.txtApellido.setText(persona.apellido)
            self.ui.txtCedula.setText(persona.cedula)
            self.ui.txtEmail.setText(persona.email)



