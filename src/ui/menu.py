import pyMeow as pm
import json
from ui.config import *
from ui.materials.components import *

class Content:

    def draw():
        navigation = [Content.legit, Content.visual, Content.misc, Content.config]

        for i, callback in enumerate(navigation):
           if i not in Navigation.done:
               [callback(), Navigation.done.append(i)]

        navigation[Navigation.active]()

    def legit():

        # label aimbot
        pm.draw_font(
            fontId=1,
            text="Aimbot",
            posX=Menu.x + 75,
            posY=Menu.y + 40,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#8d969e")
        )

        # tab aimbot
        pm.draw_rectangle_rounded(
            posX=Menu.x + 70,
            posY=Menu.y + 68,
            width=200,
            height=170,
            roundness=0.05,
            segments=1,
            color=pm.fade_color(pm.get_color("#111316"), 0.99)
        )

        Components.add_switch(
            ref="aimbot_enable",
            text="Enable",
            posX=80,
            posY=80
        )

        Components.add_switch(
            ref="only_spotted",
            text="Only Spotted",
            posX=80,
            posY=105
        )

        Components.add_switch(
            ref="draw_fov",
            text="Draw Fov",
            posX=80,
            posY=130
        )

        Components.add_color_picker(
            ref="fov",
            posX=205,
            posY=131,
            default_color=pm.get_color("white")
        )

        Components.add_slider(
            ref="fov",
            text="Fov",
            posX=80,
            posY=160,
            width=95,
            min_value=0,
            max_value=182,
            fmt=".0f"
        )

        Components.add_slider(
            ref="smooth",
            text="Smooth",
            posX=80,
            posY=185,
            width=95,
            min_value=0,
            max_value=30,
            fmt=".0f"
        )

        Components.add_combo(
            ref="aimbot_keybind",
            label="On Key",
            posX=80,
            posY=205,
            spacing=78,
            items=["none", "ctrl", "shift", "mouse1"]
        )

        # label trigger
        pm.draw_font(
            fontId=1,
            text="Trigger",
            posX=Menu.x + 295,
            posY=Menu.y + 40,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#8d969e")
        )

        # tab trigger
        pm.draw_rectangle_rounded(
            posX=Menu.x + 290,
            posY=Menu.y + 68,
            width=200,
            height=120,
            roundness=0.05,
            segments=1,
            color=pm.fade_color(pm.get_color("#111316"), 0.99)
        )

        Components.add_switch(
            ref="trigger_enable",
            text="Enable",
            posX=300,
            posY=80
        )

        Components.add_switch(
            ref="target_chicken",
            text="Target Chicken",
            posX=300,
            posY=105
        )

        Components.add_slider(
            ref="delay",
            text="Delay",
            posX=300,
            posY=135,
            width=80,
            min_value=0,
            max_value=0.5,
            fmt=".2f"
        )

        Components.add_combo(
            ref="trigger_keybind",
            label="On Key",
            posX=300,
            posY=155,
            spacing=78,
            items=["none", "ctrl", "shift"]
        )

    def visual():

        # label enemy
        pm.draw_font(
            fontId=1,
            text="Enemy",
            posX=Menu.x + 75,
            posY=Menu.y + 40,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#8d969e")
        )

        # tab enemy 1
        pm.draw_rectangle_rounded(
            posX=Menu.x + 70,
            posY=Menu.y + 68,
            width=200,
            height=190,
            roundness=0.05,
            segments=1,
            color=pm.fade_color(pm.get_color("#111316"), 0.99)
        )

        # tab enemy 2
        pm.draw_rectangle_rounded(
            posX=Menu.x + 70,
            posY=Menu.y + 270,
            width=200,
            height=40,
            roundness=0.25,
            segments=1,
            color=pm.fade_color(pm.get_color("#111316"), 0.99)
        )

        Components.add_switch(
            ref="enemy_bone",
            text="Bone",
            posX=80,
            posY=80
        )

        Components.add_color_picker(
            ref="enemy_bone",
            posX=205,
            posY=81,
            default_color=pm.get_color("#fc0362")
        )

        Components.add_switch(
            ref="enemy_box",
            text="Box",
            posX=80,
            posY=105
        )

        Components.add_color_picker(
            ref="enemy_box",
            posX=205,
            posY=106,
            default_color=pm.get_color("#d1c75c")
        )

        Components.add_switch(
            ref="enemy_line",
            text="Line",
            posX=80,
            posY=130
        )

        Components.add_color_picker(
            ref="enemy_line",
            posX=205,
            posY=131,
            default_color=pm.get_color("#b8b8b8")
        )

        Components.add_switch(
            ref="enemy_name",
            text="Name",
            posX=80,
            posY=155
        )

        Components.add_color_picker(
            ref="enemy_name",
            posX=205,
            posY=156,
            default_color=pm.get_color("#e0e0e0")
        )

        Components.add_switch(
            ref="enemy_weapon",
            text="Weapon",
            posX=80,
            posY=180
        )

        Components.add_color_picker(
            ref="enemy_weapon",
            posX=205,
            posY=181,
            default_color=pm.get_color("#fc0362")
        )

        Components.add_switch(
            ref="enemy_health",
            text="Health",
            posX=80,
            posY=205
        )

        Components.add_color_picker(
            ref="enemy_health",
            posX=180,
            posY=206,
            default_color=pm.get_color("#78839c")
        )

        Components.add_color_picker(
            ref="enemy_health_fill",
            posX=205,
            posY=206,
            default_color=pm.get_color("#42d680")
        )

        Components.add_switch(
            ref="enemy_armor",
            text="Armor",
            posX=80,
            posY=230
        )

        Components.add_color_picker(
            ref="enemy_armor",
            posX=180,
            posY=231,
            default_color=pm.get_color("#78839c")
        )

        Components.add_color_picker(
            ref="enemy_armor_fill",
            posX=205,
            posY=231,
            default_color=pm.get_color("#406fcf")
        )

        Components.add_combo(
            ref="enemy_box_style",
            label="Box Style",
            posX=80,
            posY=280,
            spacing=78,
            items=["normal", "corner"]
        )

        # label friend
        pm.draw_font(
            fontId=1,
            text="Friend",
            posX=Menu.x + 295,
            posY=Menu.y + 40,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#8d969e")
        )

        # tab friend 1
        pm.draw_rectangle_rounded(
            posX=Menu.x + 290,
            posY=Menu.y + 68,
            width=200,
            height=190,
            roundness=0.05,
            segments=1,
            color=pm.fade_color(pm.get_color("#111316"), 0.99)
        )

        # tab friend 2
        pm.draw_rectangle_rounded(
            posX=Menu.x + 290,
            posY=Menu.y + 270,
            width=200,
            height=40,
            roundness=0.25,
            segments=1,
            color=pm.fade_color(pm.get_color("#111316"), 0.99)
        )

        Components.add_switch(
            ref="friend_bone",
            text="Bone",
            posX=300,
            posY=80
        )

        Components.add_color_picker(
            ref="friend_bone",
            posX=425,
            posY=81,
            default_color=pm.get_color("#2c8cbf")
        )

        Components.add_switch(
            ref="friend_box",
            text="Box",
            posX=300,
            posY=105
        )

        Components.add_color_picker(
            ref="friend_box",
            posX=425,
            posY=106,
            default_color=pm.get_color("#d1c75c")
        )

        Components.add_switch(
            ref="friend_line",
            text="Line",
            posX=300,
            posY=130
        )

        Components.add_color_picker(
            ref="friend_line",
            posX=425,
            posY=131,
            default_color=pm.get_color("#b8b8b8")
        )

        Components.add_switch(
            ref="friend_name",
            text="Name",
            posX=300,
            posY=155
        )

        Components.add_color_picker(
            ref="friend_name",
            posX=425,
            posY=156,
            default_color=pm.get_color("#e0e0e0")
        )

        Components.add_switch(
            ref="friend_weapon",
            text="Weapon",
            posX=300,
            posY=180
        )

        Components.add_color_picker(
            ref="friend_weapon",
            posX=425,
            posY=181,
            default_color=pm.get_color("#2c8cbf")
        )

        Components.add_switch(
            ref="friend_health",
            text="Health",
            posX=300,
            posY=205
        )

        Components.add_color_picker(
            ref="friend_health",
            posX=400,
            posY=206,
            default_color=pm.get_color("#78839c")
        )

        Components.add_color_picker(
            ref="friend_health_fill",
            posX=425,
            posY=206,
            default_color=pm.get_color("#42d680")
        )

        Components.add_switch(
            ref="friend_armor",
            text="Armor",
            posX=300,
            posY=230
        )

        Components.add_color_picker(
            ref="friend_armor",
            posX=400,
            posY=231,
            default_color=pm.get_color("#78839c")
        )

        Components.add_color_picker(
            ref="friend_armor_fill",
            posX=425,
            posY=231,
            default_color=pm.get_color("#406fcf")
        )

        Components.add_combo(
            ref="friend_box_style",
            label="Box Style",
            posX=300,
            posY=280,
            spacing=78,
            items=["normal", "corner"]
        )

    def misc():

        # label misc
        pm.draw_font(
            fontId=1,
            text="Miscellaneous",
            posX=Menu.x + 75,
            posY=Menu.y + 40,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#8d969e")
        )

        # tab misc
        pm.draw_rectangle_rounded(
            posX=Menu.x + 70,
            posY=Menu.y + 68,
            width=200,
            height=65,
            roundness=0.25,
            segments=1,
            color=pm.fade_color(pm.get_color("#111316"), 0.99)
        )

        Components.add_switch(
            ref="ignore_team",
            text="Ignore Team",
            posX=80,
            posY=80
        )

        Components.add_switch(
            ref="crosshair",
            text="Crosshair",
            posX=80,
            posY=105
        )

        Components.add_color_picker(
            ref="crosshair",
            posX=205,
            posY=105,
            default_color=pm.get_color("#c71844")
        )

    def config():

        # label config
        pm.draw_font(
            fontId=1,
            text="Config",
            posX=Menu.x + 75,
            posY=Menu.y + 40,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#8d969e")
        )

        # tab config
        pm.draw_rectangle_rounded(
            posX=Menu.x + 70,
            posY=Menu.y + 68,
            width=190,
            height=75,
            roundness=0.1,
            segments=1,
            color=pm.fade_color(pm.get_color("#111316"), 0.99)
        )

        Components.add_button(
            ref="load",
            text="Load",
            posX=80,
            posY=80,
            width=80,
            callback=Content.load_config
        )

        Components.add_button(
            ref="save",
            text="Save",
            posX=170,
            posY=80,
            width=80,
            callback=Content.save_config
        )

        Components.add_combo(
            ref="config_slot",
            label="Slot",
            posX=80,
            posY=110,
            width=125,
            spacing=45,
            items=["slot1", "slot2", "slot3", "slot4"]
        )

    def load_config():
        try:
            slot = Combo.queue.get("config_slot")

            if not os.path.exists(f"C:/Fury/{slot}.cfg"):
                Components.add_notification(title="Error", message="No settings saved in this slot", color="#bd355b", show_time=3)
                return

            with open(file=f"C:/Fury/{slot}.cfg", mode="r", encoding="utf-8") as config:
                data = json.load(config)

            # aimbot
            Switch.queue["aimbot_enable"] = data["aimbot"]["enable"]
            Switch.queue["only_spotted"] = data["aimbot"]["only_spotted"]
            Switch.queue["draw_fov"] = data["aimbot"]["draw_fov"]
            ColorPicker.queue["fov"]["color"] = data["aimbot"]["fov"]["color"]
            Slider.queue["fov"] = data["aimbot"]["fov"]["value"]
            Slider.queue["smooth"] = data["aimbot"]["smooth"]
            Combo.queue["aimbot_keybind"] =  data["aimbot"]["keybind"]

            # trigger
            Switch.queue["trigger_enable"] = data["trigger"]["enable"]
            Switch.queue["target_chicken"] = data["trigger"]["target_chicken"]
            Slider.queue["delay"] = data["trigger"]["delay"]
            Combo.queue["trigger_keybind"] =  data["trigger"]["keybind"]

            # esp enemy
            Switch.queue["enemy_bone"] = data["esp"]["enemy"]["bone"]["enable"]
            ColorPicker.queue["enemy_bone"]["color"] = data["esp"]["enemy"]["bone"]["color"]
            Switch.queue["enemy_box"] = data["esp"]["enemy"]["box"]["enable"]
            ColorPicker.queue["enemy_box"]["color"] = data["esp"]["enemy"]["box"]["color"]
            Combo.queue["enemy_box_style"] =  data["esp"]["enemy"]["box"]["style"]
            Switch.queue["enemy_line"] = data["esp"]["enemy"]["line"]["enable"]
            ColorPicker.queue["enemy_line"]["color"] = data["esp"]["enemy"]["line"]["color"]
            Switch.queue["enemy_name"] = data["esp"]["enemy"]["name"]["enable"]
            ColorPicker.queue["enemy_name"]["color"] = data["esp"]["enemy"]["name"]["color"]
            Switch.queue["enemy_weapon"] = data["esp"]["enemy"]["weapon"]["enable"]
            ColorPicker.queue["enemy_weapon"]["color"] = data["esp"]["enemy"]["weapon"]["color"]
            Switch.queue["enemy_health"] = data["esp"]["enemy"]["health"]["enable"]
            ColorPicker.queue["enemy_health"]["color"] = data["esp"]["enemy"]["health"]["color"]
            ColorPicker.queue["enemy_health_fill"]["color"] = data["esp"]["enemy"]["health"]["fill_color"]
            Switch.queue["enemy_armor"] = data["esp"]["enemy"]["armor"]["enable"]
            ColorPicker.queue["enemy_armor"]["color"] = data["esp"]["enemy"]["armor"]["color"]
            ColorPicker.queue["enemy_armor_fill"]["color"] = data["esp"]["enemy"]["armor"]["fill_color"]

            # esp friend
            Switch.queue["friend_bone"] = data["esp"]["friend"]["bone"]["enable"]
            ColorPicker.queue["friend_bone"]["color"] = data["esp"]["friend"]["bone"]["color"]
            Switch.queue["friend_box"] = data["esp"]["friend"]["box"]["enable"]
            ColorPicker.queue["friend_box"]["color"] = data["esp"]["friend"]["box"]["color"]
            Combo.queue["friend_box_style"] =  data["esp"]["friend"]["box"]["style"]
            Switch.queue["friend_line"] = data["esp"]["friend"]["line"]["enable"]
            ColorPicker.queue["friend_line"]["color"] = data["esp"]["friend"]["line"]["color"]
            Switch.queue["friend_name"] = data["esp"]["friend"]["name"]["enable"]
            ColorPicker.queue["friend_name"]["color"] = data["esp"]["friend"]["name"]["color"]
            Switch.queue["friend_weapon"] = data["esp"]["friend"]["weapon"]["enable"]
            ColorPicker.queue["friend_weapon"]["color"] = data["esp"]["friend"]["weapon"]["color"]
            Switch.queue["friend_health"] = data["esp"]["friend"]["health"]["enable"]
            ColorPicker.queue["friend_health"]["color"] = data["esp"]["friend"]["health"]["color"]
            ColorPicker.queue["friend_health_fill"]["color"] = data["esp"]["friend"]["health"]["fill_color"]
            Switch.queue["friend_armor"] = data["esp"]["friend"]["armor"]["enable"]
            ColorPicker.queue["friend_armor"]["color"] = data["esp"]["friend"]["armor"]["color"]
            ColorPicker.queue["friend_armor_fill"]["color"] = data["esp"]["friend"]["armor"]["fill_color"]

            # misc
            Switch.queue["ignore_team"] = data["misc"]["ignore_team"]
            Switch.queue["crosshair"] = data["misc"]["crosshair"]
            ColorPicker.queue["crosshair"]["color"] = data["misc"]["crosshair"]["color"]

            Components.add_notification(title="Success", message="Config loaded successfully", show_time=3)
        except:
            Components.add_notification(title="Error", message="Failed to load configuration", color="#bd355b", show_time=3)

    def save_config():
        try:
            slot = Combo.queue.get("config_slot")

            data = {
                "aimbot": {
                    "enable": Switch.queue.get("aimbot_enable"),
                    "only_spotted": Switch.queue.get("only_spotted"),
                    "draw_fov": Switch.queue.get("draw_fov"),
                    "fov": {
                        "value": Slider.queue.get("fov"),
                        "color": ColorPicker.queue.get("fov", {}).get("color")
                    },
                    "smooth": Slider.queue.get("smooth"),
                    "keybind": Combo.queue.get("aimbot_keybind")
                },
                "trigger": {
                    "enable": Switch.queue.get("trigger_enable"),
                    "target_chicken": Switch.queue.get("target_chicken"),
                    "delay": Slider.queue.get("delay"),
                    "keybind": Combo.queue.get("trigger_keybind")
                },
                "esp": {
                    "enemy": {
                        "bone": {
                            "enable": Switch.queue.get("enemy_bone"),
                            "color": ColorPicker.queue.get("enemy_bone", {}).get("color")
                        },
                        "box": {
                            "enable": Switch.queue.get("enemy_box"),
                            "color": ColorPicker.queue.get("enemy_box", {}).get("color"),
                            "style": Combo.queue.get("enemy_box_style")
                        },
                        "line": {
                            "enable": Switch.queue.get("enemy_line"),
                            "color": ColorPicker.queue.get("enemy_line", {}).get("color")
                        },
                        "name": {
                            "enable": Switch.queue.get("enemy_name"),
                            "color": ColorPicker.queue.get("enemy_name", {}).get("color")
                        },
                        "weapon": {
                            "enable": Switch.queue.get("enemy_weapon"),
                            "color": ColorPicker.queue.get("enemy_weapon", {}).get("color")
                        },
                        "health": {
                            "enable": Switch.queue.get("enemy_health"),
                            "color": ColorPicker.queue.get("enemy_health", {}).get("color"),
                            "fill_color": ColorPicker.queue.get("enemy_health_fill", {}).get("color")
                        },
                        "armor": {
                            "enable": Switch.queue.get("enemy_armor"),
                            "color": ColorPicker.queue.get("enemy_armor", {}).get("color"),
                            "fill_color": ColorPicker.queue.get("enemy_armor_fill", {}).get("color")
                        }
                    },
                    "friend": {
                        "bone": {
                            "enable": Switch.queue.get("friend_bone"),
                            "color": ColorPicker.queue.get("friend_bone", {}).get("color")
                        },
                        "box": {
                            "enable": Switch.queue.get("friend_box"),
                            "color": ColorPicker.queue.get("friend_box", {}).get("color"),
                            "style": Combo.queue.get("friend_box_style")
                        },
                        "line": {
                            "enable": Switch.queue.get("friend_line"),
                            "color": ColorPicker.queue.get("friend_line", {}).get("color")
                        },
                        "name": {
                            "enable": Switch.queue.get("friend_name"),
                            "color": ColorPicker.queue.get("friend_name", {}).get("color")
                        },
                        "weapon": {
                            "enable": Switch.queue.get("friend_weapon"),
                            "color": ColorPicker.queue.get("friend_weapon", {}).get("color")
                        },
                        "health": {
                            "enable": Switch.queue.get("friend_health"),
                            "color": ColorPicker.queue.get("friend_health", {}).get("color"),
                            "fill_color": ColorPicker.queue.get("friend_health_fill", {}).get("color")
                        },
                        "armor": {
                            "enable": Switch.queue.get("friend_armor"),
                            "color": ColorPicker.queue.get("friend_armor", {}).get("color"),
                            "fill_color": ColorPicker.queue.get("friend_armor_fill", {}).get("color")
                        }
                    }
                },
                "misc": {
                    "ignore_team": Switch.queue.get("ignore_team"),
                    "crosshair": {
                        "enable": Switch.queue.get("crosshair"),
                        "color": ColorPicker.queue.get("crosshair", {}).get("color")
                    }
                }
            }

            with open(file=f"C:/Fury/{slot}.cfg", mode="w", encoding="utf-8") as config:
                config.write(json.dumps(data, indent=4))

            Components.add_notification(title="Success", message="Config saved successfully", show_time=3)
        except:
            Components.add_notification(title="Error", message="Failed to save configuration", color="#bd355b", show_time=3)
