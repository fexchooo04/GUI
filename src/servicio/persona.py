from PySide6.QtWidgets import QMainWindow

from src.UI.vtnPrincipal import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self). __init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)

    def guardar(self):
        print('Se hizo clic en el boton guardar')
