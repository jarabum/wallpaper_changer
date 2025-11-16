import vlc
import ctypes
from PyQt5.QtWidgets import QApplication, QWidget
import urllib.parse
import sys

def find_desktop_window():
    progman = ctypes.windll.user32.FindWindowW("Progman", None)
    ctypes.windll.user32.SendMessageTimeoutW(progman, 0x052C, 0, 0, 0, 1000, 0)
    return progman

class VlcWallpaper(QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.setWindowFlags(self.windowFlags() | 0x00000080)
        self.showFullScreen()
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        file_uri = 'file:///' + urllib.parse.quote(video_path.replace("\\", "/"))
        winid = int(self.winId())
        self.player.set_hwnd(winid)
        self.player.set_mrl(file_uri)
        self.player.play()

def playvideo(video_path):
    app = QApplication(sys.argv)
    w = VlcWallpaper(video_path)
    desktop_hwnd = find_desktop_window()
    w_winid = int(w.winId())
    ctypes.windll.user32.SetParent(w_winid, desktop_hwnd)
    ctypes.windll.user32.SetWindowPos(w_winid, 0, 0, 0, w.width(), w.height(), 0x0040)
    w.show()
    app.exec_()

playvideo(sys.argv[1])