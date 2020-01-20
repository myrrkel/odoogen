# -*- coding: utf-8 -*-

import logging
import markdown
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from docgen.docgen import DocGen

from wordprocessor import *


logger = logging.getLogger(__name__)


class Ui_MainWindow(object):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(854, 541)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setAutoFillBackground(False)
        main_window.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.ForceTabbedDocks)
        self.centralWidget = QtWidgets.QWidget(main_window)
        self.centralWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.text_editor = wordprocessor.WordProcessor(main_window)
        self.gridLayout.addWidget(self.text_editor)
        
        # self.text_editor.setHtml("test <b>BIG</b>")
        # self.menuBar.addAction(self.menuTools.menuAction())

        container = QtWidgets.QWidget()
        container.setLayout(self.gridLayout)
        main_window.setCentralWidget(container)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.searchEdit.setPlaceholderText(_translate("MainWindow", "Search"))


class MainWindow(QMainWindow):

    # currentTrackChanged = pyqtSignal(str, name='currentTrackChanged')

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        doc_generator = DocGen()
        md_doc = doc_generator.get_all_markdown_docs(self.get_test_path())
        html_doc = markdown.markdown(md_doc)
        logger.info(html_doc)
        # self.ui.text_editor.editor.document().setMarkdown()
        self.ui.text_editor.editor.setHtml(html_doc)
        md_text = self.ui.text_editor.editor.getMarkdown()
        logger.info("Markdow Result: %s", md_text)


    def get_test_path(self):
        return os.path.join(os.path.dirname(__file__), 'test')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setStatusBar(main_window.ui.text_editor.status)
    main_window.show()
    sys.exit(app.exec_())

