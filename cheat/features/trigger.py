import pyMeow as pm
import win32api, win32con, ctypes
from config import *
from time import sleep
from core.offsets import *

class Trigger:
    def __init__(self, process, module):
        self.process = process
        self.module = module
        self.mapping = {"shift": 16, "ctrl": 17}

    def update(self):

        if not Config.trigger["enable"] or (Config.trigger["key"] != "none" and not ctypes.windll.user32.GetAsyncKeyState(self.mapping.get(Config.trigger["key"]))):
            return

        try:
            local_player_pawn = pm.r_int64(self.process, self.module + dwLocalPlayerPawn)
            local_player_team = pm.r_int(self.process, local_player_pawn + m_iTeamNum)
            entity_id = pm.r_int(self.process, local_player_pawn + m_iIDEntIndex)

            if entity_id > 0:
                entity_list = pm.r_int64(self.process, self.module + dwEntityList)
                entity_entry = pm.r_int64(self.process, entity_list + 8 * (entity_id >> 9) + 16)
                entity = pm.r_int64(self.process, entity_entry + 120 * (entity_id & 511))
                entity_team = pm.r_int(self.process, entity + m_iTeamNum)
                health = pm.r_int(self.process, entity + m_iHealth)

                if (Config.misc["ignore_team"] or (entity_team != local_player_team) and health > 0) and (Config.trigger["target_chicken"] or entity_team != 0):
                    sleep(Config.trigger["delay"])
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                    sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        except:
            pass
