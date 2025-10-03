import pyMeow as pm, time, os
from ui.config import *

class Control:

    @staticmethod
    def toggle_menu():
        # https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

        if pm.key_pressed(vKey=0x2D): # insert: 0x2D
            current_time = time.time()

            if current_time - Menu.time > 0.3:
                Menu.show = not Menu.show
                Menu.time = current_time

                pm.toggle_mouse() # block input

    @staticmethod
    def update_mouse():
        pos = pm.mouse_position()
        Mouse.x = pos["x"]
        Mouse.y = pos["y"]

    @staticmethod
    def auto_close():
        if not pm.process_exists(processName="cs2.exe"):
            os._exit(0)

    @staticmethod
    def drag_menu():

        if pm.mouse_pressed() and Menu.show:

            if not Menu.dragging and Menu.x <= Mouse.x <= Menu.x + 510 and Menu.y <= Mouse.y <= Menu.y + 50:
                Menu.dragging = True
                Menu.offset_x = Mouse.x - Menu.x
                Menu.offset_y = Mouse.y - Menu.y

            if Menu.dragging:
                Menu.x = Mouse.x - Menu.offset_x
                Menu.y = Mouse.y - Menu.offset_y

        if not pm.mouse_pressed():
            Menu.dragging = False

    @staticmethod
    def drag_spectators():

        if Switch.queue.get("spectators") and Switch.queue["spectators"] and Menu.show:

            if pm.mouse_pressed():
                
                if not Spectators.dragging and Spectators.x <= Mouse.x <= Spectators.x + 140 and Spectators.y <= Mouse.y <= Spectators.y + 25:
                    Spectators.dragging = True
                    Spectators.offset_x = Mouse.x - Spectators.x
                    Spectators.offset_y = Mouse.y - Spectators.y

                if Spectators.dragging:
                    Spectators.x = Mouse.x - Spectators.offset_x
                    Spectators.y = Mouse.y - Spectators.offset_y

            if not pm.mouse_pressed():
                Spectators.dragging = False
