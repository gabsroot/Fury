import pyMeow as pm, os, ctypes
from core.utils import *
from cheat.features.esp import *
from cheat.features.aimbot import *
from cheat.features.trigger import *

class Overlay:
    def __init__(self):
        try:
            self.process = pm.open_process("cs2.exe")
            self.module = pm.get_module(self.process, "client.dll")["base"]
            self.title = Utils.random_string(10)
            
            self.esp = ESP(self.process, self.module)
            self.aimbot = Aimbot(self.process, self.module)
            self.trigger = Trigger(self.process, self.module)
        except:
            ctypes.windll.user32.MessageBoxW(0, "Failed to open process. Please restart and try again.", "Error", 0x10)
            os._exit(0)

    def render(self):
        pm.overlay_init(target=self.title, title=self.title, fps=144)

        for font_id, font in enumerate(["C:/Fury/fonts/pixel.ttf", "C:/Fury/fonts/weapon.ttf"], start=1):
            if not os.path.exists(font):
                ctypes.windll.user32.MessageBoxW(0, "Failed to load fonts. Please restart and try again.", "Error", 0x10)
                os._exit(0)

            pm.load_font(fileName=font, fontId=font_id)

        # render
        while pm.overlay_loop():
            try:
                self.esp.update()
                self.aimbot.update()
                self.trigger.update()

                pm.end_drawing()
            except:
                continue
