from core.offsets import Offsets
import pyMeow as pm

class NoFlash:
    def __init__(self, client):
        self.process = client.process
        self.module = client.module
        self.localPlayerPawn = pm.r_int64(self.process, self.module + Offsets.dwLocalPlayerPawn)
        self.noFlash = client.setup["misc"]["noFlash"]["enable"]

    def Update(self):
        pm.w_int(self.process, self.localPlayerPawn + Offsets.m_flFlashMaxAlpha, 0 if self.noFlash else 1132396544)
