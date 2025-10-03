import pyMeow as pm, ctypes
from core.offsets import *
from ui.config import *
from time import sleep

class Trigger:
    def __init__(self, process, module):
        self.process = process
        self.module = module
        self.keys = {"shift": 0x10, "ctrl": 0x11}

    def update(self):

        if not Switch.queue.get("trigger_enable"):
            return

        if (key := Combo.queue.get("trigger_keybind")) != "none" and (vk := self.keys.get(key)) is not None and not pm.key_pressed(vKey=vk):
            return

        try:
            local_player_pawn = pm.r_int64(self.process, self.module + dwLocalPlayerPawn)
            local_player_team = pm.r_int(self.process, local_player_pawn + m_iTeamNum)
            entity_id = pm.r_int(self.process, local_player_pawn + m_iIDEntIndex)

            if entity_id > 0:
                entity_list = pm.r_int64(self.process, self.module + dwEntityList)
                entity_entry = pm.r_int64(self.process, entity_list + 8 * (entity_id >> 9) + 16)
                entity = pm.r_int64(self.process, entity_entry + 120 * (entity_id & 0x1FF))
                entity_team = pm.r_int(self.process, entity + m_iTeamNum)
                health = pm.r_int(self.process, entity + m_iHealth)

                if (Switch.queue.get("ignore_team") or (entity_team != local_player_team) and health > 0) and (Switch.queue.get("target_chicken") or entity_team != 0):
                    sleep(Slider.queue.get("delay"))
                    pm.mouse_click(button="left")
        except:
            pass
