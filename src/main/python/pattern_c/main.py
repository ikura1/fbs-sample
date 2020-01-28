import sys
from fbs_runtime.application_context.PySide2 import ApplicationContext
from ui.module import Slider


if __name__ == "__main__":
    appctxt = ApplicationContext()
    widget = Slider()
    widget.show()
    sys.exit(appctxt.app.exec_())
