from PyQt5 import QtWidgets

from point_spectra_gui.future_.functions.BasicFunctionality import Basics
from point_spectra_gui.ui.MaskData import Ui_Form


class Ui_Form(Ui_Form, Basics):
    uiID = 0

    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        Ui_Form.uiID += 1

    def get_widget(self):
        return self.groupBox

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Mask Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def connectWidgets(self):
        super().connectWidgets()
        print(Ui_Form.uiID)
        self.pushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.maskFileLineEdit))

    def getGuiParams(self):
        return super().getGuiParams()
