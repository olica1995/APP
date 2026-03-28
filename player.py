import sys
import os
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QIcon

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class HLSPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live Stream Player")
        self.resize(1280, 720)

        # Set the Window Icon
        icon_path = resource_path("logo.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.browser = QWebEngineView()
        
        # YOUR RESTORED URL
        target_url = "https://live21.bozztv.com/akamaissh101/ssh101/livetv1995/playlist.m3u8"
        self.browser.setUrl(QUrl(target_url))
        
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set the App Icon (Taskbar)
    icon_path = resource_path("logo.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
        
    window = HLSPlayer()
    window.show()
    sys.exit(app.exec())
