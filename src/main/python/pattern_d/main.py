import sys
from fbs_runtime.application_context.PySide2 import ApplicationContext
from forms.debugger import Debugger


if __name__ == "__main__":
    appctxt = ApplicationContext()
    widget = Debugger()
    widget.show()
    sys.exit(appctxt.app.exec_())
