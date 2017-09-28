


        MainWindow.resize(557, 658)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regression = QtWidgets.QGroupBox(self.centralWidget)
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
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method"))



