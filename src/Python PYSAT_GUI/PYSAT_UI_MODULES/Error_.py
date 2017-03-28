from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QDialog


# When a window is opened
# |----------------------|
# |               - || x |
# |----------------------|
# |                      |
# |   This is an Error   |
# |       Message        |
# |                      |
# |              | ok |  |
# |----------------------|
#
# As long as this window is open we let a variable hold True
# it will prominently go False when the Window is closed




class error_print(QDialog):
    def __init__(self, message):
        """
        Outputs an error to the user in a separate window

        Usage

        :param message: error_print("Error message here")
        """
        super().__init__()
        self.message = message
        try:
            self.error_print(self.message)
        except:
            print(self.message)

    def error_print(self, message):
        print(message)
        try:
            """
            Warning Message Box
            """
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(message)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        except:
            pass

