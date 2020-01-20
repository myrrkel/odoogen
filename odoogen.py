#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging

from darkStyle.darkStyle import darkStyle
from translators import *
from main_window import * 

root_logger = logging.getLogger()
root_logger.setLevel("INFO")
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root_logger.addHandler(handler)
logger = logging.getLogger(__name__)

def main():
    app = QtWidgets.QApplication(sys.argv)

    tr = translators(app)      
    locale_language = QtCore.QLocale.system().name()
    tr.install_translators(locale_language)

    #Load & Set the DarkStyleSheet
    app.setStyleSheet(darkStyle.load_stylesheet_pyqt5())


    main_window = MainWindow()
    # ui = Ui_MainWindow()

    # ui.setupUi(main_window)
    # main_window.setStatusBar(ui.text_editor.status)



    # main_window.ui.text_editor.editor.setHtml("test <b>BIG</b>")
    main_window.show()

    app.exec()
    sys.exit()


if __name__ == "__main__":
    main()

