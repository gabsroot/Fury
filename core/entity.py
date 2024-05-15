from core.offsets import Offsets
import pyMeow as pm

class Entity:
    def __init__(self, entityController, entityPawn, process):
        self.entityController = entityController
        self.entityPawn = entityPawn
        self.process = process

    def Health(self):
        return pm.r_int(self.process, self.entityPawn + Offsets.m_iHealth)
    
    def Armor(self):
        return pm.r_int(self.process, self.entityPawn + Offsets.m_ArmorValue)

    def Team(self):
        return pm.r_int(self.process, self.entityPawn + Offsets.m_iTeamNum)

    def Name(self):
        return pm.r_string(self.process, self.entityController + Offsets.m_iszPlayerName)
    
    def Ping(self):
        return pm.r_int(self.process, self.entityController + Offsets.m_iPing)
    
    def Score(self):
        return pm.r_int(self.process, self.entityController + Offsets.m_iScore)
    
    def Pos(self):
        return pm.r_vec3(self.process, self.entityPawn + Offsets.m_vOldOrigin)

    def Bone(self, index):
        scene = pm.r_int64(self.process, self.entityPawn + Offsets.m_pGameSceneNode)
        bone = pm.r_int64(self.process, scene + 480)
        return pm.r_vec3(self.process, bone + index * 32)

    def WorldToScreen(self, matrix):
        try:
            self.pos2d = pm.world_to_screen(matrix, self.Pos(), 1)
            self.headPos2d = pm.world_to_screen(matrix, self.Bone(6), 1)
            self.neck = pm.world_to_screen(matrix, self.Bone(5), 1)
            self.leftFeet = pm.world_to_screen(matrix, self.Bone(27), 1)
            self.rightFeet = pm.world_to_screen(matrix, self.Bone(24), 1)
            self.waist = pm.world_to_screen(matrix, self.Bone(0), 1)
            self.leftKnees = pm.world_to_screen(matrix, self.Bone(26), 1)
            self.rightKnees = pm.world_to_screen(matrix, self.Bone(23), 1)
            self.leftHand = pm.world_to_screen(matrix, self.Bone(16), 1)
            self.rightHand = pm.world_to_screen(matrix, self.Bone(11), 1)
            self.leftArm = pm.world_to_screen(matrix, self.Bone(14), 1)
            self.rightArm = pm.world_to_screen(matrix, self.Bone(9), 1)
            self.leftShoulder = pm.world_to_screen(matrix, self.Bone(13), 1)
            self.rightShoulder = pm.world_to_screen(matrix, self.Bone(8), 1)
        except:
            return False
        
        return True
