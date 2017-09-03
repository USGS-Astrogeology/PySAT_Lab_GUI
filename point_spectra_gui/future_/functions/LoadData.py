# from plio import io_ccam_pds
# from plio import io_ccam_pds
import pandas as pd
from PyQt5 import QtWidgets
from pysat.spectral.spectral_data import spectral_data

from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.LoadData import Ui_loadData
from point_spectra_gui.ui_modules.Error_ import error_print


class Ui_Form(Ui_loadData, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def connectWidgets(self):
        pass

        self.newFilePushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.fileNameLineEdit))

    def getGuiParams(self):
        return super().getGuiParams()

    def function(self):
        params = self.getGuiParams()
        filename = params['fileNameLineEdit']
        keyname = params['dataSetNameLineEdit']
        try:
            print('Loading data file: ' + str(filename))
            Basics.data[keyname] = spectral_data(pd.read_csv(filename, header=[0, 1]))
            Basics.datakeys.append(keyname)
        except Exception as e:
            error_print('Problem reading data: {}'.format(e))

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)
