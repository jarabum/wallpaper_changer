import sys
import vlc
from PyQt5.QtWidgets import QApplication, QWidget
import ctypes

def find_desktop_window():
    progman = ctypes.windll.user32.FindWindowW("Progman", None)
    ctypes.windll.user32.SendMessageTimeoutW(progman, 0x052C, 0, 0, 0, 1000, 0)
    return progman

class VlcWallpaper(QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.setWindowFlags(self.windowFlags() | 0x00000080)
        self.showFullScreen()
        self.vlc_instance = vlc.Instance()
        self.media_list = self.vlc_instance.media_list_new([video_path])
        self.list_player = self.vlc_instance.media_list_player_new()
        self.player = self.list_player.get_media_player()
        winid = int(self.winId())
        self.player.set_hwnd(winid)
        self.list_player.set_media_list(self.media_list)
        self.list_player.set_playback_mode(vlc.PlaybackMode.loop)
        self.list_player.play()

def playvideo(video_path):
    app = QApplication(sys.argv)
    w = VlcWallpaper(video_path)
    desktop_hwnd = find_desktop_window()
    w_winid = int(w.winId())
    ctypes.windll.user32.SetParent(w_winid, desktop_hwnd)
    ctypes.windll.user32.SetWindowPos(
        w_winid, 0, 0, 0, w.width(), w.height(), 0x0040
    )
    w.show()
    app.exec_()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        playvideo(sys.argv[1])
    else:
        print("Usage: python playvideo.py path_to_video.mp4")