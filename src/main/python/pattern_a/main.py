import sys
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QSpinBox


class SpinBox(QSpinBox):
    pass


if __name__ == "__main__":
    appctxt = ApplicationContext()
    widget = SpinBox()
    widget.show()
    sys.exit(appctxt.app.exec_())
