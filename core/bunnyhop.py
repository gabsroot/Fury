from core.offsets import Offsets
import pyMeow as pm
import ctypes

class BunnyHop:
    def __init__(self, client):
        self.process = client.process
        self.module = client.module
        self.bunnyHop = client.setup["misc"]["bunnyHop"]["enable"]
        self.bunnyJumping = client.setup["misc"]["bunnyHop"]["jumping"]

    def Update(self, client):
        if ctypes.windll.user32.GetAsyncKeyState(0x20) and client.setup["misc"]["bunnyHop"]["enable"]:
            if not self.bunnyJumping:
                pm.w_int(self.process, self.module + Offsets.jump, 889244)
                self.bunnyJumping = True

            elif self.bunnyJumping:
                pm.w_int(self.process, self.module + Offsets.jump, 253)
                self.bunnyJumping = False
