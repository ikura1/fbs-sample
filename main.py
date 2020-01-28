import sys
from fbs_runtime.application_context import ApplicationContext
from PySide2.QtWidgets import QApplication, QDialog
from forms.debugger import Debugger


if __name__ == "__main__":
    appctxt = ApplicationContext()
    dialog = Dubugger()
    dialog.show()
    sys.exit(appctxt.app.exec_())
