from core.offsets import *
from core.esp import *
from core.trigger import *
from core.aimbot import *
from core.misc import *
from core.utils import *
from dpg.theme import *
from threading import Thread
import dearpygui.dearpygui as dpg
import ctypes, os, subprocess, time
import pyMeow as pm

class Toogle:
    data = {
        "aimbot": {
            "enable": False,
            "only_visible": False,
            "key": "shift",
            "distance": 5000,
            "fov": 10,
            "smooth": 0
        },
        "trigger": {
            "enable": False,
            "delay": 0.05,
            "key_bind": False,
            "key": "shift",
            "target_chicken": False
        },
        "esp": {
            "enemy": {
                "bone": {
                    "enable": False,
                    "color": "red",
                    "thick": 1.8
                },
                "shadow": {
                    "enable": False,
                    "color": "black",
                    "thick": 2.4
                },
                "box": {
                    "enable": False,
                    "color": "red",
                    "rounded": 0.0
                },
                "line": {
                    "enable": False,
                    "color": "red",
                    "thick": 1.5
                },
                "name": {
                    "enable": False,
                    "color": "white",
                },
                "weapon": {
                    "enable": False,
                    "color": "red",
                },
                "health": False
            },
            "friend": {
                "bone": {
                    "enable": False,
                    "color": "blue",
                    "thick": 1.8
                },
                "shadow": {
                    "enable": False,
                    "color": "black",
                    "thick": 2.4
                },
                "box": {
                    "enable": False,
                    "color": "blue",
                    "rounded": 0.0
                },
                "line": {
                    "enable": False,
                    "color": "blue",
                    "thick": 1.5
                },
                "name": {
                    "enable": False,
                    "color": "white"
                },
                "weapon": {
                    "enable": False,
                    "color": "blue"
                },
                "health": False
            }
        },
        "misc": {
            "ignore_team": False,
            "no_flash": False
        },
        "config": {
            "slot": "slot1",
            "file": "C:\\Fury\\config\\slot1"
        }
    }

class CheatSetup:
    def __init__(self):
        # create config directory
        [os.makedirs(folder, exist_ok=True) for folder in ["C:\\Fury", "C:\\Fury\\fonts", "C:\\Fury\\config"]]

        # download fonts
        Utils.download_fonts()

        # open cs automatically
        if not Utils.process_running("cs2.exe"):
            subprocess.Popen(["cmd", "/c", "start", "steam://rungameid/730"], creationflags=subprocess.CREATE_NO_WINDOW)

            while not Utils.process_running("cs2.exe"):
                time.sleep(1)

            time.sleep(10)

class CheatManager:
    def __init__(self):
        self.process = pm.open_process("cs2.exe")
        self.module = pm.get_module(self.process, "client.dll")["base"]
        self.esp = ESP(self.process, self.module)
        self.trigger = Trigger(self.process, self.module)
        self.aimbot = Aimbot(self.process, self.module)
        self.misc = Misc(self.process, self.module)

    def overlay_init(self):
        pm.overlay_init(target="Counter-Strike 2", title="Counter-Strike 2", fps=144)

        # load fonts
        for font_id, font in enumerate(["C:\\Fury\\fonts\\pixel.ttf", "C:\\Fury\\fonts\\weapon.ttf"], start=1):
            if not os.path.exists(font):
                ctypes.windll.user32.MessageBoxW(0, "Fonts could not be loaded. Please restart and try again", "Error", 0x10)
                os._exit(0)

            pm.load_font(fileName=font, fontId=font_id)

        # overlay loop
        while pm.overlay_loop():
            try:
                self.esp.update(Toogle)
                self.trigger.update(Toogle)
                self.aimbot.update(Toogle)
            except:
                pass

