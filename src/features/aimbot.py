import pyMeow as pm, math, ctypes
from ui.config import *
from core.offsets import *
from features.entity import *

class Aimbot:
    def __init__(self, process, module):
        self.process = process
        self.module = module
        self.entities = Entities(process, module)
        self.sw = pm.get_screen_width()
        self.sh = pm.get_screen_height()
        self.keys = {"shift": 0x10, "ctrl": 0x11, "mouse1": 0x01}

    def update(self):
        if not Switch.queue.get("aimbot_enable"):
            return

        if (key := Combo.queue.get("aimbot_keybind")) != "none" and (vk := self.keys.get(key)) is not None and not pm.key_pressed(vKey=vk):
            return

        local_pawn = pm.r_int64(self.process, self.module + dwLocalPlayerPawn)
        
        if not local_pawn:
            return

        local_controller = pm.r_int64(self.process, self.module + dwLocalPlayerController)
        local_team = pm.r_int(self.process, local_controller + m_iTeamNum)

        best_pos = None
        best_fov = float(Slider.queue.get("fov") or 50) / 5.0
        smooth = max(1.0, float(Slider.queue.get("smooth") or 5))

        for entity in self.entities.enumerate():
            try:
                if not entity.health() or entity.health() <= 0:
                    continue

                if entity.team() == local_team and not Switch.queue.get("ignore_team"):
                    continue

                if not entity.spotted() and Switch.queue.get("only_spotted"):
                    continue

                pos = entity.bone_pos(6) # head = 6
                fov = self.get_fov(pos)

                if fov < best_fov:
                    best_fov = fov
                    best_pos = pos
            except:
                continue

        if not best_pos:
            return

        view = pm.r_floats(self.process, self.module + dwViewMatrix, 16)
        screen = pm.world_to_screen(view, best_pos, 1)

        if not screen:
            return

        dx = screen["x"] - self.sw / 2
        dy = screen["y"] - self.sh / 2
        mx = int(dx / smooth)
        my = int(dy / smooth)

        if abs(mx) > 1 or abs(my) > 1:
            ctypes.windll.user32.mouse_event(0x0001, mx, my, 0, 0)
            # pm.mouse_move(x=mx, y=my, relative=False)
            
    def get_fov(self, pos):
        view = pm.r_floats(self.process, self.module + dwViewMatrix, 16)
        screen = pm.world_to_screen(view, pos, 1)

        if not screen:
            return 999.0

        dx = screen["x"] - self.sw / 2
        dy = screen["y"] - self.sh / 2

        return math.hypot(dx, dy) / 5
