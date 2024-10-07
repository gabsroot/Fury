from core.offsets import *
from core.utils import *
from time import sleep
import pyMeow as pm
import win32api, win32con, ctypes

class Trigger:
    def __init__(self, process, module):
        self.process = process
        self.module = module

    def update(self, Toogle):
        if not Toogle.data["trigger"]["enable"] or (Toogle.data["trigger"]["key_bind"] and not ctypes.windll.user32.GetAsyncKeyState(Utils.get_id("trigger").get(Toogle.data["trigger"]["key"]))):
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

                if (Toogle.data["misc"]["ignore_team"] or (entity_team != local_player_team) and health > 0) and (Toogle.data["trigger"]["target_chicken"] or entity_team != 0):
                    sleep(Toogle.data["trigger"]["delay"])
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                    sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        except:
            pass