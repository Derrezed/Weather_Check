from PyQt5.QtWidgets import QApplication
import sys
from GuiWindow import GuiWindow


app = QApplication(sys.argv)
win = GuiWindow()
win.show()
sys.exit(app.exec_())



