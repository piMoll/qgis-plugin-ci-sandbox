import os.path

from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.uic import loadUiType


class OpenAbout(QDialog):

    def __init__(self, iface):
        main_window = iface.mainWindow() if iface is not None else None
        QDialog.__init__(self, main_window)

        Ui_DialogAbout, _ = loadUiType(
            os.path.join(os.path.dirname(__file__), "ui", "ui_about.ui")
        )
        self.ui = Ui_DialogAbout()
        self.ui.setupUi(self)
        self.iface = iface
