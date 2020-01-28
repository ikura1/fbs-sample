import sys
from fbs_runtime.application_context.PySide2 import ApplicationContext
from module import Button


if __name__ == "__main__":
    appctxt = ApplicationContext()
    widget = Button()
    widget.show()
    sys.exit(appctxt.app.exec_())
