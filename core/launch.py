import subprocess, time, os, requests, ctypes
from core.utils import *

class Launch:
    def __init__(self):
        self.process = "cs2.exe"
        self.app_id = 730

        self.create_setup_folder()
        self.download_fonts()

    def wait(self):
        if not Utils.process_running(self.process):
            subprocess.Popen(["cmd", "/c", "start", f"steam://rungameid/{self.app_id}"], creationflags=subprocess.CREATE_NO_WINDOW)

            while not Utils.process_running(self.process):
                time.sleep(1)

            time.sleep(30)

    def create_setup_folder(self):
        try:
            for folder in ["C:/Fury", "C:/Fury/fonts", "C:/Fury/config"]:
                os.makedirs(name=folder, exist_ok=True)
        except:
            ctypes.windll.user32.MessageBoxW(0, "Failed to create configuration folder. Please restart and try again.", "Error", 0x10)
            os._exit(0)

    def download_fonts(self):
        try:
            fonts = [
                {"url": "https://github.com/gabsroot/Fury/raw/main/fonts/arial.ttf", "name": "arial.ttf"},
                {"url": "https://github.com/gabsroot/Fury/raw/main/fonts/pixel.ttf", "name": "pixel.ttf"},
                {"url": "https://github.com/gabsroot/Fury/raw/main/fonts/weapon.ttf", "name": "weapon.ttf"}
            ]

            for font in fonts:
                font_path = f"C:/Fury/fonts/{font['name']}"

                if not os.path.exists(font_path):
                    response = requests.get(font["url"])

                    if response.status_code == 200:
                        with open(font_path, "wb") as file:
                            file.write(response.content)
        except:
            ctypes.windll.user32.MessageBoxW(0, "Failed to download fonts. Please restart and try again.", "Error", 0x10)
            os._exit(0)
