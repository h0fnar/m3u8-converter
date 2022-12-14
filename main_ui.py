# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(526, 216)
        Dialog.setMinimumSize(QtCore.QSize(526, 216))
        Dialog.setMaximumSize(QtCore.QSize(526, 216))
        Dialog.setAcceptDrops(False)
        self.lineEdit_find = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_find.setGeometry(QtCore.QRect(20, 90, 361, 21))
        self.lineEdit_find.setObjectName("lineEdit_find")
        self.lineEdit_replace = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_replace.setGeometry(QtCore.QRect(20, 140, 361, 21))
        self.lineEdit_replace.setObjectName("lineEdit_replace")
        self.label_find = QtWidgets.QLabel(Dialog)
        self.label_find.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_find.setObjectName("label_find")
        self.lineEdit_folder = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_folder.setEnabled(True)
        self.lineEdit_folder.setGeometry(QtCore.QRect(20, 30, 361, 21))
        self.lineEdit_folder.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_folder.setObjectName("lineEdit_folder")
        self.label_folder = QtWidgets.QLabel(Dialog)
        self.label_folder.setGeometry(QtCore.QRect(20, 10, 60, 16))
        self.label_folder.setObjectName("label_folder")
        self.label_replace = QtWidgets.QLabel(Dialog)
        self.label_replace.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_replace.setObjectName("label_replace")
        self.button_select = QtWidgets.QPushButton(Dialog)
        self.button_select.setGeometry(QtCore.QRect(400, 30, 113, 32))
        self.button_select.setAutoDefault(False)
        self.button_select.setDefault(False)
        self.button_select.setFlat(False)
        self.button_select.setObjectName("button_select")
        self.button_convert = QtWidgets.QPushButton(Dialog)
        self.button_convert.setGeometry(QtCore.QRect(400, 180, 113, 32))
        self.button_convert.setMouseTracking(False)
        self.button_convert.setAutoDefault(True)
        self.button_convert.setDefault(True)
        self.button_convert.setFlat(False)
        self.button_convert.setObjectName("button_convert")
        self.button_quit = QtWidgets.QPushButton(Dialog)
        self.button_quit.setGeometry(QtCore.QRect(290, 180, 113, 32))
        self.button_quit.setAutoDefault(False)
        self.button_quit.setObjectName("button_quit")
        self.label_image_1 = QtWidgets.QLabel(Dialog)
        self.label_image_1.setGeometry(QtCore.QRect(410, 70, 91, 91))
        self.label_image_1.setToolTip("")
        self.label_image_1.setToolTipDuration(1)
        self.label_image_1.setWhatsThis("")
        self.label_image_1.setText("")
        self.label_image_1.setPixmap(QtGui.QPixmap(":/images/img/icon.png"))
        self.label_image_1.setScaledContents(True)
        self.label_image_1.setObjectName("label_image_1")
        self.checkBox_utf8 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_utf8.setGeometry(QtCore.QRect(20, 180, 131, 20))
        self.checkBox_utf8.setChecked(True)
        self.checkBox_utf8.setObjectName("checkBox_utf8")
        self.checkBox_find_replace = QtWidgets.QCheckBox(Dialog)
        self.checkBox_find_replace.setGeometry(QtCore.QRect(150, 180, 131, 20))
        self.checkBox_find_replace.setChecked(True)
        self.checkBox_find_replace.setObjectName("checkBox_find_replace")
        self.label_count = QtWidgets.QLabel(Dialog)
        self.label_count.setEnabled(True)
        self.label_count.setGeometry(QtCore.QRect(180, 10, 201, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_count.setFont(font)
        self.label_count.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_count.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.label_count.setObjectName("label_count")
        self.lineEdit_replace.raise_()
        self.lineEdit_find.raise_()
        self.label_find.raise_()
        self.label_folder.raise_()
        self.label_replace.raise_()
        self.button_select.raise_()
        self.button_convert.raise_()
        self.button_quit.raise_()
        self.label_image_1.raise_()
        self.checkBox_utf8.raise_()
        self.checkBox_find_replace.raise_()
        self.lineEdit_folder.raise_()
        self.label_count.raise_()

        self.retranslateUi(Dialog)
        self.button_select.clicked.connect(Dialog.select_button_clicked) # type: ignore
        self.button_quit.clicked.connect(Dialog.quit_button_clicked) # type: ignore
        self.button_convert.clicked.connect(Dialog.convert_button_clicked) # type: ignore
        self.checkBox_utf8.stateChanged['int'].connect(Dialog.utf8_checkbox) # type: ignore
        self.checkBox_find_replace.stateChanged['int'].connect(Dialog.find_replace_checkbox) # type: ignore
        self.lineEdit_folder.textEdited['QString'].connect(Dialog.line_folder) # type: ignore
        self.lineEdit_find.textEdited['QString'].connect(Dialog.line_find) # type: ignore
        self.lineEdit_replace.textEdited['QString'].connect(Dialog.line_replace) # type: ignore
        self.label_count.objectNameChanged['QString'].connect(Dialog.label_count) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_folder, self.button_select)
        Dialog.setTabOrder(self.button_select, self.lineEdit_find)
        Dialog.setTabOrder(self.lineEdit_find, self.lineEdit_replace)
        Dialog.setTabOrder(self.lineEdit_replace, self.checkBox_utf8)
        Dialog.setTabOrder(self.checkBox_utf8, self.checkBox_find_replace)
        Dialog.setTabOrder(self.checkBox_find_replace, self.button_quit)
        Dialog.setTabOrder(self.button_quit, self.button_convert)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "M3U8 Converter"))
        self.label_find.setText(_translate("Dialog", "Find"))
        self.label_folder.setText(_translate("Dialog", "Folder"))
        self.label_replace.setText(_translate("Dialog", "Replace"))
        self.button_select.setText(_translate("Dialog", "Select"))
        self.button_convert.setText(_translate("Dialog", "Convert"))
        self.button_quit.setText(_translate("Dialog", "Quit"))
        self.checkBox_utf8.setText(_translate("Dialog", "utf8-mac to utf8"))
        self.checkBox_find_replace.setText(_translate("Dialog", "find and replace"))
        self.label_count.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#37e735;\">TextLabel </span></p></body></html>"))
import resources_rc
