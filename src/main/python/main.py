import sys
from fbs_runtime.application_context.PySide2 import ApplicationContext
# from fbs_runtime.application_context import ApplicationContext
from PySide2.QtWidgets import QApplication, QDialog
from forms.debugger import Debugger
from module_a import Button
from hoge.module_b import Dialog


if __name__ == "__main__":
    appctxt = ApplicationContext()
    # widget = Button()
    # widget = Dialog()
    widget = Debugger()
    widget.show()
    sys.exit(appctxt.app.exec_())
