# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.Normalization = QtWidgets.QVBoxLayout(self.groupBox)
        self.Normalization.setObjectName("Normalization")
        self.chooseDataFormLayout = QtWidgets.QFormLayout()
        self.chooseDataFormLayout.setObjectName("chooseDataFormLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.chooseDataFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chooseDataLabel)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.chooseDataFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chooseDataComboBox)
        self.Normalization.addLayout(self.chooseDataFormLayout)
        self.varToNormalizeVerticalLayout = QtWidgets.QVBoxLayout()
        self.varToNormalizeVerticalLayout.setObjectName("varToNormalizeVerticalLayout")
        self.varToNormalizeLabel = QtWidgets.QLabel(self.groupBox)
        self.varToNormalizeLabel.setObjectName("varToNormalizeLabel")
        self.varToNormalizeVerticalLayout.addWidget(self.varToNormalizeLabel)
        self.varToNormalizeListWidget = QtWidgets.QListWidget(self.groupBox)
        self.varToNormalizeListWidget.setObjectName("varToNormalizeListWidget")
        self.varToNormalizeVerticalLayout.addWidget(self.varToNormalizeListWidget)
        self.Normalization.addLayout(self.varToNormalizeVerticalLayout)
        self.waveLengthLayout = QtWidgets.QGridLayout()
        self.waveLengthLayout.setObjectName("waveLengthLayout")
        self.minimumWavelengthLabel = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel.setObjectName("minimumWavelengthLabel")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel, 0, 0, 1, 1)
        self.minimumWavelengthSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox.setObjectName("minimumWavelengthSpinBox")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox, 0, 1, 1, 1)
        self.maximumWavelengthLabel = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel.setObjectName("maximumWavelengthLabel")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel, 0, 2, 1, 1)
        self.maximumWavelengthSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox.setObjectName("maximumWavelengthSpinBox")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox, 0, 3, 1, 1)
        self.minimumWavelengthLabel_2 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_2.setObjectName("minimumWavelengthLabel_2")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_2, 1, 0, 1, 1)
        self.minimumWavelengthSpinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_2.setObjectName("minimumWavelengthSpinBox_2")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_2, 1, 1, 1, 1)
        self.maximumWavelengthLabel_2 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_2.setObjectName("maximumWavelengthLabel_2")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_2, 1, 2, 1, 1)
        self.maximumWavelengthSpinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_2.setObjectName("maximumWavelengthSpinBox_2")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_2, 1, 3, 1, 1)
        self.minimumWavelengthLabel_3 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_3.setObjectName("minimumWavelengthLabel_3")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_3, 2, 0, 1, 1)
        self.minimumWavelengthSpinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_3.setObjectName("minimumWavelengthSpinBox_3")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_3, 2, 1, 1, 1)
        self.maximumWavelengthLabel_3 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_3.setObjectName("maximumWavelengthLabel_3")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_3, 2, 2, 1, 1)
        self.maximumWavelengthSpinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_3.setObjectName("maximumWavelengthSpinBox_3")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_3, 2, 3, 1, 1)
        self.minimumWavelengthLabel_4 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_4.setObjectName("minimumWavelengthLabel_4")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_4, 3, 0, 1, 1)
        self.minimumWavelengthSpinBox_4 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_4.setObjectName("minimumWavelengthSpinBox_4")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_4, 3, 1, 1, 1)
        self.maximumWavelengthLabel_4 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_4.setObjectName("maximumWavelengthLabel_4")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_4, 3, 2, 1, 1)
        self.maximumWavelengthSpinBox_4 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_4.setObjectName("maximumWavelengthSpinBox_4")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_4, 3, 3, 1, 1)
        self.minimumWavelengthLabel_5 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_5.setObjectName("minimumWavelengthLabel_5")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_5, 4, 0, 1, 1)
        self.minimumWavelengthSpinBox_5 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_5.setObjectName("minimumWavelengthSpinBox_5")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_5, 4, 1, 1, 1)
        self.maximumWavelengthLabel_5 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_5.setObjectName("maximumWavelengthLabel_5")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_5, 4, 2, 1, 1)
        self.maximumWavelengthSpinBox_5 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_5.setObjectName("maximumWavelengthSpinBox_5")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_5, 4, 3, 1, 1)
        self.minimumWavelengthLabel_6 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_6.setObjectName("minimumWavelengthLabel_6")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_6, 5, 0, 1, 1)
        self.minimumWavelengthSpinBox_6 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_6.setObjectName("minimumWavelengthSpinBox_6")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_6, 5, 1, 1, 1)
        self.maximumWavelengthLabel_6 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_6.setObjectName("maximumWavelengthLabel_6")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_6, 5, 2, 1, 1)
        self.maximumWavelengthSpinBox_6 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_6.setObjectName("maximumWavelengthSpinBox_6")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_6, 5, 3, 1, 1)
        self.minimumWavelengthLabel_7 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_7.setObjectName("minimumWavelengthLabel_7")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_7, 6, 0, 1, 1)
        self.minimumWavelengthSpinBox_7 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_7.setObjectName("minimumWavelengthSpinBox_7")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_7, 6, 1, 1, 1)
        self.maximumWavelengthLabel_7 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_7.setObjectName("maximumWavelengthLabel_7")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_7, 6, 2, 1, 1)
        self.maximumWavelengthSpinBox_7 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_7.setObjectName("maximumWavelengthSpinBox_7")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_7, 6, 3, 1, 1)
        self.minimumWavelengthLabel_8 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_8.setObjectName("minimumWavelengthLabel_8")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_8, 7, 0, 1, 1)
        self.minimumWavelengthSpinBox_8 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_8.setObjectName("minimumWavelengthSpinBox_8")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_8, 7, 1, 1, 1)
        self.maximumWavelengthLabel_8 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_8.setObjectName("maximumWavelengthLabel_8")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_8, 7, 2, 1, 1)
        self.maximumWavelengthSpinBox_8 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_8.setObjectName("maximumWavelengthSpinBox_8")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_8, 7, 3, 1, 1)
        self.minimumWavelengthLabel_9 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_9.setObjectName("minimumWavelengthLabel_9")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_9, 8, 0, 1, 1)
        self.minimumWavelengthSpinBox_9 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_9.setObjectName("minimumWavelengthSpinBox_9")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_9, 8, 1, 1, 1)
        self.maximumWavelengthLabel_9 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_9.setObjectName("maximumWavelengthLabel_9")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_9, 8, 2, 1, 1)
        self.maximumWavelengthSpinBox_9 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_9.setObjectName("maximumWavelengthSpinBox_9")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_9, 8, 3, 1, 1)
        self.minimumWavelengthLabel_10 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_10.setObjectName("minimumWavelengthLabel_10")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_10, 9, 0, 1, 1)
        self.minimumWavelengthSpinBox_10 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_10.setObjectName("minimumWavelengthSpinBox_10")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_10, 9, 1, 1, 1)
        self.maximumWavelengthLabel_10 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_10.setObjectName("maximumWavelengthLabel_10")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_10, 9, 2, 1, 1)
        self.maximumWavelengthSpinBox_10 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_10.setObjectName("maximumWavelengthSpinBox_10")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_10, 9, 3, 1, 1)
        self.minimumWavelengthLabel_11 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_11.setObjectName("minimumWavelengthLabel_11")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_11, 10, 0, 1, 1)
        self.minimumWavelengthSpinBox_11 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_11.setObjectName("minimumWavelengthSpinBox_11")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_11, 10, 1, 1, 1)
        self.maximumWavelengthLabel_11 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_11.setObjectName("maximumWavelengthLabel_11")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_11, 10, 2, 1, 1)
        self.maximumWavelengthSpinBox_11 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_11.setObjectName("maximumWavelengthSpinBox_11")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_11, 10, 3, 1, 1)
        self.minimumWavelengthLabel_12 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_12.setObjectName("minimumWavelengthLabel_12")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_12, 11, 0, 1, 1)
        self.minimumWavelengthSpinBox_12 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_12.setObjectName("minimumWavelengthSpinBox_12")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_12, 11, 1, 1, 1)
        self.maximumWavelengthLabel_12 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_12.setObjectName("maximumWavelengthLabel_12")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_12, 11, 2, 1, 1)
        self.maximumWavelengthSpinBox_12 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_12.setObjectName("maximumWavelengthSpinBox_12")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_12, 11, 3, 1, 1)
        self.minimumWavelengthLabel_13 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_13.setObjectName("minimumWavelengthLabel_13")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_13, 12, 0, 1, 1)
        self.minimumWavelengthSpinBox_13 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_13.setObjectName("minimumWavelengthSpinBox_13")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_13, 12, 1, 1, 1)
        self.maximumWavelengthLabel_13 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_13.setObjectName("maximumWavelengthLabel_13")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_13, 12, 2, 1, 1)
        self.maximumWavelengthSpinBox_13 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_13.setObjectName("maximumWavelengthSpinBox_13")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_13, 12, 3, 1, 1)
        self.minimumWavelengthLabel_14 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_14.setObjectName("minimumWavelengthLabel_14")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_14, 13, 0, 1, 1)
        self.minimumWavelengthSpinBox_14 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_14.setObjectName("minimumWavelengthSpinBox_14")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_14, 13, 1, 1, 1)
        self.maximumWavelengthLabel_14 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_14.setObjectName("maximumWavelengthLabel_14")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_14, 13, 2, 1, 1)
        self.maximumWavelengthSpinBox_14 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_14.setObjectName("maximumWavelengthSpinBox_14")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_14, 13, 3, 1, 1)
        self.minimumWavelengthLabel_15 = QtWidgets.QLabel(self.groupBox)
        self.minimumWavelengthLabel_15.setObjectName("minimumWavelengthLabel_15")
        self.waveLengthLayout.addWidget(self.minimumWavelengthLabel_15, 14, 0, 1, 1)
        self.minimumWavelengthSpinBox_15 = QtWidgets.QSpinBox(self.groupBox)
        self.minimumWavelengthSpinBox_15.setObjectName("minimumWavelengthSpinBox_15")
        self.waveLengthLayout.addWidget(self.minimumWavelengthSpinBox_15, 14, 1, 1, 1)
        self.maximumWavelengthLabel_15 = QtWidgets.QLabel(self.groupBox)
        self.maximumWavelengthLabel_15.setObjectName("maximumWavelengthLabel_15")
        self.waveLengthLayout.addWidget(self.maximumWavelengthLabel_15, 14, 2, 1, 1)
        self.maximumWavelengthSpinBox_15 = QtWidgets.QSpinBox(self.groupBox)
        self.maximumWavelengthSpinBox_15.setObjectName("maximumWavelengthSpinBox_15")
        self.waveLengthLayout.addWidget(self.maximumWavelengthSpinBox_15, 14, 3, 1, 1)
        self.Normalization.addLayout(self.waveLengthLayout)
        self.addDelRangeLayout = QtWidgets.QHBoxLayout()
        self.addDelRangeLayout.setObjectName("addDelRangeLayout")
        self.addRangePushButton = QtWidgets.QPushButton(self.groupBox)
        self.addRangePushButton.setObjectName("addRangePushButton")
        self.addDelRangeLayout.addWidget(self.addRangePushButton)
        self.deleteRangePushButton = QtWidgets.QPushButton(self.groupBox)
        self.deleteRangePushButton.setObjectName("deleteRangePushButton")
        self.addDelRangeLayout.addWidget(self.deleteRangePushButton)
        self.Normalization.addLayout(self.addDelRangeLayout)
        self.verticalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Normalization"))
        self.chooseDataLabel.setText(_("Choose data"))
        self.varToNormalizeLabel.setText(_("Variable to normalize"))
        self.minimumWavelengthLabel.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_2.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_2.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_3.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_3.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_4.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_4.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_5.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_5.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_6.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_6.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_7.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_7.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_8.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_8.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_9.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_9.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_10.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_10.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_11.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_11.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_12.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_12.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_13.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_13.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_14.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_14.setText(_("Maximum wavelength"))
        self.minimumWavelengthLabel_15.setText(_("Minimum wavelength"))
        self.maximumWavelengthLabel_15.setText(_("Maximum wavelength"))
        self.addRangePushButton.setText(_("Add Range"))
        self.deleteRangePushButton.setText(_("Delete Range"))

