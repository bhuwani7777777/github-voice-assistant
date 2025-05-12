import sys
from PyQt5.QtWidgets import QApplication
from gui import ChatBotWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatBotWindow()
    window.show()
    sys.exit(app.exec_())
