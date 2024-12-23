import dearpygui.dearpygui as dpg
import os, ctypes, json, subprocess
from config import *
from ui.theme import *
from core.utils import *

class Menu:
    def __init__(self):
        self.window_width = 550
        self.window_height = 400

    def setup_registry(self):
        dpg.create_context()

        with dpg.font_registry():
            try:
                self.arial = dpg.add_font("C:/Fury/fonts/arial.ttf", 16)
                self.weapon = dpg.add_font("C:/Fury/fonts/weapon.ttf", 16)
            except:
                ctypes.windll.user32.MessageBoxW(0, "Failed to load fonts. Please restart and try again.", "Error", 0x10)
                os._exit(0)
            
        with dpg.handler_registry():
            dpg.bind_theme(Theme.window())
            dpg.bind_font(self.arial)
            dpg.add_mouse_drag_handler(callback=self.drag_window)

    def drag_window(self, sender, app, user):
        if dpg.get_mouse_pos(local=False)[1] <= 35:
            pos = dpg.get_viewport_pos()
            x = pos[0] + app[1]
            y = max(pos[1] + app[2], 0)
            dpg.set_viewport_pos([x, y])

    def create_viewport(self):
        with dpg.window(label="", width=self.window_width, height=self.window_height, no_collapse=True, no_move=True, no_resize=True, on_close=lambda: os._exit(0)):
            
            with dpg.tab_bar():

                # legit tab
                with dpg.tab(label="Legit"):

                    with dpg.tab_bar():

                        # aimbot tab
                        with dpg.tab(label="Aimbot"):

                            # enable
                            dpg.add_checkbox(
                                tag="aimbot.enable",
                                pos=(10, 90),
                                label="Enable",
                                user_data="aimbot",
                                callback=self.change_state
                            )

                            dpg.add_checkbox(
                                tag="aimbot.only_visible",
                                pos=(10, 120),
                                label="Only Visible",
                                user_data="aimbot.only_visible",
                                callback=self.change_state
                            )

                            dpg.add_checkbox(
                                tag="aimbot.draw_fov",
                                pos=(10, 150),
                                label="Draw Fov",
                                user_data="aimbot.draw_fov",
                                callback=self.change_state
                            )

                            dpg.add_combo(
                                tag="aimbot.key",
                                pos=(10, 180),
                                label="Key",
                                width=120,
                                items=["shift", "ctrl", "mouse_1"],
                                default_value="shift",
                                user_data="aimbot.key",
                                callback=self.change_combo
                            )

                            dpg.add_slider_int(
                                tag="aimbot.fov",
                                pos=(10, 210),
                                label="Fov",
                                width=120,
                                min_value=5,
                                max_value=300,
                                default_value=10,
                                user_data="aimbot.fov",
                                callback=self.change_slider
                            )

                            dpg.add_slider_int(
                                tag="aimbot.smooth",
                                pos=(10, 240),
                                label="Smooth",
                                width=120,
                                min_value=0,
                                max_value=100,
                                default_value=0,
                                user_data="aimbot.smooth",
                                callback=self.change_slider
                            )

                            dpg.add_slider_int(
                                tag="aimbot.distance",
                                pos=(10, 270),
                                label="Distance",
                                width=120,
                                min_value=0,
                                max_value=5000,
                                default_value=5000,
                                user_data="aimbot.distance",
                                callback=self.change_slider
                            )

                        # trigger tab
                        with dpg.tab(label="Trigger"):

                            # enable
                            dpg.add_checkbox(
                                tag="trigger.enable",
                                pos=(10, 90),
                                label="Enable",
                                user_data="trigger",
                                callback=self.change_state
                            )

                            dpg.add_checkbox(
                                tag="trigger.target_chicken",
                                pos=(10, 120),
                                label="Target Chicken",
                                user_data="trigger.target_chicken",
                                callback=self.change_state
                            )

                            dpg.add_combo(
                                tag="trigger.key",
                                pos=(10, 150),
                                label="Key",
                                width=120,
                                items=["none", "shift", "ctrl"],
                                default_value="none",
                                user_data="trigger.key",
                                callback=self.change_combo
                            )
                            
                            dpg.add_slider_float(
                                tag="trigger.delay",
                                pos=(10, 180),
                                label="Delay",
                                width=120,
                                min_value=0,
                                max_value=2,
                                default_value=0.05,
                                format="%.2f",
                                user_data="trigger.delay",
                                callback=self.change_slider
                            )

                # visual tab
                with dpg.tab(label="Visual"):
                    with dpg.tab_bar():
                        # enemy tab
                        with dpg.tab(label="Enemy"):
                            
                            # bone
                            dpg.add_checkbox(
                                tag="esp.enemy.bone",
                                pos=(10, 90),
                                label="Bone",
                                user_data="esp.enemy.bone",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.enemy.bone.color",
                                pos=(120, 90),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["enemy"]["bone"]["color"].values()),
                                user_data="esp.enemy.bone.color",
                                callback=self.change_color
                            )

                            dpg.add_slider_float(
                                tag="esp.enemy.bone.thick",
                                pos=(220, 90),
                                label="Thick",
                                width=120,
                                min_value=1,
                                max_value=3,
                                default_value=2,
                                format="%.1f",
                                user_data="esp.enemy.bone.thick",
                                callback=self.change_slider
                            )

                            # line
                            dpg.add_checkbox(
                                tag="esp.enemy.line",
                                pos=(10, 120),
                                label="Line",
                                user_data="esp.enemy.line",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.enemy.line.color",
                                pos=(120, 120),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["enemy"]["line"]["color"].values()),
                                user_data="esp.enemy.line.color",
                                callback=self.change_color
                            )

                            dpg.add_slider_float(
                                tag="esp.enemy.line.thick",
                                pos=(220, 120),
                                label="Thick",
                                width=120,
                                min_value=0.5,
                                max_value=3,
                                default_value=1,
                                format="%.1f",
                                user_data="esp.enemy.line.thick",
                                callback=self.change_slider
                            )

                            # box
                            dpg.add_checkbox(
                                tag="esp.enemy.box",
                                pos=(10, 150),
                                label="Box",
                                user_data="esp.enemy.box",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.enemy.box.color",
                                pos=(120, 150),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["enemy"]["box"]["color"].values()),
                                user_data="esp.enemy.box.color",
                                callback=self.change_color
                            )

                            dpg.add_combo(
                                tag="esp.enemy.box.style",
                                pos=(220, 150),
                                label="Style",
                                width=120,
                                items=["normal", "corner"],
                                default_value="normal",
                                user_data="esp.enemy.box.style",
                                callback=self.change_combo
                            )

                            # name
                            dpg.add_checkbox(
                                tag="esp.enemy.name",
                                pos=(10, 180),
                                label="Name",
                                user_data="esp.enemy.name",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.enemy.name.color",
                                pos=(120, 180),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["enemy"]["name"]["color"].values()),
                                user_data="esp.enemy.name.color",
                                callback=self.change_color
                            )

                            # weapon
                            dpg.add_checkbox(
                                tag="esp.enemy.weapon",
                                pos=(10, 210),
                                label="Weapon",
                                user_data="esp.enemy.weapon",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.enemy.weapon.color",
                                pos=(120, 210),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["enemy"]["weapon"]["color"].values()),
                                user_data="esp.enemy.weapon.color",
                                callback=self.change_color
                            )

                            # health
                            dpg.add_checkbox(
                                tag="esp.enemy.health",
                                pos=(10, 240),
                                label="Health",
                                user_data="esp.enemy.health",
                                callback=self.change_state
                            )

                            # armor
                            dpg.add_checkbox(
                                tag="esp.enemy.armor",
                                pos=(10, 270),
                                label="Armor",
                                user_data="esp.enemy.armor",
                                callback=self.change_state
                            )

                        # friend tab
                        with dpg.tab(label="Friend"):
                            
                            # bone
                            dpg.add_checkbox(
                                tag="esp.friend.bone",
                                pos=(10, 90),
                                label="Bone",
                                user_data="esp.friend.bone",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.friend.bone.color",
                                pos=(120, 90),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["friend"]["bone"]["color"].values()),
                                user_data="esp.friend.bone.color",
                                callback=self.change_color
                            )

                            dpg.add_slider_float(
                                tag="esp.friend.bone.thick",
                                pos=(220, 90),
                                label="Thick",
                                width=120,
                                min_value=0.1,
                                max_value=5,
                                default_value=1.0,
                                format="%.1f"
                            )

                            # line
                            dpg.add_checkbox(
                                tag="esp.friend.line",
                                pos=(10, 120),
                                label="Line",
                                user_data="esp.friend.line",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.friend.line.color",
                                pos=(120, 120),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["friend"]["line"]["color"].values()),
                                user_data="esp.friend.line.color",
                                callback=self.change_color
                            )

                            dpg.add_slider_float(
                                tag="esp.friend.line.thick",
                                pos=(220, 120),
                                label="Thick",
                                width=120,
                                min_value=0.1,
                                max_value=5,
                                default_value=1.0,
                                format="%.1f"
                            )

                            # box
                            dpg.add_checkbox(
                                tag="esp.friend.box",
                                pos=(10, 150),
                                label="Box",
                                user_data="esp.friend.box",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.friend.box.color",
                                pos=(120, 150),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["friend"]["box"]["color"].values()),
                                user_data="esp.friend.box.color",
                                callback=self.change_color
                            )

                            dpg.add_combo(
                                tag="esp.friend.box.style",
                                pos=(220, 150),
                                label="Style",
                                width=120,
                                items=["normal", "corner"],
                                default_value="normal",
                                user_data="esp.friend.box.style",
                                callback=self.change_combo
                            )

                            # name
                            dpg.add_checkbox(
                                tag="esp.friend.name",
                                pos=(10, 180),
                                label="Name",
                                user_data="esp.friend.name",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.friend.name.color",
                                pos=(120, 180),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["friend"]["name"]["color"].values()),
                                user_data="esp.friend.name.color",
                                callback=self.change_color
                            )

                            # weapon
                            dpg.add_checkbox(
                                tag="esp.friend.weapon",
                                pos=(10, 210),
                                label="Weapon",
                                user_data="esp.friend.weapon",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.friend.weapon.color",
                                pos=(120, 210),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.esp["friend"]["weapon"]["color"].values()),
                                user_data="esp.friend.weapon.color",
                                callback=self.change_color
                            )

                            # health
                            dpg.add_checkbox(
                                tag="esp.friend.health",
                                pos=(10, 240),
                                label="Health",
                                user_data="esp.friend.health",
                                callback=self.change_state
                            )

                            # armor
                            dpg.add_checkbox(
                                tag="esp.friend.armor",
                                pos=(10, 270),
                                label="Armor",
                                user_data="esp.friend.armor",
                                callback=self.change_state
                            )
                        
                        # other tab
                        with dpg.tab(label="Other"):
                            
                            dpg.add_checkbox(
                                tag="esp.other.crosshair",
                                pos=(10, 90),
                                label="Crosshair",
                                user_data="crosshair",
                                callback=self.change_state
                            )

                            dpg.add_color_edit(
                                tag="esp.other.crosshair.color",
                                pos=(120, 90),
                                label="Color",
                                no_alpha=True,
                                no_inputs=True,
                                no_tooltip=True,
                                no_options=True,
                                default_value=list(Config.crosshair["color"].values()),
                                user_data="crosshair.color",
                                callback=self.change_color
                            )

                # misc tab
                with dpg.tab(label="Misc"):
                    
                    dpg.add_checkbox(
                        tag="misc.ignore_team",
                        pos=(10, 60),
                        label="Ignore Team",
                        user_data="ignore_team",
                        callback=self.change_state
                    )

                # config tab
                with dpg.tab(label="Config"):

                    with dpg.tab_bar():

                        with dpg.tab(label="Setup"):
                            
                            dpg.add_combo(
                                pos=(10, 90),
                                label="Config",
                                width=140,
                                items=["slot1", "slot2", "slot3", "slot4", "slot5"],
                                default_value="slot1",
                                user_data="config.slot",
                                callback=self.change_combo
                            )
                            
                            dpg.add_button(
                                pos=(10, 120),
                                label="Load",
                                width=66,
                                callback=self.load_config
                            )

                            dpg.add_button(
                                pos=(84, 120),
                                label="Save",
                                width=66,
                                callback=self.save_config
                            )

                            dpg.add_button(
                                pos=(10, 150),
                                label="Open Directory",
                                width=140,
                                callback=lambda: subprocess.Popen(["cmd", "/c", "start", "C:/Fury/config"], creationflags=subprocess.CREATE_NO_WINDOW)
                            )

                        with dpg.tab(label="About"):

                            dpg.add_button(
                                pos=(10, 90),
                                label="Repository",
                                width=140,
                                callback=lambda: subprocess.Popen(["cmd", "/c", "start", "https://github.com/gabsroot/fury"], creationflags=subprocess.CREATE_NO_WINDOW)
                            )

        # create a viewport
        dpg.create_viewport(title=Utils.random_string(10), x_pos=600, y_pos=300, width=self.window_width, height=self.window_height, decorated=False, resizable=False)

    def save_config(self):
        try:
            data = {
                "aimbot": Config.aimbot,
                "trigger": Config.trigger,
                "esp": Config.esp,
                "crosshair": Config.crosshair,
                "misc": Config.misc
            }

            with open(f"C:/Fury/config/{Config.config['slot']}", "w", encoding="utf-8") as config:
                config.write(json.dumps(data, indent=4))

        except:
            ctypes.windll.user32.MessageBoxW(0, "Failed to save this config.", "Error", 0x10)
    
    def load_config(self):
        try:
            if not os.path.exists(f"C:/Fury/config/{Config.config['slot']}"):
                ctypes.windll.user32.MessageBoxW(0, "No settings saved in this slot.", "Error", 0x30)
                return

            with open(f"C:/Fury/config/{Config.config['slot']}", "r", encoding="utf-8") as config:
                data = json.load(config)

            Config.aimbot = data["aimbot"]
            Config.trigger = data["trigger"]
            Config.esp = data["esp"]
            Config.crosshair = data["crosshair"]
            Config.misc = data["misc"]

            # aimbot
            for item in["enable", "only_visible", "draw_fov", "key", "fov", "smooth", "distance"]:
                dpg.set_value(item=f"aimbot.{item}", value=Config.aimbot[item])

            # trigger
            for item in ["enable", "target_chicken", "key", "delay"]:
                dpg.set_value(item=f"trigger.{item}", value=Config.trigger[item])

            # esp
            for entity in ["enemy", "friend"]:
                dpg.set_value(item=f"esp.{entity}.bone", value=Config.esp[entity]["bone"]["enable"])
                dpg.set_value(item=f"esp.{entity}.bone.color", value=list(Config.esp[entity]["bone"]["color"].values()))
                dpg.set_value(item=f"esp.{entity}.bone.thick", value=Config.esp[entity]["bone"]["thick"])

                dpg.set_value(item=f"esp.{entity}.line", value=Config.esp[entity]["line"]["enable"])
                dpg.set_value(item=f"esp.{entity}.line.color", value=list(Config.esp[entity]["line"]["color"].values()))
                dpg.set_value(item=f"esp.{entity}.line.thick", value=Config.esp[entity]["line"]["thick"])

                dpg.set_value(item=f"esp.{entity}.box", value=Config.esp[entity]["box"]["enable"])
                dpg.set_value(item=f"esp.{entity}.box.color", value=list(Config.esp[entity]["box"]["color"].values()))
                dpg.set_value(item=f"esp.{entity}.box.style", value=Config.esp[entity]["box"]["style"])

                dpg.set_value(item=f"esp.{entity}.name", value=Config.esp[entity]["name"]["enable"])
                dpg.set_value(item=f"esp.{entity}.name.color", value=list(Config.esp[entity]["name"]["color"].values()))

                dpg.set_value(item=f"esp.{entity}.weapon", value=Config.esp[entity]["weapon"]["enable"])
                dpg.set_value(item=f"esp.{entity}.weapon.color", value=list(Config.esp[entity]["weapon"]["color"].values()))

                dpg.set_value(item=f"esp.{entity}.health", value=Config.esp[entity]["health"]["enable"])
                dpg.set_value(item=f"esp.{entity}.armor", value=Config.esp[entity]["armor"]["enable"])

            # crosshair
            dpg.set_value(item="esp.other.crosshair", value=Config.crosshair["enable"])
            dpg.set_value(item="esp.other.crosshair.color", value=list(Config.crosshair["color"].values()))
            
            # misc
            dpg.set_value(item="misc.ignore_team", value=Config.misc["ignore_team"])
        except:
            ctypes.windll.user32.MessageBoxW(0, "Failed to load this config.", "Error", 0x10)

    def set_items_theme(self):
        for item in dpg.get_all_items():
            item_type = dpg.get_item_info(item)["type"]

            if item_type == "mvAppItemType::mvCheckbox":
                dpg.bind_item_theme(item, Theme.checkbox())

            elif item_type == "mvAppItemType::mvCombo":
                dpg.bind_item_theme(item, Theme.combo())
            
            elif item_type in ["mvAppItemType::mvSliderInt", "mvAppItemType::mvSliderFloat"]:
                dpg.bind_item_theme(item, Theme.slider())

            elif item_type == "mvAppItemType::mvButton":
                dpg.bind_item_theme(item, Theme.button())

            elif item_type == "mvAppItemType::mvInputText":
                dpg.bind_item_theme(item, Theme.input())

            elif item_type == "mvAppItemType::mvColorEdit":
                dpg.bind_item_theme(item, Theme.color_picker())

    def change_state(self, sender, app_data, user_data):
        data = user_data.split(".")

        # aimbot
        if data[0] == "aimbot":
            if len(data) == 1:
                Config.aimbot["enable"] = dpg.get_value(sender)
            
            elif data[1] in Config.aimbot:
                Config.aimbot[data[1]] = dpg.get_value(sender)

        # trigger
        elif data[0] == "trigger":
            if len(data) == 1:
                Config.trigger["enable"] = dpg.get_value(sender)
            
            elif data[1] in Config.trigger:
                Config.trigger[data[1]] = dpg.get_value(sender)

        # esp
        elif data[0] == "esp":
            if len(data) > 2 and data[1] in Config.esp and data[2] in Config.esp[data[1]]:
                Config.esp[data[1]][data[2]]["enable"] = dpg.get_value(sender)

        # crosshair
        elif data[0] == "crosshair":
            Config.crosshair["enable"] = dpg.get_value(sender)

        # ignore_team
        elif data[0] == "ignore_team":
            Config.misc["ignore_team"] = dpg.get_value(sender)

    def change_combo(self, sender, app_data, user_data):
        data = user_data.split(".")

        # aimbot
        if data[0] == "aimbot":
            if len(data) == 2 and data[1] in Config.aimbot:
                Config.aimbot[data[1]] = dpg.get_value(sender)

        # trigger
        elif data[0] == "trigger":
            if len(data) == 2 and data[1] in Config.trigger:
                Config.trigger[data[1]] = dpg.get_value(sender)

        # esp
        elif data[0] == "esp":
            if len(data) > 2 and data[1] in Config.esp and data[2] in Config.esp[data[1]]:
                Config.esp[data[1]][data[2]]["style"] = dpg.get_value(sender)

        # config
        elif data[0] == "config":
            Config.config["slot"] = dpg.get_value(sender)

    def change_slider(self, sender, app_data, user_data):
        data = user_data.split(".")

        # aimbot
        if data[0] == "aimbot":
            if len(data) == 1:
                Config.aimbot["fov"] = dpg.get_value(sender)
            elif len(data) == 2 and data[1] in Config.aimbot:
                Config.aimbot[data[1]] = dpg.get_value(sender)

        # trigger
        elif data[0] == "trigger":
            if len(data) == 1:
                Config.trigger["delay"] = dpg.get_value(sender)
            elif len(data) == 2 and data[1] in Config.trigger:
                Config.trigger[data[1]] = dpg.get_value(sender)

        # esp
        elif data[0] == "esp":
            if len(data) > 2 and data[1] in Config.esp and data[2] in Config.esp[data[1]]:
                Config.esp[data[1]][data[2]]["thick"] = dpg.get_value(sender)

    def change_color(self, sender, app_data, user_data):
        value = dpg.get_value(sender)
        color = {"r": int(value[0]), "g": int(value[1]), "b": int(value[2]), "a": int(value[3])}
        data = user_data.split(".")

        # esp
        if len(data) == 4:
            Config.esp[data[1]][data[2]][data[3]] = color

        # crosshair
        elif data[0] == "crosshair":
            Config.crosshair["color"] = color

    def run(self):
        dpg.setup_dearpygui()
        
        self.set_items_theme()

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
