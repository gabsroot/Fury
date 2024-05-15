from core.offsets import Offsets
from core.trigger import TriggerBot
from core.noflash import NoFlash
from core.bunnyhop import BunnyHop
from core.antiaim import AntiAim
from core.config import Config
from core.esp import ESP
from core.utils import Utils
from threading import Thread
import dearpygui.dearpygui as dpg
import pyMeow as pm
import os

class Fury:
    def __init__(self):
        self.windowWidth = 520
        self.windowHeight = 350
        self.config = Config()
        self.util = Utils()

        try:
            self.process = pm.open_process("cs2.exe")
            self.module = pm.get_module(self.process, "client.dll")["base"]
        except:
            self.util.ShowMessageBox("Warning", "The process cs2.exe is not running. Please open Counter-Strike 2, and run it again.", 0x30)
            os._exit(0)

        # default config
        self.setup = {
            "esp": {
                "bone": {
                    "enable": False,
                    "thick": 1.8,
                    "color": "yellow"
                },
                "boneShadow": {
                    "enable": False,
                    "thick": 2.8,
                    "color": "black"
                },
                "box": {
                    "enable": False,
                    "rounded": 0.3,
                    "color": "blue"
                },
                "line": {
                    "enable": False,
                    "thick": 1.2,
                    "color": "red"
                },
                "name": {
                    "enable": False,
                    "color": "blue"
                },
                "health": {
                    "enable": False
                },
                "armor": {
                    "enable": False
                }
            },
            "triggerBot": {
                "enable": False,
                "delay": 0.05,
                "bind": False,
                "key": "shift",
                "targetChicken": False
            },
            "hvh": {
                "antiAim": {
                    "pitch": {
                        "status": False,
                        "value": 0
                    },
                    "jitter": {
                        "status": False,
                        "speed": 0
                    }
                }
            },
            "misc": {
                "ignoreTeam": {
                    "enable": False
                },
                "bunnyHop": {
                    "enable": False,
                    "jumping": False
                },
                "noFlash": {
                    "enable": False
                },
                "fieldOfVision": {
                    "value": 0.0
                }
            },
            "color": {
                "list": ["Red", "Green", "Blue", "White", "Black", "Yellow", "Cyan", "Purple"],
                "value": {
                    "red": pm.get_color("#bd2045"),
                    "green": pm.get_color("#15e007"),
                    "blue": pm.get_color("#0794e0"),
                    "white": pm.get_color("#d4d4d4"),
                    "black": pm.get_color("#0f0f0f"),
                    "yellow": pm.get_color("#b8bd33"),
                    "cyan": pm.get_color("#33babd"),
                    "purple": pm.get_color("#9244eb")
                }
            },
            "config": {
                "slot": "slot1",
                "file": os.path.join(os.getenv("LOCALAPPDATA"), "slot1")
            }
        }

        Thread(target=self.CreateOverlay, daemon=True).start()

    def InitializeDPG(self):
        dpg.create_context()
        dpg.create_viewport()

        with dpg.handler_registry():
            # Set the font
            with dpg.font_registry():
                dpg.bind_font(dpg.add_font(self.util.LoadFont(), 16)) 

            # Set the theme
            dpg.bind_theme(self.util.LoadTheme())

            # Drag the window
            dpg.add_mouse_drag_handler(button=0, threshold=0.0, callback=self.util.DragWindow)

    def MainWindow(self):
        with dpg.window(label="", width=self.windowWidth, height=self.windowHeight, no_collapse=True, no_move=True, no_resize=True, no_close=True):
            with dpg.tab_bar():
                with dpg.tab(label="Visual"):
                    # Visual tab
                    dpg.add_checkbox(pos=(10, 60), label="Bone", tag="checkbox[bone]", default_value=self.setup["esp"]["bone"]["enable"], callback=self.ChangeESPBone)
                    dpg.add_combo(pos=(150, 60), label="Color", tag="combo[bone][color]", width=100, items=self.setup["color"]["list"], default_value=self.setup["esp"]["bone"]["color"].capitalize(), show=self.setup["esp"]["bone"]["enable"], callback=self.ChangeESPBoneColor)
                    dpg.add_slider_float(pos=(310, 60), label="Thick", tag="slider[bone][thick]", width=130, min_value=1, max_value=5, default_value=self.setup["esp"]["bone"]["thick"], clamped=True, format="%.1f", show=self.setup["esp"]["bone"]["enable"], callback=self.ChangeESPBoneThick)

                    dpg.add_checkbox(pos=(10, 90), label="Bone Shadow", tag="checkbox[boneShadow]", default_value=False, callback=self.ChangeESPBoneShadow)
                    dpg.add_combo(pos=(150, 90), label="Color", tag="combo[boneShadow][color]", width=100, items=self.setup["color"]["list"], default_value=self.setup["esp"]["boneShadow"]["color"].capitalize(), show=self.setup["esp"]["boneShadow"]["enable"], callback=self.ChangeESPBoneShadowColor)
                    dpg.add_slider_float(pos=(310, 90), label="Thick", tag="slider[boneShadow][thick]", width=130, min_value=1, max_value=5, default_value=self.setup["esp"]["boneShadow"]["thick"], clamped=True, format="%.1f", show=self.setup["esp"]["boneShadow"]["enable"], callback=self.ChangeESPBoneShadowThick)

                    dpg.add_checkbox(pos=(10, 120), label="Box", tag="checkbox[box]", default_value=False, callback=self.ChangeESPBox)
                    dpg.add_combo(pos=(150, 120), label="Color", tag="combo[box][color]", width=100, items=self.setup["color"]["list"], default_value=self.setup["esp"]["box"]["color"].capitalize(), show=self.setup["esp"]["box"]["enable"], callback=self.ChangeESPBoxColor)
                    dpg.add_slider_float(pos=(310, 120), label="Rounded", tag="slider[box][rounded]", width=130, min_value=0.1, max_value=1.0, default_value=self.setup["esp"]["box"]["rounded"], clamped=True, format="%.1f", show=self.setup["esp"]["box"]["enable"], callback=self.ChangeESPBoxRounded)

                    dpg.add_checkbox(pos=(10, 150), label="Line", tag="checkbox[line]", default_value=False, callback=self.ChangeESPLine)
                    dpg.add_combo(pos=(150, 150), label="Color", tag="combo[line][color]", width=100, items=self.setup["color"]["list"], default_value=self.setup["esp"]["line"]["color"].capitalize(), show=self.setup["esp"]["line"]["enable"], callback=self.ChangeESPLineColor)
                    dpg.add_slider_float(pos=(310, 150), label="Thick", tag="slider[line][thick]", width=130, min_value=1, max_value=3, default_value=self.setup["esp"]["line"]["thick"], clamped=True, format="%.1f", show=self.setup["esp"]["line"]["enable"], callback=self.ChangeESPLineThick)

                    dpg.add_checkbox(pos=(10, 180), label="Name", tag="checkbox[name]", default_value=False, callback=self.ChangeESPName)
                    dpg.add_combo(pos=(150, 180), label="Color", tag="combo[name][color]", width=100, items=self.setup["color"]["list"], default_value=self.setup["esp"]["name"]["color"].capitalize(), show=self.setup["esp"]["name"]["enable"], callback=self.ChangeESPNameColor)

                    dpg.add_checkbox(pos=(10, 210), label="Health", tag="checkbox[health]", default_value=False, callback=self.ChangeESPHealth)

                    dpg.add_checkbox(pos=(10, 240), label="Armor", tag="checkbox[armor]", default_value=False, callback=self.ChangeESPArmor)
                    
                with dpg.tab(label="Trigger"):
                    # Trigger tab
                    dpg.add_checkbox(pos=(10, 60), label="Enable", tag="checkbox[triggerbot]", default_value=self.setup["triggerBot"]["enable"], callback=self.ChangeTriggerBot)

                    dpg.add_slider_float(pos=(120, 60), label="Delay", tag="slider[triggerBot][delay]", width=130, min_value=0.0, max_value=2, default_value=self.setup["triggerBot"]["delay"], clamped=True, format="%.2f", show=self.setup["triggerBot"]["enable"], callback=self.ChangeTriggerBotDelay)

                    dpg.add_checkbox(pos=(10, 90), label="Keybind", tag="checkbox[triggerBot][keyBind]", default_value=self.setup["triggerBot"]["bind"], show=self.setup["triggerBot"]["enable"], callback=self.ChangeTriggerBotBindKey)

                    dpg.add_combo(pos=(120, 90), label="Key", tag="combo[triggerBot][key]", width=100, items=["ctrl", "shift"], default_value=self.setup["triggerBot"]["key"], show=self.setup["triggerBot"]["bind"], callback=self.ChangeTriggerBotKey)

                    dpg.add_checkbox(pos=(10, 120), label="Target Chicken", tag="checkbox[triggerBot][targetChicken]", default_value=self.setup["triggerBot"]["targetChicken"], show=self.setup["triggerBot"]["enable"], callback=self.ChangeTriggerBotTargetChicken)

                with dpg.tab(label="HvH"):
                    # HvH tab
                    with dpg.tab_bar():
                        with dpg.tab(label="Anti Aim"):
                            # AntiAim tab
                            dpg.add_checkbox(pos=(10, 90), label="Pitch", default_value=self.setup["hvh"]["antiAim"]["pitch"]["status"], callback=self.ChangeHVHAntiAimPitch)

                            dpg.add_slider_int(pos=(140, 90), label="Angle", width=130, min_value=-90, max_value=90, default_value=self.setup["hvh"]["antiAim"]["pitch"]["status"], callback=self.ChangeHVHAntiAimPitchValue)

                            dpg.add_checkbox(pos=(10, 120), label="Jitter", default_value=self.setup["hvh"]["antiAim"]["jitter"]["status"], callback=self.ChangeHVHAntiAimJitter)

                            dpg.add_slider_int(pos=(140, 120), label="Speed", width=130, min_value=-90, max_value=90, default_value=self.setup["hvh"]["antiAim"]["jitter"]["speed"], callback=self.ChangeHVHAntiAimJitterSpeed)


                with dpg.tab(label="Misc"):
                    # Misc tab
                    dpg.add_checkbox(pos=(10, 60), label="Ignore Team", tag="checkbox[ignoreTeam]", default_value=False, callback=self.ChangeMiscIgnoreTeam)

                    dpg.add_checkbox(pos=(10, 90), label="Bunny Hop", tag="checkbox[bunnyHop]", default_value=False, callback=self.ChangeMiscBunnyHop)

                    dpg.add_checkbox(pos=(10, 120), label="No Flash", tag="checkbox[noFlash]", default_value=False, callback=self.ChangeMiscNoFlash)

                    dpg.add_slider_int(pos=(10, 150), label="Fov", tag="slider[fov]", width=130, min_value=0, max_value=160, default_value=self.setup["misc"]["fieldOfVision"]["value"], callback=self.ChangeFieldOfVision)

                with dpg.tab(label="Config"):
                    # Config tab
                    dpg.add_combo(pos=(10, 60), label="Config", width=140, items=["slot1", "slot2", "slot3", "slot4", "slot5"], default_value=self.setup["config"]["slot"], callback=self.ChangeConfigSlot)
                    
                    dpg.add_button(pos=(10, 90), label="Load", width=66, callback=self.LoadConfig)

                    dpg.add_button(pos=(84, 90), label="Save", width=66, callback=lambda: self.config.Save(self.setup["config"]["file"], self))

        # Create the main window
        dpg.create_viewport(x_pos=600, y_pos=300, title=self.util.GenRandomString(10), width=self.windowWidth, height=self.windowHeight, decorated=False, resizable=False)

    def CreateOverlay(self):
        # Start overlay
        pm.overlay_init(target="Counter-Strike 2", title="Counter-Strike 2", fps=144)
        
        bunnyHop = BunnyHop(self)

        # Module execution loop
        while pm.overlay_loop():
            try:
                ESP(self).Update()
                TriggerBot(self).Update()
                NoFlash(self).Update()
                AntiAim(self).Update()
                bunnyHop.Update(self)
            except: pass
    
    def LoadConfig(self):
        # Load a saved config
        config = self.config.Load(file=self.setup["config"]["file"])

        if not config:
            self.util.ShowMessageBox("Error", "This configuration does not exist!", 0x10)
            return

        self.setup = config

        # Update data in UI
        dpg.set_value("checkbox[bone]", value=self.setup["esp"]["bone"]["enable"])
        dpg.set_value("combo[bone][color]", value=self.setup["esp"]["bone"]["color"].capitalize())
        dpg.configure_item("combo[bone][color]", show=self.setup["esp"]["bone"]["enable"])
        dpg.set_value("slider[bone][thick]", value=self.setup["esp"]["bone"]["thick"])
        dpg.configure_item("slider[bone][thick]", show=self.setup["esp"]["bone"]["enable"])
        dpg.set_value("checkbox[boneShadow]", value=self.setup["esp"]["boneShadow"]["enable"])
        dpg.set_value("combo[boneShadow][color]", value=self.setup["esp"]["boneShadow"]["color"].capitalize())
        dpg.configure_item("combo[boneShadow][color]", show=self.setup["esp"]["boneShadow"]["enable"])
        dpg.set_value("slider[boneShadow][thick]", value=self.setup["esp"]["boneShadow"]["thick"])
        dpg.configure_item("slider[boneShadow][thick]", show=self.setup["esp"]["boneShadow"]["enable"])
        dpg.set_value("checkbox[box]", value=self.setup["esp"]["box"]["enable"])
        dpg.set_value("combo[box][color]", value=self.setup["esp"]["box"]["color"].capitalize())
        dpg.configure_item("combo[box][color]", show=self.setup["esp"]["box"]["enable"])
        dpg.set_value("slider[box][rounded]", value=self.setup["esp"]["box"]["rounded"])
        dpg.configure_item("slider[box][rounded]", show=self.setup["esp"]["box"]["enable"])
        dpg.set_value("checkbox[line]", value=self.setup["esp"]["line"]["enable"])
        dpg.set_value("combo[line][color]", value=self.setup["esp"]["line"]["color"].capitalize())
        dpg.configure_item("combo[line][color]", show=self.setup["esp"]["line"]["enable"])
        dpg.set_value("slider[line][thick]", value=self.setup["esp"]["line"]["thick"])
        dpg.configure_item("slider[line][thick]", show=self.setup["esp"]["line"]["enable"])
        dpg.set_value("checkbox[name]", value=self.setup["esp"]["name"]["enable"])
        dpg.set_value("combo[name][color]", value=self.setup["esp"]["name"]["color"].capitalize())
        dpg.configure_item("combo[name][color]", show=self.setup["esp"]["name"]["enable"])
        dpg.set_value("checkbox[health]", value=self.setup["esp"]["health"]["enable"])
        dpg.set_value("checkbox[armor]", value=self.setup["esp"]["armor"]["enable"])
        dpg.set_value("checkbox[triggerbot]", value=self.setup["triggerBot"]["enable"])
        dpg.set_value("slider[triggerBot][delay]", value=self.setup["triggerBot"]["delay"])
        dpg.configure_item("slider[triggerBot][delay]", show=self.setup["triggerBot"]["enable"])
        dpg.configure_item("checkbox[triggerBot][keyBind]", show=self.setup["triggerBot"]["enable"])
        dpg.set_value("checkbox[triggerBot][keyBind]", value=self.setup["triggerBot"]["bind"])
        dpg.set_value("combo[triggerBot][key]", value=self.setup["triggerBot"]["key"])
        dpg.configure_item("combo[triggerBot][key]", show=self.setup["triggerBot"]["bind"])
        dpg.set_value("checkbox[triggerBot][targetChicken]", value=self.setup["triggerBot"]["targetChicken"])
        dpg.configure_item("checkbox[triggerBot][targetChicken]", show=self.setup["triggerBot"]["enable"]) 
        dpg.set_value("checkbox[ignoreTeam]", value=self.setup["misc"]["ignoreTeam"]["enable"])
        dpg.set_value("checkbox[bunnyHop]", value=self.setup["misc"]["bunnyHop"]["enable"])
        dpg.set_value("checkbox[noFlash]", value=self.setup["misc"]["noFlash"]["enable"])
        dpg.set_value("slider[fov]", value=self.setup["misc"]["fieldOfVision"]["value"])
        
    def Run(self):
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    # Change ESP Bone status
    def ChangeESPBone(self, sender):
        self.setup["esp"]["bone"]["enable"] = dpg.get_value(sender)
        dpg.configure_item("combo[bone][color]", show=self.setup["esp"]["bone"]["enable"])
        dpg.configure_item("slider[bone][thick]", show=self.setup["esp"]["bone"]["enable"])

    # Change ESP Bone color
    def ChangeESPBoneColor(self, sender):
        self.setup["esp"]["bone"]["color"] = dpg.get_value(sender).lower()

    # Change ESP Bone thick
    def ChangeESPBoneThick(self, sender):
        self.setup["esp"]["bone"]["thick"] = dpg.get_value(sender)

    # Change ESP Bone Shadow status
    def ChangeESPBoneShadow(self, sender):
        self.setup["esp"]["boneShadow"]["enable"] = dpg.get_value(sender)
        dpg.configure_item("combo[boneShadow][color]", show=self.setup["esp"]["boneShadow"]["enable"])
        dpg.configure_item("slider[boneShadow][thick]", show=self.setup["esp"]["boneShadow"]["enable"])

    # Change ESP Bone Shadow color
    def ChangeESPBoneShadowColor(self, sender):
        self.setup["esp"]["boneShadow"]["color"] = dpg.get_value(sender).lower()

    # Change ESP Bone Shadow thick
    def ChangeESPBoneShadowThick(self, sender):
        self.setup["esp"]["boneShadow"]["thick"] = dpg.get_value(sender)

    # Change ESP Box status
    def ChangeESPBox(self, sender):
        self.setup["esp"]["box"]["enable"] = dpg.get_value(sender)
        dpg.configure_item("combo[box][color]", show=self.setup["esp"]["box"]["enable"])
        dpg.configure_item("slider[box][rounded]", show=self.setup["esp"]["box"]["enable"])

    # Change ESP Box color
    def ChangeESPBoxColor(self, sender):
        self.setup["esp"]["box"]["color"] = dpg.get_value(sender).lower()

    # Change the rounding of the ESP Box
    def ChangeESPBoxRounded(self, sender):
        self.setup["esp"]["box"]["rounded"] = dpg.get_value(sender)

    # Change ESP Line status
    def ChangeESPLine(self, sender):
        self.setup["esp"]["line"]["enable"] = dpg.get_value(sender)
        dpg.configure_item("combo[line][color]", show=self.setup["esp"]["line"]["enable"])
        dpg.configure_item("slider[line][thick]", show=self.setup["esp"]["line"]["enable"])
    
    # Change ESP Line color
    def ChangeESPLineColor(self, sender):
        self.setup["esp"]["line"]["color"] = dpg.get_value(sender).lower()

    # Change ESP Line thick
    def ChangeESPLineThick(self, sender):
        self.setup["esp"]["line"]["thick"] = dpg.get_value(sender)

    # Change ESP Name status
    def ChangeESPName(self, sender):
        self.setup["esp"]["name"]["enable"] = dpg.get_value(sender)
        dpg.configure_item("combo[name][color]", show=self.setup["esp"]["name"]["enable"])

    # Change ESP Name color
    def ChangeESPNameColor(self, sender):
        self.setup["esp"]["name"]["color"] = dpg.get_value(sender).lower()

    # Change ESP Health status
    def ChangeESPHealth(self, sender):
        self.setup["esp"]["health"]["enable"] = dpg.get_value(sender)

    # Change ESP Armor status
    def ChangeESPArmor(self, sender):
        self.setup["esp"]["armor"]["enable"] = dpg.get_value(sender)

    # Change TriggerBot status
    def ChangeTriggerBot(self, sender):
        self.setup["triggerBot"]["enable"] = dpg.get_value(sender)
        dpg.configure_item("slider[triggerBot][delay]", show=self.setup["triggerBot"]["enable"])
        dpg.configure_item("checkbox[triggerBot][keyBind]", show=self.setup["triggerBot"]["enable"])
        dpg.configure_item("combo[triggerBot][key]", show=self.setup["triggerBot"]["enable"])
        dpg.configure_item("checkbox[triggerBot][targetChicken]", show=self.setup["triggerBot"]["enable"])
    
    # Change TriggerBot delay
    def ChangeTriggerBotDelay(self, sender):
        self.setup["triggerBot"]["delay"] = dpg.get_value(sender)

    # Change TriggerBot bind state
    def ChangeTriggerBotBindKey(self, sender):
        self.setup["triggerBot"]["bind"] = dpg.get_value(sender)

    # Change TriggerBot key
    def ChangeTriggerBotKey(self, sender):
        self.setup["triggerBot"]["key"] = dpg.get_value(sender)

    # Change state of the target chicken
    def ChangeTriggerBotTargetChicken(self, sender):
        self.setup["triggerBot"]["targetChicken"] = dpg.get_value(sender)

    # Change AntiAim Pitch state
    def ChangeHVHAntiAimPitch(self, sender):
        self.setup["hvh"]["antiAim"]["pitch"]["status"] = dpg.get_value(sender)

    # Change AntiAim Pitch value
    def ChangeHVHAntiAimPitchValue(self, sender):
        self.setup["hvh"]["antiAim"]["pitch"]["value"] = dpg.get_value(sender)

    # Change AntiAim Jitter/Spin state
    def ChangeHVHAntiAimJitter(self, sender):
        self.setup["hvh"]["antiAim"]["jitter"]["status"] = dpg.get_value(sender)

    # Change AntiAim Jitter/Spin Speed
    def ChangeHVHAntiAimJitterSpeed(self, sender):
        self.setup["hvh"]["antiAim"]["jitter"]["speed"] = dpg.get_value(sender)

    # Change IgnoreTeam state
    def ChangeMiscIgnoreTeam(self, sender):
        self.setup["misc"]["ignoreTeam"]["enable"] = dpg.get_value(sender)

    # Change NoFlash state
    def ChangeMiscNoFlash(self, sender):
        self.setup["misc"]["noFlash"]["enable"] = dpg.get_value(sender)

    # Change BunnyHop state
    def ChangeMiscBunnyHop(self, sender):
        self.setup["misc"]["bunnyHop"]["enable"] = dpg.get_value(sender)

    # Change FieldOfVision state
    def ChangeFieldOfVision(self, sender):
        self.localPlayerController = pm.r_int64(self.process, self.module + Offsets.dwLocalPlayerController)
        self.setup["misc"]["fieldOfVision"]["value"] = dpg.get_value(sender)
        pm.w_int(self.process, self.localPlayerController + Offsets.m_iDesiredFOV, self.setup["misc"]["fieldOfVision"]["value"])

    # Change the config slot
    def ChangeConfigSlot(self, sender):
        self.setup["config"]["file"] = os.path.join(os.getenv("LOCALAPPDATA"), dpg.get_value(sender))

app = Fury()
app.InitializeDPG()
app.MainWindow()
app.Run()