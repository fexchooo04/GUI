# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(706, 445)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(220, 170, 81, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btnGuardar.setFont(font)
        self.btnBorrar = QPushButton(self.centralwidget)
        self.btnBorrar.setObjectName(u"btnBorrar")
        self.btnBorrar.setGeometry(QRect(370, 170, 75, 31))
        self.btnBorrar.setFont(font)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(90, 20, 79, 130))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.lbNombre = QLabel(self.splitter)
        self.lbNombre.setObjectName(u"lbNombre")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lbNombre.setFont(font1)
        self.splitter.addWidget(self.lbNombre)
        self.lbApellido = QLabel(self.splitter)
        self.lbApellido.setObjectName(u"lbApellido")
        self.lbApellido.setFont(font1)
        self.splitter.addWidget(self.lbApellido)
        self.lbCedula = QLabel(self.splitter)
        self.lbCedula.setObjectName(u"lbCedula")
        self.lbCedula.setFont(font1)
        self.splitter.addWidget(self.lbCedula)
        self.lbSexo = QLabel(self.splitter)
        self.lbSexo.setObjectName(u"lbSexo")
        self.lbSexo.setFont(font1)
        self.splitter.addWidget(self.lbSexo)
        self.lbEmail = QLabel(self.splitter)
        self.lbEmail.setObjectName(u"lbEmail")
        self.lbEmail.setFont(font1)
        self.splitter.addWidget(self.lbEmail)
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(180, 21, 361, 132))
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.txtNombre = QLineEdit(self.splitter_2)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setMaxLength(50)
        self.splitter_2.addWidget(self.txtNombre)
        self.txtApellido = QLineEdit(self.splitter_2)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setMaxLength(50)
        self.splitter_2.addWidget(self.txtApellido)
        self.txtCedula = QLineEdit(self.splitter_2)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setMaxLength(10)
        self.splitter_2.addWidget(self.txtCedula)
        self.cbSexo = QComboBox(self.splitter_2)
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.setObjectName(u"cbSexo")
        self.splitter_2.addWidget(self.cbSexo)
        self.txtEmail = QLineEdit(self.splitter_2)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setMaxLength(100)
        self.splitter_2.addWidget(self.txtEmail)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 706, 33))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema de Gestion del Personal", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.btnBorrar.setText(QCoreApplication.translate("vtnPrincipal", u"Borrar", None))
        self.lbNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lbApellido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.lbCedula.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00e9dula:", None))
        self.lbSexo.setText(QCoreApplication.translate("vtnPrincipal", u"Sexo:", None))
        self.lbEmail.setText(QCoreApplication.translate("vtnPrincipal", u"E-mail", None))
        self.cbSexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccionar", None))
        self.cbSexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Masculino", None))
        self.cbSexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Femenino", None))

    # retranslateUi


