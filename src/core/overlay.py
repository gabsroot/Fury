import pyMeow as pm
from ui.materials.draw import *
from ui.controllers.control import *
from ui.resources.fonts import *
from core.utils import *
from features.esp import *
from features.aimbot import *
from features.trigger import *

class App:
    def __init__(self):

        if not pm.process_exists(processName="cs2.exe"):
            ctypes.windll.user32.MessageBoxW(0, "The cs2.exe process was not found.\n\nPlease open the game and try again.", "Warning", 0x30)
            os._exit(0)
        
        title = Utils.random_string(10)

        # overlay
        pm.overlay_init(target=title, title=title, fps=144, exitKey=0)
        pm.set_fps(pm.get_monitor_refresh_rate())

        # create dirs
        os.makedirs(name="C:/Fury", exist_ok=True)

        # fonts
        Fonts.load(name="arial.ttf", ref=1)
        Fonts.load(name="icons.ttf", ref=2)
        Fonts.load(name="weapon.ttf", ref=3)

        # process
        self.process = pm.open_process("cs2.exe")
        self.module = pm.get_module(self.process, "client.dll")["base"]

        # ftr
        self.esp = ESP(self.process, self.module)
        self.aimbot = Aimbot(self.process, self.module)
        self.trigger = Trigger(self.process, self.module)

    def run(self):

        while pm.overlay_loop():
            try:
                pm.begin_drawing()

                self.esp.update()
                self.aimbot.update()
                self.trigger.update()

                # Draw.draw_spectators()
                Draw.draw_menu()

                Control.update_mouse()
                Control.toggle_menu()
                Control.auto_close()
                
                # Control.drag_spectators()
                Control.drag_menu()

                pm.end_drawing()
            except:
                continue