class CheatMenu(CheatSetup, CheatManager):
    def __init__(self):
        CheatSetup.__init__(self)
        CheatManager.__init__(self)

        self.window_width = 520
        self.window_height = 350

        thread = Thread(target=self.overlay_init, daemon=True)
        thread.start()

    def create_window(self):
        dpg.create_context()
        dpg.create_viewport()

        with dpg.font_registry():
            arial = "C:\\Fury\\fonts\\arial.ttf"

            if not os.path.exists(arial):
                ctypes.windll.user32.MessageBoxW(0, "Fonts could not be loaded. Please restart and try again", "Error", 0x10)
                os._exit(0)

            self.font = dpg.add_font(arial, 16)

        with dpg.handler_registry():
            dpg.bind_theme(Theme.window())
            dpg.bind_font(self.font)
            dpg.add_mouse_drag_handler(callback=self.draw_window)

    def create_viewport(self):
        with dpg.window(label="", width=self.window_width, height=self.window_height, no_collapse=True, no_move=True, no_resize=True, on_close=lambda: os._exit(0)):
            with dpg.tab_bar():
                # legit tab
                with dpg.tab(label="Legit"):
                    with dpg.tab_bar():
                        # visual tab
                        with dpg.tab(label="Aimbot"):
                            dpg.add_checkbox(
                                tag="<checkbox:aimbot:enable>",
                                pos=(10, 90),
                                label="Enable",
                                default_value=Toogle.data["aimbot"]["enable"],
                                callback=self.toogle_aimbot
                            )

                            dpg.add_text(
                                "(?)",
                                tag="<label:tooltip:aimbot>",
                                pos=(86, 89),
                                color=(247, 218, 0, 200)
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:aimbot:only_visible>",
                                pos=(10, 120),
                                label="Only Visible",
                                default_value=Toogle.data["aimbot"]["only_visible"],
                                callback=self.toogle_aimbot_only_visible,
                                show=Toogle.data["aimbot"]["enable"]
                            )

                            dpg.add_combo(
                                tag="<combo:aimbot:on_key>",
                                pos=(10, 150),
                                label="Key",
                                width=130,
                                items=[key for key in Utils.get_id("aimbot")],
                                default_value=Toogle.data["aimbot"]["key"],
                                callback=self.change_aimbot_key,
                                show=Toogle.data["aimbot"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:aimbot:distance>",
                                pos=(10, 180),
                                label="Distance",
                                width=130,
                                min_value=0,
                                max_value=5000,
                                default_value=Toogle.data["aimbot"]["distance"],
                                clamped=True,
                                format="%.0f",
                                callback=self.change_aimbot_distance,
                                show=Toogle.data["aimbot"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:aimbot:fov>",
                                pos=(10, 210),
                                label="Fov",
                                width=130,
                                min_value=0,
                                max_value=50,
                                default_value=Toogle.data["aimbot"]["fov"],
                                clamped=True,
                                format="%.0f",
                                callback=self.change_aimbot_fov,
                                show=Toogle.data["aimbot"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:aimbot:smooth>",
                                pos=(10, 240),
                                label="Smooth",
                                width=130,
                                min_value=0,
                                max_value=50,
                                default_value=Toogle.data["aimbot"]["smooth"],
                                clamped=True,
                                format="%.0f",
                                callback=self.change_aimbot_smooth,
                                show=Toogle.data["aimbot"]["enable"]
                            )

                        # trigger tab
                        with dpg.tab(label="Trigger"):
                            dpg.add_checkbox(
                                tag="<checkbox:trigger:enable>",
                                pos=(10, 90),
                                label="Enable",
                                default_value=Toogle.data["trigger"]["enable"],
                                callback=self.toogle_trigger
                            )

                            dpg.add_slider_float(
                                tag="<slider:trigger:delay>",
                                pos=(120, 90),
                                label="Delay",
                                width=130,
                                min_value=0.0,
                                max_value=1,
                                default_value=Toogle.data["trigger"]["delay"],
                                clamped=True,
                                format="%.2f",
                                callback=self.change_trigger_delay,
                                show=Toogle.data["trigger"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:trigger:key_bind>",
                                pos=(10, 120),
                                label="Keybind",
                                default_value=Toogle.data["trigger"]["key_bind"],
                                callback=self.change_trigger_key_bind,
                                show=Toogle.data["trigger"]["enable"]
                            )

                            dpg.add_combo(
                                tag="<combo:trigger:key>",
                                pos=(120, 120),
                                label="Key",
                                width=100,
                                items=[key for key in Utils.get_id("trigger")],
                                default_value=Toogle.data["trigger"]["key"],
                                callback=self.change_trigger_key,
                                show=Toogle.data["trigger"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:trigger:target_chicken>",
                                pos=(10, 150),
                                label="Target Chicken",
                                default_value=Toogle.data["trigger"]["target_chicken"],
                                callback=self.change_trigger_target_chicken,
                                show=Toogle.data["trigger"]["enable"]
                            )

                # visual tab
                with dpg.tab(label="Visual"):
                    with dpg.tab_bar():
                        # enemy tab
                        with dpg.tab(label="Enemy"):
                            dpg.add_checkbox(
                                tag="<checkbox:bone:enemy>",
                                pos=(10, 90),
                                label="Bone",
                                default_value=Toogle.data["esp"]["enemy"]["bone"]["enable"],
                                callback=self.toogle_bone,
                                user_data="enemy"
                            )
                            
                            dpg.add_combo(
                                tag="<combo:bone:enemy:color>",
                                pos=(120, 90),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["enemy"]["bone"]["color"],
                                callback=self.change_color,
                                user_data="bone:enemy",
                                show=Toogle.data["esp"]["enemy"]["bone"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:bone:enemy:thick>",
                                pos=(290, 90),
                                label="Thick",
                                width=130,
                                min_value=1,
                                max_value=5,
                                default_value=Toogle.data["esp"]["enemy"]["bone"]["thick"],
                                clamped=True,
                                format="%.1f",
                                callback=self.change_thick,
                                user_data="bone:enemy",
                                show=Toogle.data["esp"]["enemy"]["bone"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:shadow:enemy>",
                                pos=(10, 120),
                                label="Shadow",
                                default_value=Toogle.data["esp"]["enemy"]["shadow"]["enable"],
                                callback=self.toogle_shadow,
                                user_data="enemy"
                            )

                            dpg.add_combo(
                                tag="<combo:shadow:enemy:color>",
                                pos=(120, 120),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["enemy"]["shadow"]["color"],
                                callback=self.change_color,
                                user_data="shadow:enemy",
                                show=Toogle.data["esp"]["enemy"]["shadow"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:shadow:enemy:thick>",
                                pos=(290, 120),
                                label="Thick",
                                width=130,
                                min_value=1,
                                max_value=5,
                                default_value=Toogle.data["esp"]["enemy"]["shadow"]["thick"],
                                clamped=True,
                                format="%.1f",
                                callback=self.change_thick,
                                user_data="shadow:enemy",
                                show=Toogle.data["esp"]["enemy"]["shadow"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:box:enemy>",
                                pos=(10, 150),
                                label="Box",
                                default_value=Toogle.data["esp"]["enemy"]["box"]["enable"],
                                callback=self.toogle_box,
                                user_data="enemy"
                            )

                            dpg.add_combo(
                                tag="<combo:box:enemy:color>",
                                pos=(120, 150),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["enemy"]["box"]["color"],
                                callback=self.change_color,
                                user_data="box:enemy",
                                show=Toogle.data["esp"]["enemy"]["box"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:box:enemy:rounded>",
                                pos=(290, 150),
                                label="Rounded",
                                width=130,
                                min_value=0.0,
                                max_value=1.0,
                                default_value=Toogle.data["esp"]["enemy"]["box"]["rounded"],
                                clamped=True,
                                format="%.1f",
                                callback=self.change_radius,
                                user_data="box:enemy",
                                show=Toogle.data["esp"]["enemy"]["box"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:line:enemy>",
                                pos=(10, 180),
                                label="Line",
                                default_value=Toogle.data["esp"]["enemy"]["line"]["enable"],
                                callback=self.toogle_line,
                                user_data="enemy"
                            )
                            
                            dpg.add_combo(
                                tag="<combo:line:enemy:color>",
                                pos=(120, 180),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["enemy"]["line"]["color"],
                                callback=self.change_color,
                                user_data="line:enemy",
                                show=Toogle.data["esp"]["enemy"]["line"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:line:enemy:thick>",
                                pos=(290, 180),
                                label="Thick",
                                width=130,
                                min_value=1,
                                max_value=3,
                                default_value=Toogle.data["esp"]["enemy"]["line"]["thick"],
                                clamped=True,
                                format="%.1f",
                                callback=self.change_thick,
                                user_data="line:enemy",
                                show=Toogle.data["esp"]["enemy"]["line"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:name:enemy>",
                                pos=(10, 210),
                                label="Name",
                                default_value=Toogle.data["esp"]["enemy"]["name"]["enable"],
                                callback=self.toogle_name,
                                user_data="enemy"
                            )
                            
                            dpg.add_combo(
                                tag="<combo:name:enemy:color>",
                                pos=(120, 210),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["enemy"]["name"]["color"],
                                callback=self.change_color,
                                user_data="name:enemy",
                                show=Toogle.data["esp"]["enemy"]["name"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:weapon:enemy>",
                                pos=(10, 240),
                                label="Weapon",
                                default_value=Toogle.data["esp"]["enemy"]["weapon"]["enable"],
                                callback=self.toogle_weapon,
                                user_data="enemy"
                            )

                            dpg.add_combo(
                                tag="<combo:weapon:enemy:color>",
                                pos=(120, 240),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["enemy"]["weapon"]["color"],
                                callback=self.change_color,
                                user_data="weapon:enemy",
                                show=Toogle.data["esp"]["enemy"]["weapon"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:health:enemy>",
                                pos=(10, 270),
                                label="Health",
                                default_value=Toogle.data["esp"]["enemy"]["health"],
                                callback=self.toogle_health,
                                user_data="enemy"
                            )

                        # friend tab
                        with dpg.tab(label="Friend"):
                            dpg.add_checkbox(
                                tag="<checkbox:bone:friend>",
                                pos=(10, 90),
                                label="Bone",
                                default_value=Toogle.data["esp"]["friend"]["bone"]["enable"],
                                callback=self.toogle_bone,
                                user_data="friend"
                            )
                            
                            dpg.add_combo(
                                tag="<combo:bone:friend:color>",
                                pos=(120, 90),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["friend"]["bone"]["color"],
                                callback=self.change_color,
                                user_data="bone:friend",
                                show=Toogle.data["esp"]["friend"]["bone"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:bone:friend:thick>",
                                pos=(290, 90),
                                label="Thick",
                                width=130,
                                min_value=1,
                                max_value=5,
                                default_value=Toogle.data["esp"]["friend"]["bone"]["thick"],
                                clamped=True,
                                format="%.1f",
                                callback=self.change_thick,
                                user_data="bone:friend",
                                show=Toogle.data["esp"]["friend"]["bone"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:shadow:friend>",
                                pos=(10, 120),
                                label="Shadow",
                                default_value=Toogle.data["esp"]["friend"]["shadow"]["enable"],
                                callback=self.toogle_shadow,
                                user_data="friend"
                            )

                            dpg.add_combo(
                                tag="<combo:shadow:friend:color>",
                                pos=(120, 120),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["friend"]["shadow"]["color"],
                                callback=self.change_color,
                                user_data="shadow:friend",
                                show=Toogle.data["esp"]["friend"]["shadow"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:shadow:friend:thick>",
                                pos=(290, 120),
                                label="Thick",
                                width=130,
                                min_value=1,
                                max_value=5,
                                default_value=Toogle.data["esp"]["friend"]["shadow"]["thick"],
                                clamped=True,
                                format="%.1f",
                                callback=self.change_thick,
                                user_data="shadow:friend",
                                show=Toogle.data["esp"]["friend"]["shadow"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:box:friend>",
                                pos=(10, 150),
                                label="Box",
                                default_value=Toogle.data["esp"]["friend"]["box"]["enable"],
                                callback=self.toogle_box,
                                user_data="friend"
                            )

                            dpg.add_combo(
                                tag="<combo:box:friend:color>",
                                pos=(120, 150),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["friend"]["box"]["color"],
                                callback=self.change_color,
                                user_data="box:friend",
                                show=Toogle.data["esp"]["friend"]["box"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:box:friend:rounded>",
                                pos=(290, 150),
                                label="Rounded",
                                width=130,
                                min_value=0.0,
                                max_value=1.0,
                                default_value=Toogle.data["esp"]["friend"]["box"]["rounded"],
                                clamped=True,
                                format="%.1f",
                                callback=self.change_radius,
                                user_data="box:friend",
                                show=Toogle.data["esp"]["friend"]["box"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:line:friend>",
                                pos=(10, 180),
                                label="Line",
                                default_value=Toogle.data["esp"]["friend"]["line"]["enable"],
                                callback=self.toogle_line,
                                user_data="friend"
                            )
                            
                            dpg.add_combo(
                                tag="<combo:line:friend:color>",
                                pos=(120, 180),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["friend"]["line"]["color"],
                                callback=self.change_color,
                                user_data="line:friend",
                                show=Toogle.data["esp"]["friend"]["line"]["enable"]
                            )

                            dpg.add_slider_float(
                                tag="<slider:line:friend:thick>",
                                pos=(290, 180),
                                label="Thick",
                                width=130,
                                min_value=1,
                                max_value=3,
                                default_value=Toogle.data["esp"]["friend"]["line"]["thick"],
                                clamped=True,
                                format="%.1f",
                                callback=self.change_thick,
                                user_data="line:friend",
                                show=Toogle.data["esp"]["friend"]["line"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:name:friend>",
                                pos=(10, 210),
                                label="Name",
                                default_value=Toogle.data["esp"]["friend"]["name"]["enable"],
                                callback=self.toogle_name,
                                user_data="friend"
                            )
                            
                            dpg.add_combo(
                                tag="<combo:name:friend:color>",
                                pos=(120, 210),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["friend"]["name"]["color"],
                                callback=self.change_color,
                                user_data="name:friend",
                                show=Toogle.data["esp"]["friend"]["name"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:weapon:friend>",
                                pos=(10, 240),
                                label="Weapon",
                                default_value=Toogle.data["esp"]["friend"]["weapon"]["enable"],
                                callback=self.toogle_weapon,
                                user_data="friend"
                            )

                            dpg.add_combo(
                                tag="<combo:weapon:friend:color>",
                                pos=(120, 240),
                                label="Color",
                                width=100,
                                items=[color for color in colors],
                                default_value=Toogle.data["esp"]["friend"]["weapon"]["color"],
                                callback=self.change_color,
                                user_data="weapon:friend",
                                show=Toogle.data["esp"]["friend"]["weapon"]["enable"]
                            )

                            dpg.add_checkbox(
                                tag="<checkbox:health:friend>",
                                pos=(10, 270),
                                label="Health",
                                default_value=Toogle.data["esp"]["friend"]["health"],
                                callback=self.toogle_health,
                                user_data="friend"
                            )

                # misc tab
                with dpg.tab(label="Misc"):
                    dpg.add_checkbox(
                        tag="<checkbox:misc:ignore_team>",
                        pos=(10, 60),
                        label="Ignore Team",
                        default_value=Toogle.data["misc"]["ignore_team"],
                        callback=self.change_ignore_team
                    )

                    dpg.add_checkbox(
                        tag="<checkbox:misc:no_flash>",
                        pos=(10, 90),
                        label="No Flash",
                        default_value=Toogle.data["misc"]["no_flash"],
                        callback=self.change_no_flash
                    )

                    dpg.add_text(
                        "(?)",
                        tag="<label:tooltip:no_flash>",
                        pos=(97, 89),
                        color=(247, 218, 0, 200)
                    )

                # config tab
                with dpg.tab(label="Config"):
                    dpg.add_combo(
                        tag="<combo:config:slots>",
                        pos=(10, 60),
                        label="Config",
                        width=140,
                        items=["slot1", "slot2", "slot3", "slot4", "slot5"],
                        default_value=Toogle.data["config"]["slot"],
                        callback=self.change_config_slot
                    )
                    
                    dpg.add_button(
                        tag="<button:config:load>",
                        pos=(10, 90),
                        label="Load",
                        width=66,
                        callback=lambda: self.load_config()
                    )

                    dpg.add_button(
                        tag="<button:config:save>",
                        pos=(84, 90),
                        label="Save",
                        width=66,
                        callback=lambda: Utils.save_config(Toogle)
                    )

                    dpg.add_button(
                        tag="<button:config:open_folder>",
                        pos=(10, 120),
                        label="Open Directory",
                        width=140,
                        callback=lambda: subprocess.Popen(["cmd", "/c", "start", "C:\\Fury\\config"], creationflags=subprocess.CREATE_NO_WINDOW)
                    )

                # credits tab
                with dpg.tab(label="Credits"):
                    dpg.add_button(
                        tag="<button:credits:repository>",
                        pos=(10, 60),
                        label="Repository",
                        width=140,
                        callback=lambda: subprocess.Popen(["cmd", "/c", "start", "https://github.com/gabsroot/fury"], creationflags=subprocess.CREATE_NO_WINDOW)
                    )

                    dpg.add_button(
                        tag="<button:credits:offsets>",
                        pos=(10, 90),
                        label="Offsets",
                        width=140,
                        callback=lambda: subprocess.Popen(["cmd", "/c", "start", "https://github.com/a2x/cs2-dumper"], creationflags=subprocess.CREATE_NO_WINDOW)
                    )

        # tooltip text
        with dpg.tooltip(parent="<label:tooltip:aimbot>", tag="<tooltip:aimbot>"):
            dpg.add_text("Risk!")

        with dpg.tooltip(parent="<label:tooltip:no_flash>", tag="<tooltip:no_flash>"):
            dpg.add_text("Risk!")

        # set tooltip theme
        [dpg.bind_item_theme(item, Theme.tooltip()) for item in [
                "<tooltip:aimbot>",
                "<tooltip:no_flash>"
            ]
        ]

        # set checkbox theme 
        [dpg.bind_item_theme(item, Theme.checkbox()) for item in 
            [
                "<checkbox:aimbot:enable>",
                "<checkbox:aimbot:only_visible>",
                "<checkbox:trigger:enable>",
                "<checkbox:trigger:key_bind>",
                "<checkbox:trigger:target_chicken>",
                "<checkbox:bone:enemy>",
                "<checkbox:shadow:enemy>",
                "<checkbox:box:enemy>",
                "<checkbox:line:enemy>",
                "<checkbox:name:enemy>",
                "<checkbox:weapon:enemy>",
                "<checkbox:health:enemy>",
                "<checkbox:bone:friend>",
                "<checkbox:shadow:friend>",
                "<checkbox:box:friend>",
                "<checkbox:line:friend>",
                "<checkbox:name:friend>",
                "<checkbox:weapon:friend>",
                "<checkbox:health:friend>",
                "<checkbox:misc:ignore_team>",
                "<checkbox:misc:no_flash>"
            ]
        ]

        # set combo theme
        [dpg.bind_item_theme(item, Theme.combo()) for item in 
            [
                "<combo:aimbot:on_key>",
                "<combo:bone:enemy:color>",
                "<combo:shadow:enemy:color>",
                "<combo:box:enemy:color>",
                "<combo:line:enemy:color>",
                "<combo:name:enemy:color>",
                "<combo:weapon:enemy:color>",
                "<combo:bone:friend:color>",
                "<combo:shadow:friend:color>",
                "<combo:box:friend:color>",
                "<combo:line:friend:color>",
                "<combo:name:friend:color>",
                "<combo:weapon:friend:color>",
                "<combo:trigger:key>",
                "<combo:config:slots>"
            ]
        ]

        # set slider theme
        [dpg.bind_item_theme(item, Theme.slider()) for item in 
            [
                "<slider:aimbot:distance>",
                "<slider:aimbot:fov>",
                "<slider:aimbot:smooth>",
                "<slider:bone:enemy:thick>",
                "<slider:shadow:enemy:thick>",
                "<slider:box:enemy:rounded>",
                "<slider:line:enemy:thick>",
                "<slider:bone:friend:thick>",
                "<slider:shadow:friend:thick>",
                "<slider:box:friend:rounded>",
                "<slider:line:friend:thick>",
                "<slider:trigger:delay>"
            ]
        ]

        # set button theme
        [dpg.bind_item_theme(item, Theme.button()) for item in 
            [
                "<button:config:load>",
                "<button:config:save>",
                "<button:config:open_folder>",
                "<button:credits:repository>",
                "<button:credits:offsets>"
            ]
        ]

        # create a viewport
        dpg.create_viewport(x_pos=600, y_pos=300, title=Utils.gen_random_string(10), width=self.window_width, height=self.window_height, decorated=False, resizable=False)

    def toogle_aimbot(self, sender):
        Toogle.data["aimbot"]["enable"] = dpg.get_value(sender)
        dpg.configure_item("<checkbox:aimbot:only_visible>", show=Toogle.data["aimbot"]["enable"])
        dpg.configure_item("<combo:aimbot:on_key>", show=Toogle.data["aimbot"]["enable"])
        dpg.configure_item("<slider:aimbot:distance>", show=Toogle.data["aimbot"]["enable"])
        dpg.configure_item("<slider:aimbot:fov>", show=Toogle.data["aimbot"]["enable"])
        dpg.configure_item("<slider:aimbot:smooth>", show=Toogle.data["aimbot"]["enable"])

    def toogle_aimbot_only_visible(self, sender):
        Toogle.data["aimbot"]["only_visible"] = dpg.get_value(sender)

    def change_aimbot_key(self, sender):
        Toogle.data["aimbot"]["key"] = dpg.get_value(sender)

    def change_aimbot_distance(self, sender):
        Toogle.data["aimbot"]["distance"] = int(dpg.get_value(sender))

    def change_aimbot_fov(self, sender):
        Toogle.data["aimbot"]["fov"] = int(dpg.get_value(sender))

    def change_aimbot_smooth(self, sender):
        Toogle.data["aimbot"]["smooth"] = int(dpg.get_value(sender))

    def toogle_trigger(self, sender):
        Toogle.data["trigger"]["enable"] = dpg.get_value(sender)
        dpg.configure_item("<slider:trigger:delay>", show=Toogle.data["trigger"]["enable"])
        dpg.configure_item("<checkbox:trigger:key_bind>", show=Toogle.data["trigger"]["enable"])
        dpg.configure_item("<checkbox:trigger:key_bind>", show=Toogle.data["trigger"]["enable"])
        dpg.configure_item("<combo:trigger:key>", show=Toogle.data["trigger"]["enable"])
        dpg.configure_item("<checkbox:trigger:target_chicken>", show=Toogle.data["trigger"]["enable"])

    def change_trigger_key_bind(self, sender):
        Toogle.data["trigger"]["key_bind"] = dpg.get_value(sender)

    def change_trigger_key(self, sender):
        Toogle.data["trigger"]["key"] = dpg.get_value(sender)

    def change_trigger_delay(self, sender):
        Toogle.data["trigger"]["delay"] = dpg.get_value(sender)

    def change_trigger_target_chicken(self, sender):
        Toogle.data["trigger"]["target_chicken"] = dpg.get_value(sender)

    def toogle_bone(self, sender, app_data, user_data):
        Toogle.data["esp"][user_data]["bone"]["enable"] = dpg.get_value(sender)
        dpg.configure_item(f"<combo:bone:{user_data}:color>", show=Toogle.data["esp"][user_data]["bone"]["enable"])
        dpg.configure_item(f"<slider:bone:{user_data}:thick>", show=Toogle.data["esp"][user_data]["bone"]["enable"])

    def toogle_shadow(self, sender, app_data, user_data):
        Toogle.data["esp"][user_data]["shadow"]["enable"] = dpg.get_value(sender)
        dpg.configure_item(f"<combo:shadow:{user_data}:color>", show=Toogle.data["esp"][user_data]["shadow"]["enable"])
        dpg.configure_item(f"<slider:shadow:{user_data}:thick>", show=Toogle.data["esp"][user_data]["shadow"]["enable"])

    def toogle_box(self, sender, app_data, user_data):
        Toogle.data["esp"][user_data]["box"]["enable"] = dpg.get_value(sender)
        dpg.configure_item(f"<combo:box:{user_data}:color>", show=Toogle.data["esp"][user_data]["box"]["enable"])
        dpg.configure_item(f"<slider:box:{user_data}:rounded>", show=Toogle.data["esp"][user_data]["box"]["enable"])

    def toogle_line(self, sender, app_data, user_data):
        Toogle.data["esp"][user_data]["line"]["enable"] = dpg.get_value(sender)
        dpg.configure_item(f"<combo:line:{user_data}:color>", show=Toogle.data["esp"][user_data]["line"]["enable"])
        dpg.configure_item(f"<slider:line:{user_data}:thick>", show=Toogle.data["esp"][user_data]["line"]["enable"])

    def toogle_name(self, sender, app_data, user_data):
        Toogle.data["esp"][user_data]["name"]["enable"] = dpg.get_value(sender)
        dpg.configure_item(f"<combo:name:{user_data}:color>", show=Toogle.data["esp"][user_data]["name"]["enable"])

    def toogle_weapon(self, sender, app_data, user_data):
        Toogle.data["esp"][user_data]["weapon"]["enable"] = dpg.get_value(sender)
        dpg.configure_item(f"<combo:weapon:{user_data}:color>", show=Toogle.data["esp"][user_data]["weapon"]["enable"])

    def toogle_health(self, sender, app_data, user_data):
        Toogle.data["esp"][user_data]["health"] = dpg.get_value(sender)

    def change_color(self, sender, app_data, user_data):
        data = user_data.split(":")
        Toogle.data["esp"][data[1]][data[0]]["color"] = dpg.get_value(sender)

    def change_thick(self, sender, app_data, user_data):
        data = user_data.split(":")
        Toogle.data["esp"][data[1]][data[0]]["thick"] = dpg.get_value(sender)

    def change_radius(self, sender, app_data, user_data):
        data = user_data.split(":")
        Toogle.data["esp"][data[1]][data[0]]["rounded"] = dpg.get_value(sender)

    def change_ignore_team(self, sender):
        Toogle.data["misc"]["ignore_team"] = dpg.get_value(sender)

    def change_no_flash(self, sender):
        Toogle.data["misc"]["no_flash"] = dpg.get_value(sender)
        self.misc.no_flash(Toogle)

    def change_config_slot(self, sender):
        Toogle.data["config"]["file"] = f"C:\\Fury\\config\\{dpg.get_value(sender)}"

    def load_config(self):
        try:
            config = Utils.load_config(Toogle)

            if not config:
                ctypes.windll.user32.MessageBoxW(0, "This configuration does not exist", "Error", 0x10)
                return

            Toogle.data = config

            # aimbot
            dpg.set_value("<checkbox:aimbot:enable>", value=config["aimbot"]["enable"])
            dpg.set_value("<checkbox:aimbot:only_visible>", value=config["aimbot"]["only_visible"])
            dpg.set_value("<combo:aimbot:on_key>", value=config["aimbot"]["key"])
            dpg.set_value("<slider:aimbot:distance>", value=config["aimbot"]["distance"])
            dpg.set_value("<slider:aimbot:fov>", value=config["aimbot"]["fov"])
            dpg.set_value("<slider:aimbot:smooth>", value=config["aimbot"]["smooth"])

            # show aimbot controls
            dpg.configure_item(item="<combo:aimbot:on_key>", show=config["aimbot"]["enable"])
            dpg.configure_item(item="<checkbox:aimbot:only_visible>", show=config["aimbot"]["enable"])
            dpg.configure_item(item="<slider:aimbot:distance>", show=config["aimbot"]["enable"])
            dpg.configure_item(item="<slider:aimbot:fov>", show=config["aimbot"]["enable"])
            dpg.configure_item(item="<slider:aimbot:smooth>", show=config["aimbot"]["enable"])

            # trigger
            dpg.set_value("<checkbox:trigger:enable>", value=config["trigger"]["enable"])
            dpg.set_value("<slider:trigger:delay>", value=config["trigger"]["delay"])
            dpg.set_value("<checkbox:trigger:key_bind>", value=config["trigger"]["key_bind"])
            dpg.set_value("<combo:trigger:key>", value=config["trigger"]["key"])
            dpg.set_value("<checkbox:trigger:target_chicken>", value=config["trigger"]["target_chicken"])

            # show trigger controls
            dpg.configure_item(item="<slider:trigger:delay>", show=config["trigger"]["enable"])
            dpg.configure_item(item="<checkbox:trigger:key_bind>", show=config["trigger"]["enable"])
            dpg.configure_item(item="<combo:trigger:key>", show=config["trigger"]["enable"])
            dpg.configure_item(item="<checkbox:trigger:target_chicken>", show=config["trigger"]["enable"])

            # esp enemy
            dpg.set_value("<checkbox:bone:enemy>", value=config["esp"]["enemy"]["bone"]["enable"])
            dpg.set_value("<combo:bone:enemy:color>", value=config["esp"]["enemy"]["bone"]["color"])
            dpg.set_value("<slider:bone:enemy:thick>", value=config["esp"]["enemy"]["bone"]["thick"])
            dpg.set_value("<checkbox:shadow:enemy>", value=config["esp"]["enemy"]["shadow"]["enable"])
            dpg.set_value("<combo:shadow:enemy:color>", value=config["esp"]["enemy"]["shadow"]["color"])
            dpg.set_value("<slider:shadow:enemy:thick>", value=config["esp"]["enemy"]["shadow"]["thick"])
            dpg.set_value("<checkbox:box:enemy>", value=config["esp"]["enemy"]["box"]["enable"])
            dpg.set_value("<combo:box:enemy:color>", value=config["esp"]["enemy"]["box"]["color"])
            dpg.set_value("<slider:box:enemy:rounded>", value=config["esp"]["enemy"]["box"]["rounded"])
            dpg.set_value("<checkbox:line:enemy>", value=config["esp"]["enemy"]["line"]["enable"])
            dpg.set_value("<combo:line:enemy:color>", value=config["esp"]["enemy"]["line"]["color"])
            dpg.set_value("<slider:line:enemy:thick>", value=config["esp"]["enemy"]["line"]["thick"])
            dpg.set_value("<checkbox:name:enemy>", value=config["esp"]["enemy"]["name"]["enable"])
            dpg.set_value("<combo:name:enemy:color>", value=config["esp"]["enemy"]["name"]["color"])
            dpg.set_value("<checkbox:weapon:enemy>", value=config["esp"]["enemy"]["weapon"]["enable"])
            dpg.set_value("<combo:weapon:enemy:color>", value=config["esp"]["enemy"]["weapon"]["color"])
            dpg.set_value("<checkbox:health:enemy>", value=config["esp"]["enemy"]["health"])

            # show enemy controls
            dpg.configure_item(item="<combo:bone:enemy:color>", show=config["esp"]["enemy"]["bone"]["enable"])
            dpg.configure_item(item="<slider:bone:enemy:thick>", show=config["esp"]["enemy"]["bone"]["enable"])
            dpg.configure_item(item="<combo:shadow:enemy:color>", show=config["esp"]["enemy"]["shadow"]["enable"])
            dpg.configure_item(item="<slider:shadow:enemy:thick>", show=config["esp"]["enemy"]["shadow"]["enable"])
            dpg.configure_item(item="<combo:box:enemy:color>", show=config["esp"]["enemy"]["box"]["enable"])
            dpg.configure_item(item="<slider:box:enemy:rounded>", show=config["esp"]["enemy"]["box"]["enable"])
            dpg.configure_item(item="<combo:line:enemy:color>", show=config["esp"]["enemy"]["line"]["enable"])
            dpg.configure_item(item="<slider:line:enemy:thick>", show=config["esp"]["enemy"]["line"]["enable"])
            dpg.configure_item(item="<combo:name:enemy:color>", show=config["esp"]["enemy"]["name"]["enable"])
            dpg.configure_item(item="<combo:weapon:enemy:color>", show=config["esp"]["enemy"]["weapon"]["enable"])

            # esp friend
            dpg.set_value("<checkbox:bone:friend>", value=config["esp"]["friend"]["bone"]["enable"])
            dpg.set_value("<combo:bone:friend:color>", value=config["esp"]["friend"]["bone"]["color"])
            dpg.set_value("<slider:bone:friend:thick>", value=config["esp"]["friend"]["bone"]["thick"])
            dpg.set_value("<checkbox:shadow:friend>", value=config["esp"]["friend"]["shadow"]["enable"])
            dpg.set_value("<combo:shadow:friend:color>", value=config["esp"]["friend"]["shadow"]["color"])
            dpg.set_value("<slider:shadow:friend:thick>", value=config["esp"]["friend"]["shadow"]["thick"])
            dpg.set_value("<checkbox:box:friend>", value=config["esp"]["friend"]["box"]["enable"])
            dpg.set_value("<combo:box:friend:color>", value=config["esp"]["friend"]["box"]["color"])
            dpg.set_value("<slider:box:friend:rounded>", value=config["esp"]["friend"]["box"]["rounded"])
            dpg.set_value("<checkbox:line:friend>", value=config["esp"]["friend"]["line"]["enable"])
            dpg.set_value("<combo:line:friend:color>", value=config["esp"]["friend"]["line"]["color"])
            dpg.set_value("<slider:line:friend:thick>", value=config["esp"]["friend"]["line"]["thick"])
            dpg.set_value("<checkbox:name:friend>", value=config["esp"]["friend"]["name"]["enable"])
            dpg.set_value("<combo:name:friend:color>", value=config["esp"]["friend"]["name"]["color"])
            dpg.set_value("<checkbox:weapon:friend>", value=config["esp"]["friend"]["weapon"]["enable"])
            dpg.set_value("<combo:weapon:friend:color>", value=config["esp"]["friend"]["weapon"]["color"])
            dpg.set_value("<checkbox:health:friend>", value=config["esp"]["friend"]["health"])
            
            # show friend controls
            dpg.configure_item(item="<combo:bone:friend:color>", show=config["esp"]["friend"]["bone"]["enable"])
            dpg.configure_item(item="<slider:bone:friend:thick>", show=config["esp"]["friend"]["bone"]["enable"])
            dpg.configure_item(item="<combo:shadow:friend:color>", show=config["esp"]["friend"]["shadow"]["enable"])
            dpg.configure_item(item="<slider:shadow:friend:thick>", show=config["esp"]["friend"]["shadow"]["enable"])
            dpg.configure_item(item="<combo:box:friend:color>", show=config["esp"]["friend"]["box"]["enable"])
            dpg.configure_item(item="<slider:box:friend:rounded>", show=config["esp"]["friend"]["box"]["enable"])
            dpg.configure_item(item="<combo:line:friend:color>", show=config["esp"]["friend"]["line"]["enable"])
            dpg.configure_item(item="<slider:line:friend:thick>", show=config["esp"]["friend"]["line"]["enable"])
            dpg.configure_item(item="<combo:name:friend:color>", show=config["esp"]["friend"]["name"]["enable"])
            dpg.configure_item(item="<combo:weapon:friend:color>", show=config["esp"]["friend"]["weapon"]["enable"])

            # misc
            dpg.set_value("<checkbox:misc:ignore_team>", value=config["misc"]["ignore_team"])
            dpg.set_value("<checkbox:misc:no_flash>", value=config["misc"]["no_flash"])
        except:
            ctypes.windll.user32.MessageBoxW(0, "An error occurred loading this config", "Error", 0x10)

    def draw_window(self, sender, app, user):
        if dpg.get_mouse_pos(local=False)[1] <= 50:
            pos = dpg.get_viewport_pos()
            dpg.set_viewport_pos([pos[0] + app[1], max(pos[1] + app[2], 0)])

    def run(self):
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

app = CheatMenu()
app.create_window()
app.create_viewport()
app.run()