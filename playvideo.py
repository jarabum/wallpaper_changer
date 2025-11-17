import sys
import vlc
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import Qt
import ctypes

def find_desktop_window():
    progman = ctypes.windll.user32.FindWindowW("Progman", None)
    ctypes.windll.user32.SendMessageTimeoutW(progman, 0x052C, 0, 0, 0, 1000, 0)
    return progman

class VlcWallpaper(QWidget):
    def __init__(self, video_path, monitor_geometry):
        super().__init__()
        # Make the window completely borderless and not in taskbar
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setGeometry(monitor_geometry)
        self.vlc_instance = vlc.Instance()
        self.media_list = self.vlc_instance.media_list_new([video_path])
        self.list_player = self.vlc_instance.media_list_player_new()
        self.player = self.list_player.get_media_player()
        winid = int(self.winId())
        self.player.set_hwnd(winid)
        self.list_player.set_media_list(self.media_list)
        self.list_player.set_playback_mode(vlc.PlaybackMode.loop)
        self.list_player.play()

def playvideo(video_path, monitor_index=0):
    app = QApplication(sys.argv)
    screens = QGuiApplication.screens()
    if monitor_index < 0 or monitor_index >= len(screens):
        print(f"Monitor index {monitor_index} out of range (found {len(screens)} monitors)")
        monitor_index = 0
    geometry = screens[monitor_index].geometry()
    w = VlcWallpaper(video_path, geometry)
    desktop_hwnd = find_desktop_window()
    w_winid = int(w.winId())
    ctypes.windll.user32.SetParent(w_winid, desktop_hwnd)
    # Set the window to exactly fill the chosen monitor
    ctypes.windll.user32.SetWindowPos(
        w_winid, 0, geometry.left(), geometry.top(),
        geometry.width(), geometry.height(), 0x0040
    )
    w.show()
    app.exec_()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Example: python playvideo.py path_to_video.mp4 1
        video_path = sys.argv[1]
        monitor_index = 0
        if len(sys.argv) > 2:
            try:
                monitor_index = int(sys.argv[2])
            except Exception:
                monitor_index = 0
        playvideo(video_path, monitor_index)
    else:
        print("Usage: python playvideo.py path_to_video.mp4 [monitor_index]")