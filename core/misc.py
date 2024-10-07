from core.offsets import *
import pyMeow as pm

class Misc:
    def __init__(self, process, module):
        self.process = process
        self.module = module

    def no_flash(self, Toogle):
        local_player_pawn = pm.r_int64(self.process, self.module + dwLocalPlayerPawn)
        pm.w_int(self.process, local_player_pawn + m_flFlashMaxAlpha, 67589 if Toogle.data["misc"]["no_flash"] else 0)