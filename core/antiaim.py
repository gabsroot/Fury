from core.offsets import Offsets
import pyMeow as pm

class AntiAim:
    def __init__(self, client):
        self.process = client.process
        self.module = client.module
        self.antiAim = client.setup["hvh"]["antiAim"]

    def Update(self):
        if self.antiAim["pitch"]["status"] or self.antiAim["jitter"]["status"]:
            angles = pm.r_vec3(self.process, self.module + Offsets.dwViewAngles)

            # pitch
            if self.antiAim["pitch"]["status"]:
                angles["x"] = self.antiAim["pitch"]["value"]
                pm.w_vec3(self.process, self.module + Offsets.dwViewAngles, angles)

            # jitter
            if self.antiAim["jitter"]["status"]:
                angles["y"] += self.antiAim["jitter"]["speed"]
                pm.w_vec3(self.process, self.module + Offsets.dwViewAngles, angles)
