from core.offsets import Offsets
from time import sleep
import ctypes, win32api, win32con
import pyMeow as pm

class TriggerBot:
    def __init__(self, client):
        self.process = client.process
        self.module = client.module
        self.ignoreTeam = client.setup["misc"]["ignoreTeam"]["enable"]
        self.triggerBot = client.setup["triggerBot"]["enable"]
        self.triggerBotDelay = client.setup["triggerBot"]["delay"]
        self.triggerBotBindKey = client.setup["triggerBot"]["bind"]
        self.triggerBotKey = client.setup["triggerBot"]["key"]
        self.targetChicken = client.setup["triggerBot"]["targetChicken"]

    def Update(self):
        key = {"shift": 16, "ctrl": 17}

        if self.triggerBot and (not self.triggerBotBindKey or ctypes.windll.user32.GetAsyncKeyState(key[self.triggerBotKey])):
            try:
                player = pm.r_int64(self.process, self.module + Offsets.dwLocalPlayerPawn)
                playerTeam = pm.r_int(self.process, player + Offsets.m_iTeamNum)
                entityId = pm.r_int(self.process, player + Offsets.m_iIDEntIndex)

                if entityId > 0:
                    entityList = pm.r_int64(self.process, self.module + Offsets.dwEntityList)
                    entityEntry = pm.r_int64(self.process, entityList + 0x8 * (entityId >> 9) + 0x10)
                    entity = pm.r_int64(self.process, entityEntry + 120 * (entityId & 0x1FF))
                    entityTeam = pm.r_int(self.process, entity + Offsets.m_iTeamNum)
                    health = pm.r_int(self.process, entity + Offsets.m_iHealth)

                    if (self.ignoreTeam or (entityTeam != playerTeam) and health > 0) and (self.targetChicken or entityTeam != 0):
                        sleep(self.triggerBotDelay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                        sleep(0.01)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

                        # pm.w_int(self.process, self.module + Offsets.attack, 67249)
                        # sleep(0.01)
                        # pm.w_int(self.process, self.module + Offsets.attack, 256)
            except:
                pass
