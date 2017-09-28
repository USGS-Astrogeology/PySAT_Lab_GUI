# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rbanderson\Documents\Projects\LIBS PDART\PySAT_Point_Spectra_GUI\point_spectra_gui\ui\\UI Files\blank.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 658)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regression = QtWidgets.QGroupBox(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.regression.setFont(font)
        self.regression.setObjectName("regression")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.regression)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.regression_choosedata_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosedata_hlayout.setContentsMargins(11, 11, 11, 11)
        self.regression_choosedata_hlayout.setSpacing(6)
        self.regression_choosedata_hlayout.setObjectName("regression_choosedata_hlayout")
        self.regression_choosedata_label = QtWidgets.QLabel(self.regression)
        self.regression_choosedata_label.setObjectName("regression_choosedata_label")
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata_label)
        self.regression_choosedata = QtWidgets.QComboBox(self.regression)
        self.regression_choosedata.setIconSize(QtCore.QSize(50, 20))
        self.regression_choosedata.setObjectName("regression_choosedata")
        self.regression_choosedata.addItem("")
        self.regression_choosedata.addItem("")
        self.regression_choosedata_hlayout.addWidget(self.regression_choosedata)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.regression_choosedata_hlayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.regression_choosedata_hlayout)
        self.regression_choosevars_hlayout = QtWidgets.QHBoxLayout()
        self.regression_choosevars_hlayout.setContentsMargins(11, 11, 11, 11)
        self.regression_choosevars_hlayout.setSpacing(6)
        self.regression_choosevars_hlayout.setObjectName("regression_choosevars_hlayout")
        self.regression_choosex_vlayout = QtWidgets.QVBoxLayout()
        self.regression_choosex_vlayout.setContentsMargins(11, 11, 11, 11)
        self.regression_choosex_vlayout.setSpacing(6)
        self.regression_choosex_vlayout.setObjectName("regression_choosex_vlayout")
        self.regression_choosex_label = QtWidgets.QLabel(self.regression)
        self.regression_choosex_label.setObjectName("regression_choosex_label")
        self.regression_choosex_vlayout.addWidget(self.regression_choosex_label)
        self.regression_choosex = QtWidgets.QListWidget(self.regression)
        self.regression_choosex.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regression_choosex.sizePolicy().hasHeightForWidth())
        self.regression_choosex.setSizePolicy(sizePolicy)
        self.regression_choosex.setMinimumSize(QtCore.QSize(0, 0))
        self.regression_choosex.setMaximumSize(QtCore.QSize(900, 16777215))
        self.regression_choosex.setObjectName("regression_choosex")
        item = QtWidgets.QListWidgetItem()
        self.regression_choosex.addItem(item)
        self.regression_choosex_vlayout.addWidget(self.regression_choosex)
        self.regression_choosevars_hlayout.addLayout(self.regression_choosex_vlayout)
        self.regression_choosey_vlayout = QtWidgets.QVBoxLayout()
        self.regression_choosey_vlayout.setContentsMargins(11, 11, 11, 11)
        self.regression_choosey_vlayout.setSpacing(6)
        self.regression_choosey_vlayout.setObjectName("regression_choosey_vlayout")
        self.regression_choosey_label = QtWidgets.QLabel(self.regression)
        self.regression_choosey_label.setObjectName("regression_choosey_label")
        self.regression_choosey_vlayout.addWidget(self.regression_choosey_label)
        self.regression_choosey = QtWidgets.QListWidget(self.regression)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regression_choosey.sizePolicy().hasHeightForWidth())
        self.regression_choosey.setSizePolicy(sizePolicy)
        self.regression_choosey.setMinimumSize(QtCore.QSize(0, 0))
        self.regression_choosey.setMaximumSize(QtCore.QSize(900, 16777215))
        self.regression_choosey.setObjectName("regression_choosey")
        item = QtWidgets.QListWidgetItem()
        self.regression_choosey.addItem(item)
        self.regression_choosey_vlayout.addWidget(self.regression_choosey)
        self.regression_choosevars_hlayout.addLayout(self.regression_choosey_vlayout)
        self.verticalLayout_2.addLayout(self.regression_choosevars_hlayout)
        self.min_max_layout = QtWidgets.QHBoxLayout()
        self.min_max_layout.setContentsMargins(11, 11, 11, 11)
        self.min_max_layout.setSpacing(6)
        self.min_max_layout.setObjectName("min_max_layout")
        self.min_label = QtWidgets.QLabel(self.regression)
        self.min_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.min_label.setObjectName("min_label")
        self.min_max_layout.addWidget(self.min_label)
        self.yvarmin_spin = QtWidgets.QDoubleSpinBox(self.regression)
        self.yvarmin_spin.setMaximum(9999999.0)
        self.yvarmin_spin.setObjectName("yvarmin_spin")
        self.min_max_layout.addWidget(self.yvarmin_spin)
        self.max_label = QtWidgets.QLabel(self.regression)
        self.max_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.max_label.setObjectName("max_label")
        self.min_max_layout.addWidget(self.max_label)
        self.yvarmax_spin = QtWidgets.QDoubleSpinBox(self.regression)
        self.yvarmax_spin.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.yvarmax_spin.setDecimals(2)
        self.yvarmax_spin.setMinimum(0.0)
        self.yvarmax_spin.setMaximum(9999999.0)
        self.yvarmax_spin.setProperty("value", 100.0)
        self.yvarmax_spin.setObjectName("yvarmax_spin")
        self.min_max_layout.addWidget(self.yvarmax_spin)
        self.verticalLayout_2.addLayout(self.min_max_layout)
        self.regression_alg_choices = QtWidgets.QComboBox(self.regression)
        self.regression_alg_choices.setMinimumSize(QtCore.QSize(250, 0))
        self.regression_alg_choices.setIconSize(QtCore.QSize(50, 20))
        self.regression_alg_choices.setObjectName("regression_alg_choices")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.regression_alg_choices.addItem("")
        self.verticalLayout_2.addWidget(self.regression_alg_choices)
        self.verticalLayout.addWidget(self.regression)
        MainWindow.setCentralWidget(self.centralWidget)
        self.actionLoad_Refence_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Refence_Data.setObjectName("actionLoad_Refence_Data")
        self.actionLoad_Unknown_Data = QtWidgets.QAction(MainWindow)
        self.actionLoad_Unknown_Data.setObjectName("actionLoad_Unknown_Data")
        self.actionSave_Current_Workflow = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Workflow.setObjectName("actionSave_Current_Workflow")
        self.actionSave_Current_Plots = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Plots.setObjectName("actionSave_Current_Plots")
        self.actionSave_Current_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Current_Data.setObjectName("actionSave_Current_Data")
        self.actionCreate_New_Workflow = QtWidgets.QAction(MainWindow)
        self.actionCreate_New_Workflow.setObjectName("actionCreate_New_Workflow")
        self.actionNoise_Reduction = QtWidgets.QAction(MainWindow)
        self.actionNoise_Reduction.setObjectName("actionNoise_Reduction")
        self.actionApply_Mask = QtWidgets.QAction(MainWindow)
        self.actionApply_Mask.setObjectName("actionApply_Mask")
        self.actionInterpolate = QtWidgets.QAction(MainWindow)
        self.actionInterpolate.setObjectName("actionInterpolate")
        self.actionInstrument_Response = QtWidgets.QAction(MainWindow)
        self.actionInstrument_Response.setObjectName("actionInstrument_Response")
        self.actionALS = QtWidgets.QAction(MainWindow)
        self.actionALS.setObjectName("actionALS")
        self.actionDietrich = QtWidgets.QAction(MainWindow)
        self.actionDietrich.setObjectName("actionDietrich")
        self.actionPolyFit = QtWidgets.QAction(MainWindow)
        self.actionPolyFit.setObjectName("actionPolyFit")
        self.actionAirPLS = QtWidgets.QAction(MainWindow)
        self.actionAirPLS.setObjectName("actionAirPLS")
        self.actionFABC = QtWidgets.QAction(MainWindow)
        self.actionFABC.setObjectName("actionFABC")
        self.actionKK = QtWidgets.QAction(MainWindow)
        self.actionKK.setObjectName("actionKK")
        self.actionMario = QtWidgets.QAction(MainWindow)
        self.actionMario.setObjectName("actionMario")
        self.actionMedian = QtWidgets.QAction(MainWindow)
        self.actionMedian.setObjectName("actionMedian")
        self.actionRubberband = QtWidgets.QAction(MainWindow)
        self.actionRubberband.setObjectName("actionRubberband")
        self.actionUndecimated_Wavelet = QtWidgets.QAction(MainWindow)
        self.actionUndecimated_Wavelet.setObjectName("actionUndecimated_Wavelet")
        self.actionRatio = QtWidgets.QAction(MainWindow)
        self.actionRatio.setObjectName("actionRatio")
        self.actionTommy_s_Methgod = QtWidgets.QAction(MainWindow)
        self.actionTommy_s_Methgod.setObjectName("actionTommy_s_Methgod")
        self.actionPiecewise_Direct_Standardization = QtWidgets.QAction(MainWindow)
        self.actionPiecewise_Direct_Standardization.setObjectName("actionPiecewise_Direct_Standardization")
        self.actionPCA = QtWidgets.QAction(MainWindow)
        self.actionPCA.setObjectName("actionPCA")
        self.actionICA = QtWidgets.QAction(MainWindow)
        self.actionICA.setObjectName("actionICA")
        self.actionK_Means = QtWidgets.QAction(MainWindow)
        self.actionK_Means.setObjectName("actionK_Means")
        self.actionHierarchical = QtWidgets.QAction(MainWindow)
        self.actionHierarchical.setObjectName("actionHierarchical")
        self.actionOthers = QtWidgets.QAction(MainWindow)
        self.actionOthers.setObjectName("actionOthers")
        self.actionOthers_2 = QtWidgets.QAction(MainWindow)
        self.actionOthers_2.setObjectName("actionOthers_2")
        self.actionOthers_3 = QtWidgets.QAction(MainWindow)
        self.actionOthers_3.setObjectName("actionOthers_3")
        self.actionPLS = QtWidgets.QAction(MainWindow)
        self.actionPLS.setObjectName("actionPLS")
        self.actionSM_PLS = QtWidgets.QAction(MainWindow)
        self.actionSM_PLS.setObjectName("actionSM_PLS")
        self.actionICA_Regression = QtWidgets.QAction(MainWindow)
        self.actionICA_Regression.setObjectName("actionICA_Regression")
        self.actionGaussian_Process = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Process.setObjectName("actionGaussian_Process")
        self.actionMLP = QtWidgets.QAction(MainWindow)
        self.actionMLP.setObjectName("actionMLP")
        self.actionSVM = QtWidgets.QAction(MainWindow)
        self.actionSVM.setObjectName("actionSVM")
        self.actionOthers_4 = QtWidgets.QAction(MainWindow)
        self.actionOthers_4.setObjectName("actionOthers_4")
        self.actionOthers_5 = QtWidgets.QAction(MainWindow)
        self.actionOthers_5.setObjectName("actionOthers_5")
        self.actionIndex = QtWidgets.QAction(MainWindow)
        self.actionIndex.setObjectName("actionIndex")
        self.actionContent_2 = QtWidgets.QAction(MainWindow)
        self.actionContent_2.setObjectName("actionContent_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_QtCreator = QtWidgets.QAction(MainWindow)
        self.actionAbout_QtCreator.setObjectName("actionAbout_QtCreator")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNormalization = QtWidgets.QAction(MainWindow)
        self.actionNormalization.setObjectName("actionNormalization")
        self.actionICA_2 = QtWidgets.QAction(MainWindow)
        self.actionICA_2.setObjectName("actionICA_2")
        self.actionPCA_2 = QtWidgets.QAction(MainWindow)
        self.actionPCA_2.setObjectName("actionPCA_2")
        self.actionPLS_DA = QtWidgets.QAction(MainWindow)
        self.actionPLS_DA.setObjectName("actionPLS_DA")
        self.actionSIMCA = QtWidgets.QAction(MainWindow)
        self.actionSIMCA.setObjectName("actionSIMCA")
        self.actionK_means = QtWidgets.QAction(MainWindow)
        self.actionK_means.setObjectName("actionK_means")
        self.actionHierarchical_2 = QtWidgets.QAction(MainWindow)
        self.actionHierarchical_2.setObjectName("actionHierarchical_2")
        self.actionCross_Validation = QtWidgets.QAction(MainWindow)
        self.actionCross_Validation.setObjectName("actionCross_Validation")
        self.actionTrain = QtWidgets.QAction(MainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")
        self.actionLine_Plot = QtWidgets.QAction(MainWindow)
        self.actionLine_Plot.setObjectName("actionLine_Plot")
        self.action1_to_1_Plot = QtWidgets.QAction(MainWindow)
        self.action1_to_1_Plot.setObjectName("action1_to_1_Plot")
        self.actionScatter_Plot = QtWidgets.QAction(MainWindow)
        self.actionScatter_Plot.setObjectName("actionScatter_Plot")
        self.actionSet_output_location = QtWidgets.QAction(MainWindow)
        self.actionSet_output_location.setObjectName("actionSet_output_location")
        self.actionCreate_N_Folds = QtWidgets.QAction(MainWindow)
        self.actionCreate_N_Folds.setObjectName("actionCreate_N_Folds")
        self.actionCreate_Test_Folds = QtWidgets.QAction(MainWindow)
        self.actionCreate_Test_Folds.setObjectName("actionCreate_Test_Folds")
        self.actionSubmodel_Ranges = QtWidgets.QAction(MainWindow)
        self.actionSubmodel_Ranges.setObjectName("actionSubmodel_Ranges")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PYSAT"))
        self.regression.setTitle(_translate("MainWindow", "Regression"))
        self.regression_choosedata_label.setText(_translate("MainWindow", "Choose data:"))
        self.regression_choosedata.setItemText(0, _translate("MainWindow", "Choose Data"))
        self.regression_choosedata.setItemText(1, _translate("MainWindow", "Known Data"))
        self.regression_choosex_label.setText(_translate("MainWindow", "X Variable:"))
        __sortingEnabled = self.regression_choosex.isSortingEnabled()
        self.regression_choosex.setSortingEnabled(False)
        item = self.regression_choosex.item(0)
        item.setText(_translate("MainWindow", "Choose X"))
        self.regression_choosex.setSortingEnabled(__sortingEnabled)
        self.regression_choosey_label.setText(_translate("MainWindow", "Y Variable:"))
        self.regression_choosey.setSortingEnabled(True)
        __sortingEnabled = self.regression_choosey.isSortingEnabled()
        self.regression_choosey.setSortingEnabled(False)
        item = self.regression_choosey.item(0)
        item.setText(_translate("MainWindow", "Choose Y"))
        self.regression_choosey.setSortingEnabled(__sortingEnabled)
        self.min_label.setText(_translate("MainWindow", "Min:"))
        self.max_label.setText(_translate("MainWindow", "Max:"))
        self.regression_alg_choices.setItemText(0, _translate("MainWindow", "Choose an algorithm"))
        self.regression_alg_choices.setItemText(1, _translate("MainWindow", "PLS"))
        self.regression_alg_choices.setItemText(2, _translate("MainWindow", "GP"))
        self.regression_alg_choices.setItemText(3, _translate("MainWindow", "OLS"))
        self.regression_alg_choices.setItemText(4, _translate("MainWindow", "OMP"))
        self.regression_alg_choices.setItemText(5, _translate("MainWindow", "Lasso"))
        self.regression_alg_choices.setItemText(6, _translate("MainWindow", "Lasso LARS"))
        self.regression_alg_choices.setItemText(7, _translate("MainWindow", "Elastic Net"))
        self.regression_alg_choices.setItemText(8, _translate("MainWindow", "Ridge"))
        self.regression_alg_choices.setItemText(9, _translate("MainWindow", "More to come..."))
        self.actionLoad_Refence_Data.setText(_translate("MainWindow", "Load Refence Data"))
        self.actionLoad_Unknown_Data.setText(_translate("MainWindow", "Load Unknown Data"))
        self.actionSave_Current_Workflow.setText(_translate("MainWindow", "Save Current Workflow"))
        self.actionSave_Current_Plots.setText(_translate("MainWindow", "Save Current Plots"))
        self.actionSave_Current_Data.setText(_translate("MainWindow", "Save Current Data"))
        self.actionCreate_New_Workflow.setText(_translate("MainWindow", "Create New Workflow"))
        self.actionNoise_Reduction.setText(_translate("MainWindow", "Noise Reduction"))
        self.actionApply_Mask.setText(_translate("MainWindow", "Apply Mask"))
        self.actionInterpolate.setText(_translate("MainWindow", "Interpolate (unknown to known)"))
        self.actionInstrument_Response.setText(_translate("MainWindow", "Instrument Response"))
        self.actionALS.setText(_translate("MainWindow", "ALS"))
        self.actionDietrich.setText(_translate("MainWindow", "Dietrich"))
        self.actionPolyFit.setText(_translate("MainWindow", "PolyFit"))
        self.actionAirPLS.setText(_translate("MainWindow", "AirPLS"))
        self.actionFABC.setText(_translate("MainWindow", "FABC"))
        self.actionKK.setText(_translate("MainWindow", "KK"))
        self.actionMario.setText(_translate("MainWindow", "Mario"))
        self.actionMedian.setText(_translate("MainWindow", "Median"))
        self.actionRubberband.setText(_translate("MainWindow", "Rubberband"))
        self.actionUndecimated_Wavelet.setText(_translate("MainWindow", "Undecimated Wavelet"))
        self.actionRatio.setText(_translate("MainWindow", "Ratio"))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))
        self.actionPiecewise_Direct_Standardization.setText(_translate("MainWindow", "Piecewise Direct Standardization"))
        self.actionPCA.setText(_translate("MainWindow", "PCA"))
        self.actionICA.setText(_translate("MainWindow", "ICA"))
        self.actionK_Means.setText(_translate("MainWindow", "K-Means"))
        self.actionHierarchical.setText(_translate("MainWindow", "Hierarchical"))
        self.actionOthers.setText(_translate("MainWindow", "Others..."))
        self.actionOthers_2.setText(_translate("MainWindow", "Others..."))
        self.actionOthers_3.setText(_translate("MainWindow", "Others..."))
        self.actionPLS.setText(_translate("MainWindow", "PLS"))
        self.actionSM_PLS.setText(_translate("MainWindow", "SM-PLS"))
        self.actionICA_Regression.setText(_translate("MainWindow", "ICA Regression"))
        self.actionGaussian_Process.setText(_translate("MainWindow", "Gaussian Process"))
        self.actionMLP.setText(_translate("MainWindow", "MLP"))
        self.actionSVM.setText(_translate("MainWindow", "SVM"))
        self.actionOthers_4.setText(_translate("MainWindow", "Others..."))
        self.actionOthers_5.setText(_translate("MainWindow", "Others..."))
        self.actionIndex.setText(_translate("MainWindow", "Index"))
        self.actionContent_2.setText(_translate("MainWindow", "Content"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
        self.actionAbout_QtCreator.setText(_translate("MainWindow", "About Qt..."))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNormalization.setText(_translate("MainWindow", "Normalization"))
        self.actionICA_2.setText(_translate("MainWindow", "ICA"))
        self.actionPCA_2.setText(_translate("MainWindow", "PCA"))
        self.actionPLS_DA.setText(_translate("MainWindow", "PLS-DA"))
        self.actionSIMCA.setText(_translate("MainWindow", "SIMCA"))
        self.actionK_means.setText(_translate("MainWindow", "K-means"))
        self.actionHierarchical_2.setText(_translate("MainWindow", "Hierarchical"))
        self.actionCross_Validation.setText(_translate("MainWindow", "Cross Validation"))
        self.actionTrain.setText(_translate("MainWindow", "Train"))
        self.actionPredict.setText(_translate("MainWindow", "Predict"))
        self.actionLine_Plot.setText(_translate("MainWindow", "Line Plot"))
        self.action1_to_1_Plot.setText(_translate("MainWindow", "1 to 1 Plot"))
        self.actionScatter_Plot.setText(_translate("MainWindow", "Scatter Plot"))
        self.actionSet_output_location.setText(_translate("MainWindow", "Output Location"))
        self.actionCreate_N_Folds.setText(_translate("MainWindow", "Create N Folds"))
        self.actionCreate_Test_Folds.setText(_translate("MainWindow", "Create Test Folds"))
        self.actionSubmodel_Ranges.setText(_translate("MainWindow", "Submodel Ranges"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

