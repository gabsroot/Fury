from core.offsets import *
from core.utils import *
import pyMeow as pm

class Entity:
    def __init__(self, entity_controller, entity_pawn, process):
        self.entity_controller = entity_controller
        self.entity_pawn = entity_pawn
        self.process = process

    def health(self):
        return pm.r_int(self.process, self.entity_pawn + m_iHealth)
    
    def armor(self):
        return pm.r_int(self.process, self.entity_pawn + m_ArmorValue)

    def team(self):
        return pm.r_int(self.process, self.entity_pawn + m_iTeamNum)

    def name(self):
        return pm.r_string(self.process, self.entity_controller + m_iszPlayerName)
    
    def weapon(self):
        current = pm.r_int64(self.process, self.entity_pawn + m_pClippingWeapon)

        if current == 0:
            return ""

        index = pm.r_int16(self.process, current + m_AttributeManager + m_Item + m_iItemDefinitionIndex)
        return Utils.get_id("weapon").get(index, "")
    
    def spotted(self):
        return pm.r_bool(self.process, self.entity_pawn + m_entitySpottedState + m_bSpotted)
    
    def ping(self):
        return pm.r_int(self.process, self.entity_controller + m_iPing)
    
    def score(self):
        return pm.r_int(self.process, self.entity_controller + m_iScore)
    
    def pos(self):
        return pm.r_vec3(self.process, self.entity_pawn + m_vOldOrigin)
    
    def bone_pos(self, index):
        scene = pm.r_int64(self.process, self.entity_pawn + m_pGameSceneNode)
        bone = pm.r_int64(self.process, scene + m_pBoneArray)
        return pm.r_vec3(self.process, bone + index * 32)

    def world_to_screen(self, view_matrix):
        try:
            self.pos_2d = pm.world_to_screen(view_matrix, self.pos(), 1)
            self.head_pos_2d = pm.world_to_screen(view_matrix, self.bone_pos(6), 1)
            self.neck = pm.world_to_screen(view_matrix, self.bone_pos(5), 1)
            self.left_feet = pm.world_to_screen(view_matrix, self.bone_pos(27), 1)
            self.right_feet = pm.world_to_screen(view_matrix, self.bone_pos(24), 1)
            self.waist = pm.world_to_screen(view_matrix, self.bone_pos(0), 1)
            self.left_knees = pm.world_to_screen(view_matrix, self.bone_pos(26), 1)
            self.right_knees = pm.world_to_screen(view_matrix, self.bone_pos(23), 1)
            self.left_hand = pm.world_to_screen(view_matrix, self.bone_pos(16), 1)
            self.right_hand = pm.world_to_screen(view_matrix, self.bone_pos(11), 1)
            self.left_arm = pm.world_to_screen(view_matrix, self.bone_pos(14), 1)
            self.right_arm = pm.world_to_screen(view_matrix, self.bone_pos(9), 1)
            self.left_shoulder = pm.world_to_screen(view_matrix, self.bone_pos(13), 1)
            self.right_shoulder = pm.world_to_screen(view_matrix, self.bone_pos(8), 1)
        except:
            return False
        
        return True

class Entities:
    def __init__(self, process, module):
        self.process = process
        self.module = module

    def get_list(self):
        local_player_controller = pm.r_int64(self.process, self.module + dwLocalPlayerController)

        for entity in range(1, 65):
            try:
                entity_list = pm.r_int64(self.process, self.module + dwEntityList)

                entity_entry = pm.r_int64(self.process, entity_list + (8 * (entity & 32767) >> 9) + 16)
                entity_controller = pm.r_int64(self.process, entity_entry + 120 * (entity & 511))

                if entity_controller == local_player_controller:
                    continue
                
                entity_controller_pawn = pm.r_int64(self.process, entity_controller + m_hPlayerPawn)
                entity_list_ptr = pm.r_int64(self.process, entity_list + 8 * ((entity_controller_pawn & 32767) >> 9) + 16)
                entity_pawn = pm.r_int64(self.process, entity_list_ptr + 120 * (entity_controller_pawn & 511))
            except:
                continue

            yield Entity(entity_controller, entity_pawn, self.process)