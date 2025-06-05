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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(706, 445)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbNombre = QLabel(self.centralwidget)
        self.lbNombre.setObjectName(u"lbNombre")
        self.lbNombre.setGeometry(QRect(90, 30, 91, 21))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbNombre.setFont(font)
        self.lbApellido = QLabel(self.centralwidget)
        self.lbApellido.setObjectName(u"lbApellido")
        self.lbApellido.setGeometry(QRect(90, 60, 91, 31))
        self.lbApellido.setFont(font)
        self.lbCedula = QLabel(self.centralwidget)
        self.lbCedula.setObjectName(u"lbCedula")
        self.lbCedula.setGeometry(QRect(90, 100, 81, 21))
        self.lbCedula.setFont(font)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(180, 30, 371, 20))
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(180, 70, 371, 20))
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(170, 100, 381, 20))
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(220, 170, 81, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.btnGuardar.setFont(font1)
        self.btnBorrar = QPushButton(self.centralwidget)
        self.btnBorrar.setObjectName(u"btnBorrar")
        self.btnBorrar.setGeometry(QRect(360, 170, 75, 31))
        self.btnBorrar.setFont(font1)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 706, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema de Gestion del Personal", None))
        self.lbNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lbApellido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.lbCedula.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00e9dula:", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.btnBorrar.setText(QCoreApplication.translate("vtnPrincipal", u"Borrar", None))
    # retranslateUi

