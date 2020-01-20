#!/usr/bin/env python3translation
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5 import QtCore


class translators():

    def __init__(self,app):
        self.app = app
        self.installed_translators = []

    def install_translator(self,filename,locale):
        translator = QtCore.QTranslator(self.app)
        app_dir = os.path.realpath(sys.argv[0])
        translator.load(app_dir+'/translation/{0}_{1}.qm'.format(filename,locale))
        self.installed_translators.append(translator)
        self.app.installTranslator(translator)

    def uninstall_translators(self):
        for translator in self.installed_translators:
            self.app.removeTranslator(translator)
        self.installed_translators = []

    def install_translators(self,locale):
        self.install_translator("widgets",locale)
