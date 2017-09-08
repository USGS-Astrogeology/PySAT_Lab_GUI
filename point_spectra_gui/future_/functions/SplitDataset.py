import numpy as np
from spectral.spectral_data import spectral_data

from point_spectra_gui.future_.util.BasicFunctionality import Basics
from point_spectra_gui.ui.SplitDataset import Ui_Form


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataComboBox, self.datakeys)

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)

    def function(self):
        params = self.getGuiParams()
        datakey = params['chooseDataComboBox']
        colname = params['splitOnUniqueValuesOfComboBox']
        try:
            vars_level0 = self.data[datakey].df.columns.get_level_values(0)
            vars_level1 = self.data[datakey].df.columns.get_level_values(1)
            vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
            vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
            colname = (vars_level0[vars_level1.index(colname)], colname)

            coldata = np.array([str(i) for i in self.data[datakey].df[colname]])
            unique_values = np.unique(coldata)
            for i in unique_values:
                new_datakey = datakey + ' - ' + str(i)
                self.datakeys.append(new_datakey)
                self.data[new_datakey] = spectral_data(self.data[datakey].df.ix[coldata == i])
        except Exception as e:
            print(e)
