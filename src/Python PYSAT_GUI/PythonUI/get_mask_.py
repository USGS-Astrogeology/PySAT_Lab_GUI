from PyQt4 import QtCore, QtGui
from pysat_function import pysat_func

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class get_mask_(object):
    def __init__(self):
        self.pysat_fun = pysat_func()

    def get_mask(self, get_mask):
        self.get_mask = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.get_mask.setFont(font)
        self.get_mask.setObjectName(_fromUtf8("get_mask"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.get_mask)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_mask_label = QtGui.QLabel(self.get_mask)
        self.get_mask_label.setObjectName(_fromUtf8("get_mask_label"))
        self.horizontalLayout.addWidget(self.get_mask_label)
        self.get_mask_line_edit = QtGui.QLineEdit(self.get_mask)
        self.get_mask_line_edit.setReadOnly(True)
        self.get_mask_line_edit.setObjectName(_fromUtf8("get_mask_line_edit"))
        self.horizontalLayout.addWidget(self.get_mask_line_edit)
        self.get_mask_button = QtGui.QToolButton(self.get_mask)
        self.get_mask_button.setObjectName(_fromUtf8("get_mask_button"))
        self.horizontalLayout.addWidget(self.get_mask_button)
        self.verticalLayout_8.addWidget(self.get_mask)

        self.get_mask.setTitle(_translate("MainWindow", "Mask File", None))
        self.get_mask_label.setText(_translate("MainWindow", "File Name", None))
        self.get_mask_line_edit.setText(_translate("MainWindow", "*.csv", None))
        self.get_mask_button.setText(_translate("MainWindow", "...", None))
        try:
            self.get_mask_button.clicked.connect(
                lambda: get_mask.on_getDataButton_clicked(self, self.get_data_k_line_edit, "Known"))
        except:
            pass

    def on_getDataButton_clicked(self, lineEdit, key):
        filename = QtGui.QFileDialog.getOpenFileName(None, "Open " + key + " Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")
        self.pysat_fun.get_data(filename, key)