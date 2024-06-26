#-----------------------------------------------------------
# Copyright (C) 2015 Martin Dobias
#-----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#---------------------------------------------------------------------

from pathlib import Path

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMessageBox

from .test_plugin_dialogs import OpenAbout


class TestPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        icons_path = Path(__file__).parent / "icons"
        
        self.action = QAction(QIcon(str(icons_path / "icon1.svg")), 'About', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action
        self.dialog = None

    def run(self):
        self.dialog = OpenAbout(self.iface)
        self.dialog.show()

