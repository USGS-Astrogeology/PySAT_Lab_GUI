# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\point_spectra_gui\ui\ui\UI_SubmodelPredict.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(545, 556)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupbox = QtWidgets.QGroupBox(Form)
        self.groupbox.setObjectName("groupbox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.referenceModelLabel = QtWidgets.QLabel(self.groupbox)
        self.referenceModelLabel.setObjectName("referenceModelLabel")
        self.gridLayout.addWidget(self.referenceModelLabel, 0, 0, 1, 1)
        self.referenceModelComboBox = QtWidgets.QComboBox(self.groupbox)
        self.referenceModelComboBox.setObjectName("referenceModelComboBox")
        self.gridLayout.addWidget(self.referenceModelComboBox, 0, 1, 1, 1)
        self.lowModelLabel = QtWidgets.QLabel(self.groupbox)
        self.lowModelLabel.setObjectName("lowModelLabel")
        self.gridLayout.addWidget(self.lowModelLabel, 1, 0, 1, 1)
        self.lowModelComboBox = QtWidgets.QComboBox(self.groupbox)
        self.lowModelComboBox.setObjectName("lowModelComboBox")
        self.gridLayout.addWidget(self.lowModelComboBox, 1, 1, 1, 1)
        self.lowModelMaxLabel = QtWidgets.QLabel(self.groupbox)
        self.lowModelMaxLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lowModelMaxLabel.setObjectName("lowModelMaxLabel")
        self.gridLayout.addWidget(self.lowModelMaxLabel, 1, 2, 1, 1)
        self.lowModelMaxSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.lowModelMaxSpinBox.setMinimumSize(QtCore.QSize(130, 0))
        self.lowModelMaxSpinBox.setMaximumSize(QtCore.QSize(910, 16777215))
        self.lowModelMaxSpinBox.setObjectName("lowModelMaxSpinBox")
        self.gridLayout.addWidget(self.lowModelMaxSpinBox, 1, 3, 1, 1)
        self.modelComboBox = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox.setObjectName("modelComboBox")
        self.gridLayout.addWidget(self.modelComboBox, 2, 1, 1, 1)
        self.minLabel = QtWidgets.QLabel(self.groupbox)
        self.minLabel.setObjectName("minLabel")
        self.gridLayout.addWidget(self.minLabel, 2, 2, 1, 1)
        self.minSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox.setObjectName("minSpinBox")
        self.gridLayout.addWidget(self.minSpinBox, 2, 3, 1, 1)
        self.maxLabel = QtWidgets.QLabel(self.groupbox)
        self.maxLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.maxLabel.setObjectName("maxLabel")
        self.gridLayout.addWidget(self.maxLabel, 2, 4, 1, 1)
        self.maxSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox.setObjectName("maxSpinBox")
        self.gridLayout.addWidget(self.maxSpinBox, 2, 5, 1, 1)
        self.modelComboBox_2 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_2.setObjectName("modelComboBox_2")
        self.gridLayout.addWidget(self.modelComboBox_2, 3, 1, 1, 1)
        self.minLabel_2 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_2.setObjectName("minLabel_2")
        self.gridLayout.addWidget(self.minLabel_2, 3, 2, 1, 1)
        self.minSpinBox_2 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_2.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_2.setObjectName("minSpinBox_2")
        self.gridLayout.addWidget(self.minSpinBox_2, 3, 3, 1, 1)
        self.maxLabel_2 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_2.setObjectName("maxLabel_2")
        self.gridLayout.addWidget(self.maxLabel_2, 3, 4, 1, 1)
        self.maxSpinBox_2 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_2.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_2.setObjectName("maxSpinBox_2")
        self.gridLayout.addWidget(self.maxSpinBox_2, 3, 5, 1, 1)
        self.modelComboBox_3 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_3.setObjectName("modelComboBox_3")
        self.gridLayout.addWidget(self.modelComboBox_3, 4, 1, 1, 1)
        self.minLabel_3 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_3.setObjectName("minLabel_3")
        self.gridLayout.addWidget(self.minLabel_3, 4, 2, 1, 1)
        self.minSpinBox_3 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_3.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_3.setObjectName("minSpinBox_3")
        self.gridLayout.addWidget(self.minSpinBox_3, 4, 3, 1, 1)
        self.maxLabel_3 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_3.setObjectName("maxLabel_3")
        self.gridLayout.addWidget(self.maxLabel_3, 4, 4, 1, 1)
        self.maxSpinBox_3 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_3.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_3.setObjectName("maxSpinBox_3")
        self.gridLayout.addWidget(self.maxSpinBox_3, 4, 5, 1, 1)
        self.modelComboBox_4 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_4.setObjectName("modelComboBox_4")
        self.gridLayout.addWidget(self.modelComboBox_4, 5, 1, 1, 1)
        self.minLabel_4 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_4.setObjectName("minLabel_4")
        self.gridLayout.addWidget(self.minLabel_4, 5, 2, 1, 1)
        self.minSpinBox_4 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_4.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_4.setObjectName("minSpinBox_4")
        self.gridLayout.addWidget(self.minSpinBox_4, 5, 3, 1, 1)
        self.maxLabel_4 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_4.setObjectName("maxLabel_4")
        self.gridLayout.addWidget(self.maxLabel_4, 5, 4, 1, 1)
        self.maxSpinBox_4 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_4.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_4.setObjectName("maxSpinBox_4")
        self.gridLayout.addWidget(self.maxSpinBox_4, 5, 5, 1, 1)
        self.modelComboBox_5 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_5.setObjectName("modelComboBox_5")
        self.gridLayout.addWidget(self.modelComboBox_5, 6, 1, 1, 1)
        self.minLabel_5 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_5.setObjectName("minLabel_5")
        self.gridLayout.addWidget(self.minLabel_5, 6, 2, 1, 1)
        self.minSpinBox_5 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_5.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_5.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_5.setObjectName("minSpinBox_5")
        self.gridLayout.addWidget(self.minSpinBox_5, 6, 3, 1, 1)
        self.maxLabel_5 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_5.setObjectName("maxLabel_5")
        self.gridLayout.addWidget(self.maxLabel_5, 6, 4, 1, 1)
        self.maxSpinBox_5 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_5.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_5.setObjectName("maxSpinBox_5")
        self.gridLayout.addWidget(self.maxSpinBox_5, 6, 5, 1, 1)
        self.modelComboBox_6 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_6.setObjectName("modelComboBox_6")
        self.gridLayout.addWidget(self.modelComboBox_6, 7, 1, 1, 1)
        self.minLabel_6 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_6.setObjectName("minLabel_6")
        self.gridLayout.addWidget(self.minLabel_6, 7, 2, 1, 1)
        self.minSpinBox_6 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_6.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_6.setObjectName("minSpinBox_6")
        self.gridLayout.addWidget(self.minSpinBox_6, 7, 3, 1, 1)
        self.maxLabel_6 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_6.setObjectName("maxLabel_6")
        self.gridLayout.addWidget(self.maxLabel_6, 7, 4, 1, 1)
        self.maxSpinBox_6 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_6.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_6.setObjectName("maxSpinBox_6")
        self.gridLayout.addWidget(self.maxSpinBox_6, 7, 5, 1, 1)
        self.modelComboBox_7 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_7.setObjectName("modelComboBox_7")
        self.gridLayout.addWidget(self.modelComboBox_7, 8, 1, 1, 1)
        self.minLabel_7 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_7.setObjectName("minLabel_7")
        self.gridLayout.addWidget(self.minLabel_7, 8, 2, 1, 1)
        self.minSpinBox_7 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_7.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_7.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_7.setObjectName("minSpinBox_7")
        self.gridLayout.addWidget(self.minSpinBox_7, 8, 3, 1, 1)
        self.maxLabel_7 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_7.setObjectName("maxLabel_7")
        self.gridLayout.addWidget(self.maxLabel_7, 8, 4, 1, 1)
        self.maxSpinBox_7 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_7.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_7.setObjectName("maxSpinBox_7")
        self.gridLayout.addWidget(self.maxSpinBox_7, 8, 5, 1, 1)
        self.modelComboBox_8 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_8.setObjectName("modelComboBox_8")
        self.gridLayout.addWidget(self.modelComboBox_8, 9, 1, 1, 1)
        self.minLabel_8 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_8.setObjectName("minLabel_8")
        self.gridLayout.addWidget(self.minLabel_8, 9, 2, 1, 1)
        self.minSpinBox_8 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_8.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_8.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_8.setObjectName("minSpinBox_8")
        self.gridLayout.addWidget(self.minSpinBox_8, 9, 3, 1, 1)
        self.maxLabel_8 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_8.setObjectName("maxLabel_8")
        self.gridLayout.addWidget(self.maxLabel_8, 9, 4, 1, 1)
        self.maxSpinBox_8 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_8.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_8.setObjectName("maxSpinBox_8")
        self.gridLayout.addWidget(self.maxSpinBox_8, 9, 5, 1, 1)
        self.modelComboBox_9 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_9.setObjectName("modelComboBox_9")
        self.gridLayout.addWidget(self.modelComboBox_9, 10, 1, 1, 1)
        self.minLabel_9 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_9.setObjectName("minLabel_9")
        self.gridLayout.addWidget(self.minLabel_9, 10, 2, 1, 1)
        self.minSpinBox_9 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_9.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_9.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_9.setObjectName("minSpinBox_9")
        self.gridLayout.addWidget(self.minSpinBox_9, 10, 3, 1, 1)
        self.maxLabel_9 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_9.setObjectName("maxLabel_9")
        self.gridLayout.addWidget(self.maxLabel_9, 10, 4, 1, 1)
        self.maxSpinBox_9 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_9.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_9.setObjectName("maxSpinBox_9")
        self.gridLayout.addWidget(self.maxSpinBox_9, 10, 5, 1, 1)
        self.modelComboBox_10 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_10.setObjectName("modelComboBox_10")
        self.gridLayout.addWidget(self.modelComboBox_10, 11, 1, 1, 1)
        self.minLabel_10 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_10.setObjectName("minLabel_10")
        self.gridLayout.addWidget(self.minLabel_10, 11, 2, 1, 1)
        self.minSpinBox_10 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_10.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_10.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_10.setObjectName("minSpinBox_10")
        self.gridLayout.addWidget(self.minSpinBox_10, 11, 3, 1, 1)
        self.maxLabel_10 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_10.setObjectName("maxLabel_10")
        self.gridLayout.addWidget(self.maxLabel_10, 11, 4, 1, 1)
        self.maxSpinBox_10 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_10.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_10.setObjectName("maxSpinBox_10")
        self.gridLayout.addWidget(self.maxSpinBox_10, 11, 5, 1, 1)
        self.modelComboBox_11 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_11.setObjectName("modelComboBox_11")
        self.gridLayout.addWidget(self.modelComboBox_11, 12, 1, 1, 1)
        self.minLabel_11 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_11.setObjectName("minLabel_11")
        self.gridLayout.addWidget(self.minLabel_11, 12, 2, 1, 1)
        self.minSpinBox_11 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_11.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_11.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_11.setObjectName("minSpinBox_11")
        self.gridLayout.addWidget(self.minSpinBox_11, 12, 3, 1, 1)
        self.maxLabel_11 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_11.setObjectName("maxLabel_11")
        self.gridLayout.addWidget(self.maxLabel_11, 12, 4, 1, 1)
        self.maxSpinBox_11 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_11.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_11.setObjectName("maxSpinBox_11")
        self.gridLayout.addWidget(self.maxSpinBox_11, 12, 5, 1, 1)
        self.modelComboBox_12 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_12.setObjectName("modelComboBox_12")
        self.gridLayout.addWidget(self.modelComboBox_12, 13, 1, 1, 1)
        self.minLabel_12 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_12.setObjectName("minLabel_12")
        self.gridLayout.addWidget(self.minLabel_12, 13, 2, 1, 1)
        self.minSpinBox_12 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_12.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_12.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_12.setObjectName("minSpinBox_12")
        self.gridLayout.addWidget(self.minSpinBox_12, 13, 3, 1, 1)
        self.maxLabel_12 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_12.setObjectName("maxLabel_12")
        self.gridLayout.addWidget(self.maxLabel_12, 13, 4, 1, 1)
        self.maxSpinBox_12 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_12.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_12.setObjectName("maxSpinBox_12")
        self.gridLayout.addWidget(self.maxSpinBox_12, 13, 5, 1, 1)
        self.modelComboBox_13 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_13.setObjectName("modelComboBox_13")
        self.gridLayout.addWidget(self.modelComboBox_13, 14, 1, 1, 1)
        self.minLabel_13 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_13.setObjectName("minLabel_13")
        self.gridLayout.addWidget(self.minLabel_13, 14, 2, 1, 1)
        self.minSpinBox_13 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_13.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_13.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_13.setObjectName("minSpinBox_13")
        self.gridLayout.addWidget(self.minSpinBox_13, 14, 3, 1, 1)
        self.maxLabel_13 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_13.setObjectName("maxLabel_13")
        self.gridLayout.addWidget(self.maxLabel_13, 14, 4, 1, 1)
        self.maxSpinBox_13 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_13.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_13.setObjectName("maxSpinBox_13")
        self.gridLayout.addWidget(self.maxSpinBox_13, 14, 5, 1, 1)
        self.modelComboBox_14 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_14.setObjectName("modelComboBox_14")
        self.gridLayout.addWidget(self.modelComboBox_14, 15, 1, 1, 1)
        self.minLabel_14 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_14.setObjectName("minLabel_14")
        self.gridLayout.addWidget(self.minLabel_14, 15, 2, 1, 1)
        self.minSpinBox_14 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_14.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_14.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_14.setObjectName("minSpinBox_14")
        self.gridLayout.addWidget(self.minSpinBox_14, 15, 3, 1, 1)
        self.maxLabel_14 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_14.setObjectName("maxLabel_14")
        self.gridLayout.addWidget(self.maxLabel_14, 15, 4, 1, 1)
        self.maxSpinBox_14 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_14.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_14.setObjectName("maxSpinBox_14")
        self.gridLayout.addWidget(self.maxSpinBox_14, 15, 5, 1, 1)
        self.modelComboBox_15 = QtWidgets.QComboBox(self.groupbox)
        self.modelComboBox_15.setObjectName("modelComboBox_15")
        self.gridLayout.addWidget(self.modelComboBox_15, 16, 1, 1, 1)
        self.minLabel_15 = QtWidgets.QLabel(self.groupbox)
        self.minLabel_15.setObjectName("minLabel_15")
        self.gridLayout.addWidget(self.minLabel_15, 16, 2, 1, 1)
        self.minSpinBox_15 = QtWidgets.QSpinBox(self.groupbox)
        self.minSpinBox_15.setMinimumSize(QtCore.QSize(130, 0))
        self.minSpinBox_15.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox_15.setObjectName("minSpinBox_15")
        self.gridLayout.addWidget(self.minSpinBox_15, 16, 3, 1, 1)
        self.maxLabel_15 = QtWidgets.QLabel(self.groupbox)
        self.maxLabel_15.setObjectName("maxLabel_15")
        self.gridLayout.addWidget(self.maxLabel_15, 16, 4, 1, 1)
        self.maxSpinBox_15 = QtWidgets.QSpinBox(self.groupbox)
        self.maxSpinBox_15.setMinimumSize(QtCore.QSize(130, 0))
        self.maxSpinBox_15.setObjectName("maxSpinBox_15")
        self.gridLayout.addWidget(self.maxSpinBox_15, 16, 5, 1, 1)
        self.highModelLabel = QtWidgets.QLabel(self.groupbox)
        self.highModelLabel.setObjectName("highModelLabel")
        self.gridLayout.addWidget(self.highModelLabel, 17, 0, 1, 1)
        self.lowModelComboBox_2 = QtWidgets.QComboBox(self.groupbox)
        self.lowModelComboBox_2.setObjectName("lowModelComboBox_2")
        self.gridLayout.addWidget(self.lowModelComboBox_2, 17, 1, 1, 1)
        self.highModelMinLabel = QtWidgets.QLabel(self.groupbox)
        self.highModelMinLabel.setObjectName("highModelMinLabel")
        self.gridLayout.addWidget(self.highModelMinLabel, 17, 2, 1, 1)
        self.highModelMaxSpinBox = QtWidgets.QSpinBox(self.groupbox)
        self.highModelMaxSpinBox.setMinimumSize(QtCore.QSize(130, 0))
        self.highModelMaxSpinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.highModelMaxSpinBox.setObjectName("highModelMaxSpinBox")
        self.gridLayout.addWidget(self.highModelMaxSpinBox, 17, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupbox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupbox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.checkBox = QtWidgets.QCheckBox(self.groupbox)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout, 18, 0, 1, 6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupbox)
        self.chooseDataLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.horizontalLayout_2.addWidget(self.chooseDataLabel)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupbox)
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.horizontalLayout_2.addWidget(self.chooseDataComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 19, 0, 1, 6)
        self.verticalLayout_2.addWidget(self.groupbox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupbox.setTitle(_translate("Form", "Submodel - Predict"))
        self.referenceModelLabel.setText(_translate("Form", "Choose reference model: "))
        self.lowModelLabel.setText(_translate("Form", "Low Model"))
        self.lowModelMaxLabel.setText(_translate("Form", "Max"))
        self.minLabel.setText(_translate("Form", "Min"))
        self.maxLabel.setText(_translate("Form", "Max"))
        self.minLabel_2.setText(_translate("Form", "Min"))
        self.maxLabel_2.setText(_translate("Form", "Max"))
        self.minLabel_3.setText(_translate("Form", "Min"))
        self.maxLabel_3.setText(_translate("Form", "Max"))
        self.minLabel_4.setText(_translate("Form", "Min"))
        self.maxLabel_4.setText(_translate("Form", "Max"))
        self.minLabel_5.setText(_translate("Form", "Min"))
        self.maxLabel_5.setText(_translate("Form", "Max"))
        self.minLabel_6.setText(_translate("Form", "Min"))
        self.maxLabel_6.setText(_translate("Form", "Max"))
        self.minLabel_7.setText(_translate("Form", "Min"))
        self.maxLabel_7.setText(_translate("Form", "Max"))
        self.minLabel_8.setText(_translate("Form", "Min"))
        self.maxLabel_8.setText(_translate("Form", "Max"))
        self.minLabel_9.setText(_translate("Form", "Min"))
        self.maxLabel_9.setText(_translate("Form", "Max"))
        self.minLabel_10.setText(_translate("Form", "Min"))
        self.maxLabel_10.setText(_translate("Form", "Max"))
        self.minLabel_11.setText(_translate("Form", "Min"))
        self.maxLabel_11.setText(_translate("Form", "Max"))
        self.minLabel_12.setText(_translate("Form", "Min"))
        self.maxLabel_12.setText(_translate("Form", "Max"))
        self.minLabel_13.setText(_translate("Form", "Min"))
        self.maxLabel_13.setText(_translate("Form", "Max"))
        self.minLabel_14.setText(_translate("Form", "Min"))
        self.maxLabel_14.setText(_translate("Form", "Max"))
        self.minLabel_15.setText(_translate("Form", "Min"))
        self.maxLabel_15.setText(_translate("Form", "Max"))
        self.highModelLabel.setText(_translate("Form", "High Model"))
        self.highModelMinLabel.setText(_translate("Form", "Min"))
        self.pushButton.setText(_translate("Form", "Add submodel"))
        self.pushButton_2.setText(_translate("Form", "Delete submodel"))
        self.checkBox.setText(_translate("Form", "Optimize "))
        self.chooseDataLabel.setText(_translate("Form", "Choose data to predict"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

