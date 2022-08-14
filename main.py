# coding: utf-8
import fnmatch
import os
import shutil
import subprocess
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from main_ui import Ui_Dialog
from about_ui import Ui_About

# added find-replace history:
settings = QtCore.QSettings('m3u8-converter-settings')
print('Settings path:')
print(settings.fileName())


def countFiles(directory, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        count = 0
        for filename in fnmatch.filter(files, filePattern):
            print(filename)
            count += 1
        print('Found: '+str(count)+' m3us')
        return count


def create_folder(directory):
    path = directory + "/Converted"
    print(path)
    path = path.replace(' ', '\\ ')
    command = 'mkdir ' + path
    subprocess.call(command, shell=True)


def convert_utf8(directory):
    path_converted = directory + "/Converted"
    path_converted = path_converted.replace(' ', '\\ ')
    command = 'find . -name "*.m3u8" -exec bash -c \'iconv -f utf-8-mac -t utf-8 -c "{}" > ' + path_converted + '/''\"{}\"\' \\;'
    subprocess.call(command, shell=True, cwd=directory)


def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        print(path)
        print(files)
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            print(filepath)
            with open(filepath, 'r', encoding='utf-8') as f:
                s = f.read()
                f.close()
            s = s.replace(find, replace)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(s)
                f.close()


def copyFiles(source, destination):
    src_dir = source
    dest_dir = destination
    shutil.copytree(src_dir, dest_dir)


def convert(directory, find, replace, utf8_check, find_replace_check):
        
    if utf8_check is True and find_replace_check is True:
        create_folder(directory)
        convert_utf8(directory)
        findReplace(directory + "/Converted", find, replace, "*.m3u8")

    if utf8_check is True and find_replace_check is False:
        create_folder(directory)
        convert_utf8(directory)

    if find_replace_check is True and utf8_check is False:
        copyFiles(directory, directory + "/Converted")
        findReplace(directory + "/Converted", find, replace, "*.m3u8")


def check_appearance():
    """Checks DARK/LIGHT mode of macos."""
    cmd = 'defaults read -g AppleInterfaceStyle'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
    return bool(p.communicate()[0])


class About(QDialog):
    def __init__(self):
        super(About, self).__init__()
        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        qr.moveTop(300)
        self.move(qr.topLeft())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button_action = QAction("M3U8 Converter", self)
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        self.dialog = About()

        menu = self.menuBar()

        about_menu = menu.addMenu("About")
        about_menu.addAction(button_action)
        
        self.form_widget = Dialog() 
        self.setCentralWidget(self.form_widget)

        Dialog.setMinimumSize(self, 526, 216)
        Dialog.setMaximumSize(self, 526, 216)

        self.center()
        self.setWindowTitle('M3U8 Converter')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        qr.moveTop(300)
        self.move(qr.topLeft())

    def onMyToolBarButtonClick(self):
        self.dialog.show()


class Dialog(QDialog):

    convert_ok = False

    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setAcceptDrops(True)

        self.ui.label_count.setText('')  # clear text label

        # added find-replace history:
        find_start = settings.value("find")
        replace_start = settings.value("replace")
        self.ui.lineEdit_find.setText(find_start)
        self.ui.lineEdit_replace.setText(replace_start)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)
            result = f.endswith('/')
            if result is True:
                f = f[:-1]
                print(f)

            count = countFiles(f, "*.m3u8")

            if count != 0: 
                count = 'Found: '+str(count)+' m3u8 '
                self.convert_ok = True
            else:
                count = 'No m3u8 '
                self.convert_ok = False

            try:
                dark_mode = check_appearance()
                if dark_mode is True:
                    count = "<html><head/><body><p><span style=\" color:#37e735;\">" + count + "</span></p></body></html>"
            finally:
                self.ui.label_count.setText(count)
                self.ui.lineEdit_folder.setText(f)

    def select_button_clicked(self):
        dirName = QFileDialog.getExistingDirectory(self, "Select Directory")
        if dirName:
            print(dirName)
            self.ui.lineEdit_folder.setText(dirName)
            count = countFiles(dirName, "*.m3u8")

            if count != 0: 
                count = 'Found: '+str(count)+' m3u8 '
                self.convert_ok = True
            else:
                count = 'No m3u8 '
                self.convert_ok = False

            try:  
                dark_mode = check_appearance()
                if dark_mode is True:
                    count = "<html><head/><body><p><span style=\" color:#37e735;\">" + count + "</span></p></body></html>"
            finally:
                self.ui.label_count.setText(count)

    def quit_button_clicked(self):
        print('exit')
        sys.exit(app.exec_())

    def convert_button_clicked(self):
        directory = self.ui.lineEdit_folder.text()
        print(directory)

        find = self.ui.lineEdit_find.text()
        print(find)
        settings.setValue('find', find)  # added find-replace history

        replace = self.ui.lineEdit_replace.text()
        print(replace)
        settings.setValue('replace', replace)  # added find-replace history

        utf8_check = self.ui.checkBox_utf8.isChecked()
        print(utf8_check)

        find_replace_check = self.ui.checkBox_find_replace.isChecked()
        print(find_replace_check)

        if self.convert_ok is True:
            convert(directory, find, replace, utf8_check, find_replace_check)

    def utf8_checkbox(self):
        if self.ui.checkBox_utf8.isChecked():
            print('checked')
        else:
            print('unchecked')

    def find_replace_checkbox(self):
        if self.ui.checkBox_find_replace.isChecked():
            print('checked')
        else:
            print('unchecked')

    def line_folder(self):
        options = QFileDialog.Options()

    def line_find(self):
        options = QFileDialog.Options()

    def line_replace(self):
        options = QFileDialog.Options()

    def label_count(self):
        options = QFileDialog.Options()


if __name__ == '__main__':
    app = QApplication([])
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
