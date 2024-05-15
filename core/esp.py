from core.offsets import Offsets
from core.entity import Entity
import pyMeow as pm

class ESP:
    def __init__(self, client):
        self.process = client.process
        self.module = client.module
        self.ignoreTeam = client.setup["misc"]["ignoreTeam"]["enable"]

        self.BOX = {
            "enable": client.setup["esp"]["box"]["enable"],
            "rounded": client.setup["esp"]["box"]["rounded"],
            "color": client.setup["color"]["value"][client.setup["esp"]["box"]["color"]]
        }

        self.HEALTH = {
            "enable": client.setup["esp"]["health"]["enable"],
            "color": pm.get_color("#bd2045")
        }

        self.ARMOR = {
            "enable": client.setup["esp"]["armor"]["enable"],
            "color": pm.get_color("#19376e")
        }

        self.LINE = {
            "enable": client.setup["esp"]["line"]["enable"],
            "thick": client.setup["esp"]["line"]["thick"],
            "color": client.setup["color"]["value"][client.setup["esp"]["line"]["color"]]
        }

        self.BONE_SHADOW = {
            "enable": client.setup["esp"]["boneShadow"]["enable"],
            "thick": client.setup["esp"]["boneShadow"]["thick"],
            "color": client.setup["color"]["value"][client.setup["esp"]["boneShadow"]["color"]]
        }

        self.BONE = {
            "enable": client.setup["esp"]["bone"]["enable"],
            "thick": client.setup["esp"]["bone"]["thick"],
            "color": client.setup["color"]["value"][client.setup["esp"]["bone"]["color"]]
        }

        self.NAME = {
            "enable": client.setup["esp"]["name"]["enable"],
            "color": client.setup["color"]["value"][client.setup["esp"]["name"]["color"]]
        }

    def GetEntityList(self):
        # returns the list of entities
        try:
            self.localPlayerController = pm.r_int64(self.process, self.module + Offsets.dwLocalPlayerController)
            self.localPlayerTeam = pm.r_int(self.process, self.localPlayerController + Offsets.m_iTeamNum)

            entityList = pm.r_int64(self.process, self.module + Offsets.dwEntityList)

            for e in range(1, 65):
                try:
                    entityEntry = pm.r_int64(self.process, entityList + (8 * (e & 0x7FFF) >> 9) + 16)
                    entityController = pm.r_int64(self.process, entityEntry + 120 * (e & 0x1FF))

                    if entityController == self.localPlayerController:
                        continue

                    controllerPawn = pm.r_int64(self.process, entityController + Offsets.m_hPlayerPawn)
                    entityListPtr = pm.r_int64(self.process, entityList + 0x8 * ((controllerPawn & 0x7FFF) >> 9) + 16)
                    entityPawn = pm.r_int64(self.process, entityListPtr + 120 * (controllerPawn & 0x1FF))
                except:
                    continue

                yield Entity(entityController, entityPawn, self.process)
        except:
            pass

    def Update(self):
        # updates ESP entities
        matrix = pm.r_floats(self.process, self.module + Offsets.dwViewMatrix, 16)

        for entity in self.GetEntityList():
            if entity.WorldToScreen(matrix):
                # ignore dead entities
                if entity.Health() <= 0:
                    continue

                # ignore my team
                if not self.ignoreTeam and (entity.Team() == self.localPlayerTeam):
                    continue
                
                try:
                    # ESP Box
                    if self.BOX["enable"]:
                        pm.draw_rectangle_rounded_lines(entity.headPos2d["x"] - (((entity.pos2d["y"] - entity.headPos2d["y"]) / 2) / 2), entity.headPos2d["y"] - (((entity.pos2d["y"] - entity.headPos2d["y"]) / 2) / 2) / 2, ((entity.pos2d["y"] - entity.headPos2d["y"]) / 2), (entity.pos2d["y"] - entity.headPos2d["y"]) + (((entity.pos2d["y"] - entity.headPos2d["y"]) / 2) / 2) / 2, self.BOX["rounded"], 1, self.BOX["color"], 1.5)

                    # ESP Health
                    if self.HEALTH["enable"]:
                        pm.draw_text(str(entity.Health()), entity.pos2d["x"] + 15, entity.headPos2d["y"], 1, self.HEALTH["color"])

                    # ESP Armor
                    if self.ARMOR["enable"]:
                        pm.draw_text(str(entity.Armor()), entity.pos2d["x"] + 15, entity.waist["y"], 1, self.ARMOR["color"])

                    # ESP Line
                    if self.LINE["enable"]:
                        pm.draw_line(pm.get_screen_width() / 2, pm.get_screen_height() - 50, entity.waist["x"], entity.rightFeet["y"], self.LINE["color"], self.LINE["thick"]) # 2 largura

                    # ESP Bone (Shadow)
                    if self.BONE_SHADOW["enable"]:
                        pm.draw_line(entity.neck["x"], entity.neck["y"], entity.rightShoulder["x"], entity.rightShoulder["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.neck["x"], entity.neck["y"], entity.leftShoulder["x"], entity.leftShoulder["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.leftArm["x"], entity.leftArm["y"], entity.leftShoulder["x"], entity.leftShoulder["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.rightArm["x"], entity.rightArm["y"], entity.rightShoulder["x"], entity.rightShoulder["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.rightArm["x"], entity.rightArm["y"], entity.rightHand["x"], entity.rightHand["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.leftArm["x"], entity.leftArm["y"], entity.leftHand["x"], entity.leftHand["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.neck["x"], entity.neck["y"], entity.waist["x"], entity.waist["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.rightKnees["x"], entity.rightKnees["y"], entity.waist["x"], entity.waist["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.leftKnees["x"], entity.leftKnees["y"], entity.waist["x"], entity.waist["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.leftKnees["x"], entity.leftKnees["y"], entity.leftFeet["x"], entity.leftFeet["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])
                        pm.draw_line(entity.rightKnees["x"], entity.rightKnees["y"], entity.rightFeet["x"], entity.rightFeet["y"], self.BONE_SHADOW["color"], self.BONE_SHADOW["thick"])

                    # ESP Bone
                    if self.BONE["enable"]:
                        pm.draw_line(entity.neck["x"], entity.neck["y"], entity.rightShoulder["x"], entity.rightShoulder["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.neck["x"], entity.neck["y"], entity.leftShoulder["x"], entity.leftShoulder["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.leftArm["x"], entity.leftArm["y"], entity.leftShoulder["x"], entity.leftShoulder["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.rightArm["x"], entity.rightArm["y"], entity.rightShoulder["x"], entity.rightShoulder["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.rightArm["x"], entity.rightArm["y"], entity.rightHand["x"], entity.rightHand["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.leftArm["x"], entity.leftArm["y"], entity.leftHand["x"], entity.leftHand["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.neck["x"], entity.neck["y"], entity.waist["x"], entity.waist["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.rightKnees["x"], entity.rightKnees["y"], entity.waist["x"], entity.waist["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.leftKnees["x"], entity.leftKnees["y"], entity.waist["x"], entity.waist["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.leftKnees["x"], entity.leftKnees["y"], entity.leftFeet["x"], entity.leftFeet["y"], self.BONE["color"], self.BONE["thick"])
                        pm.draw_line(entity.rightKnees["x"], entity.rightKnees["y"], entity.rightFeet["x"], entity.rightFeet["y"], self.BONE["color"], self.BONE["thick"])

                    # ESP Name
                    if self.NAME["enable"]:
                        pm.draw_text(entity.Name().lower() if entity.Name() != "" else "unknown", entity.waist["x"] - 10, entity.rightFeet["y"] + 10, 1, self.NAME["color"])
                
                except:
                    pass

        pm.end_drawing()
