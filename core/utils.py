from tempfile import gettempdir
from requests import get
import dearpygui.dearpygui as dpg
import os, ctypes, random, string

class Utils:
    def __init__(self):
        self.url = "https://github.com/matomo-org/travis-scripts/raw/master/fonts/Arial.ttf"

    def ShowMessageBox(self, title, message, icon):
        # Error: 0x10, Question: 0x20, Warning: 0x30, Info: 0x40
        ctypes.windll.user32.MessageBoxW(0, message, title, icon)

    def LoadFont(self):
        try:
            response = get(self.url)

            if response.status_code == 200:
                font = os.path.join(gettempdir(), "Arial.ttf")

                if not os.path.exists(font):
                    with open(font, "wb") as file:
                        file.write(response.content)

                return font
        except:
            self.ShowMessageBox("Error", "An error occurred while downloading the font", 0x10)
            os._exit(0)

    def LoadTheme(self):
        with dpg.theme() as theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (0, 18, 33, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 18, 33, 255))
                dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, (255, 255, 255, 150))
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (36, 38, 51, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Tab, (12, 26, 38, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabActive, (18, 56, 82, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TabHovered, (18, 56, 82, 255))
                dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (59, 68, 88, 255))
                dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (72, 81, 102, 255))
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (13, 26, 41, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 41, 71, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (59, 68, 88, 255)) 
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (72, 81, 102, 255))
                dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (38, 203, 190, 255))
                dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, (36, 38, 51, 255))
                dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, (36, 38, 51, 255))
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (87, 87, 87, 255))
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (87, 87, 87, 150))

        return theme

    def DragWindow(self, sender, app, user):
        if dpg.get_mouse_pos(local=False)[1] <= 50:
            pos = dpg.get_viewport_pos()
            dpg.set_viewport_pos([pos[0] + app[1], max(pos[1] + app[2], 0)])

    def GenRandomString(self, length):
        return "".join(random.choices(string.ascii_letters, k=length))
