import pyMeow as pm
import math, ctypes
from config import *
from core.offsets import *
from cheat.features.entity import *

class Aimbot:
    def __init__(self, process, module):
        self.process = process
        self.module = module
        self.entities = Entities(self.process, self.module)
        self.mapping = {"shift": 16, "ctrl": 17, "mouse_1": 1}

    def update(self):
        
        if not ctypes.windll.user32.GetAsyncKeyState(self.mapping.get(Config.aimbot["key"])) or not Config.aimbot["enable"]:
            return
        
        try:
            entity_pos = None
            fov = Config.aimbot["fov"] / 10
            smooth = Config.aimbot["smooth"]

            local_player_pawn = pm.r_int64(self.process, self.module + dwLocalPlayerPawn)
            local_player_controller = pm.r_int64(self.process, self.module + dwLocalPlayerController)
            local_player_team = pm.r_int(self.process, local_player_controller + m_iTeamNum)
            local_player_pos = pm.r_vec3(self.process, local_player_pawn + m_vOldOrigin)
            view_angles = pm.r_vec3(self.process, self.module + dwViewAngles)

            for entity in self.entities.enumerate():
                try:
                    if entity.spotted() or not Config.aimbot["only_visible"]:
                        if entity.health() != 0 and entity.team() != local_player_team or Config.misc["ignore_team"]:
                            distance = self.get_distance(local_player_pos, entity.pos())
                            
                            if distance < Config.aimbot["distance"]:
                                angles = self.calc_angle(local_player_pos, entity.pos())
                                closest = self.get_fov(view_angles, angles)

                                if closest < fov:
                                    fov = closest
                                    entity_pos = entity.pos()
                except:
                    continue

            if entity_pos is not None:
                angles = self.calc_angle(local_player_pos, entity_pos)
                punch_y = pm.r_float(self.process, local_player_pawn + m_aimPunchAngle + 4)
                angles["x"] -= punch_y * 2

                if smooth > 0:
                    angles["x"] = view_angles["x"] + (angles["x"] - view_angles["x"]) / smooth
                    angles["y"] = view_angles["y"] + (angles["y"] - view_angles["y"]) / smooth
                else:
                    angles["y"] -= punch_y * 2

                pm.w_vec3(self.process, self.module + dwViewAngles, angles)
        except:
            pass

    def calc_angle(self, local, entity):
        delta = {"x": entity["x"] - local["x"], "y": entity["y"] - local["y"], "z": entity["z"] - local["z"]}
        yaw = math.degrees(math.atan2(delta["y"], delta["x"]))
        hyp = math.sqrt(delta["x"] ** 2 + delta["y"] ** 2)
        pitch = -math.degrees(math.atan2(delta["z"], hyp))
        
        return {"x": pitch, "y": yaw, "z": 0.0}

    def get_distance(self, local, entity):
        return math.sqrt((local["x"] - entity["x"]) ** 2 + (local["y"] - entity["y"]) ** 2 + (local["z"] - entity["z"]) ** 2)

    def get_fov(self, view_angles, target):
        delta = {"x": target["x"] - view_angles["x"], "y": target["y"] - view_angles["y"]}
        return math.sqrt(delta["x"] ** 2 + delta["y"] ** 2)
