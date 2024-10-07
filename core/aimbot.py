from core.offsets import *
from core.entity import *
from core.utils import *
import pyMeow as pm
import math, ctypes

class Aimbot:
    def __init__(self, process, module):
        self.process = process
        self.module = module
        self.entities = Entities(self.process, self.module)

    def update(self, Toogle):
        if not ctypes.windll.user32.GetAsyncKeyState(Utils.get_id("aimbot").get(Toogle.data["aimbot"]["key"])) or not Toogle.data["aimbot"]["enable"]:
            return
        
        try:
            enemy_pos = None
            best_fov = Toogle.data["aimbot"]["fov"]
            smooth = Toogle.data["aimbot"]["smooth"]

            local_player_pawn = pm.r_int64(self.process, self.module + dwLocalPlayerPawn)
            local_player_controller = pm.r_int64(self.process, self.module + dwLocalPlayerController)
            local_player_team = pm.r_int(self.process, local_player_controller + m_iTeamNum)
            local_player_pos = pm.r_vec3(self.process, local_player_pawn + m_vOldOrigin)
            view_angles = pm.r_vec3(self.process, self.module + dwViewAngles)

            for entity in self.entities.get_list():
                try:
                    if entity.spotted() or not Toogle.data["aimbot"]["only_visible"]:
                        if entity.health() != 0 and entity.team() != local_player_team or Toogle.data["misc"]["ignore_team"]:
                            distance = self.get_distance(local_player_pos, entity.pos())
                            
                            if distance < Toogle.data["aimbot"]["distance"]:
                                angles = self.calc_angle(local_player_pos, entity.pos())
                                fov = self.get_fov(view_angles, angles)

                                if fov < best_fov:
                                    best_fov = fov
                                    enemy_pos = entity.pos()
                except:
                    continue

            if enemy_pos is not None:
                angles = self.calc_angle(local_player_pos, enemy_pos)

                punch_y = pm.r_float(self.process, local_player_pawn + m_aimPunchAngle + 4)
                angles["y"] -= punch_y * 2

                if smooth > 0:
                    angles["y"] = view_angles["y"] + (angles["y"] - view_angles["y"]) / smooth

                pm.w_float(self.process, self.module + dwViewAngles + 4, angles["y"])
        except:
            pass

    def calc_angle(self, local, entity):
        delta = {"x": entity["x"] - local["x"], "y": entity["y"] - local["y"], "z": entity["z"] - local["z"]}
        yaw = math.degrees(math.atan2(delta["y"], delta["x"]))
        return {"x": 0.0, "y": yaw, "z": 0.0}

    def get_distance(self, local, entity):
        return math.sqrt((local["x"] - entity["x"]) ** 2 + (local["y"] - entity["y"]) ** 2 + (local["z"] - entity["z"]) ** 2)

    def get_fov(self, view_angles, target_angles):
        delta = {"x": 0.0, "y": target_angles["y"] - view_angles["y"]}
        return abs(delta["y"])