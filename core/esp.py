from core.offsets import *
from core.entity import *
from core.colors import *
import pyMeow as pm

class ESP:
    def __init__(self, process, module):
        self.process = process
        self.module = module
        self.entities = Entities(self.process, self.module)

    def update(self, Toogle):
        try:
            view_matrix = pm.r_floats(self.process, self.module + dwViewMatrix, 16)
            local_player_controller = pm.r_int64(self.process, self.module + dwLocalPlayerController)
            local_player_team = pm.r_int(self.process, local_player_controller + m_iTeamNum)

            for entity in self.entities.get_list():
                if entity.world_to_screen(view_matrix) and entity.health() != 0:
                    box_width = (entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2
                    box_height = (entity.pos_2d["y"] - entity.head_pos_2d["y"]) + (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2

                    # enemy
                    if entity.team() != local_player_team:
                        # box
                        if Toogle.data["esp"]["enemy"]["box"]["enable"]:
                            pm.draw_rectangle_rounded_lines(
                                posX=entity.head_pos_2d["x"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2),
                                posY=entity.head_pos_2d["y"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2,
                                width=box_width,
                                height=box_height,
                                roundness=Toogle.data["esp"]["enemy"]["box"]["rounded"],
                                segments=1,
                                color=colors.get(Toogle.data["esp"]["enemy"]["box"]["color"]),
                                lineThick=1.5
                            )

                        # name
                        if Toogle.data["esp"]["enemy"]["name"]["enable"]:
                            pm.draw_font(
                                fontId=1,
                                text=entity.name().lower() if entity.name() != "" else "unknown",
                                posX=entity.head_pos_2d["x"] - 10,
                                posY=entity.head_pos_2d["y"] + box_height + 5,
                                fontSize=10,
                                spacing=0.0,
                                tint=colors.get(Toogle.data["esp"]["enemy"]["name"]["color"])
                            )
                        
                        # weapon
                        if Toogle.data["esp"]["enemy"]["weapon"]["enable"]:
                            pm.draw_font(
                                fontId=2,
                                text=entity.weapon(),
                                posX=entity.head_pos_2d["x"] - 10,
                                posY=entity.head_pos_2d["y"] + box_height + 15,
                                fontSize=15,
                                spacing=0.0,
                                tint=colors.get(Toogle.data["esp"]["enemy"]["weapon"]["color"])
                            )

                        # line
                        if Toogle.data["esp"]["enemy"]["line"]["enable"]:
                            pm.draw_line(
                                startPosX=pm.get_screen_width() / 2,
                                startPosY=pm.get_screen_height() - 50,
                                endPosX=entity.waist["x"],
                                endPosY=entity.right_feet["y"],
                                color=colors.get(Toogle.data["esp"]["enemy"]["line"]["color"]),
                                thick=Toogle.data["esp"]["enemy"]["line"]["thick"]
                            )

                        # health
                        if Toogle.data["esp"]["enemy"]["health"]:
                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) - 8,
                                posY=entity.head_pos_2d["y"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2 + ((entity.pos_2d["y"] - entity.head_pos_2d["y"]) * 0 / 100),
                                width=3,
                                height=(entity.pos_2d["y"] - entity.head_pos_2d["y"]) + (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2 - ((entity.pos_2d["y"] - entity.head_pos_2d["y"]) * 0 / 100),
                                color=pm.get_color("#db4a56")
                            )

                            # health fill
                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) - 8,
                                posY=entity.head_pos_2d["y"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2 + ((entity.pos_2d["y"] - entity.head_pos_2d["y"]) * (100 - entity.health()) / 100),
                                width=3,
                                height=(entity.pos_2d["y"] - entity.head_pos_2d["y"]) + (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2 - ((entity.pos_2d["y"] - entity.head_pos_2d["y"]) * (100 - entity.health()) / 100),
                                color=pm.get_color("#41e295"),
                            )
                        
                        # shadow
                        if Toogle.data["esp"]["enemy"]["shadow"]["enable"]:
                            [pm.draw_line(startPosX=bone[0], startPosY=bone[1], endPosX=bone[2], endPosY=bone[3], color=colors.get(bone[4]), thick=bone[5]) for bone in [
                                (entity.neck["x"], entity.neck["y"], entity.right_shoulder["x"], entity.right_shoulder["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.neck["x"], entity.neck["y"], entity.left_shoulder["x"], entity.left_shoulder["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_shoulder["x"], entity.left_shoulder["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_shoulder["x"], entity.right_shoulder["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_hand["x"], entity.right_hand["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_hand["x"], entity.left_hand["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.neck["x"], entity.neck["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.left_feet["x"], entity.left_feet["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.right_feet["x"], entity.right_feet["y"], Toogle.data["esp"]["enemy"]["shadow"]["color"], Toogle.data["esp"]["enemy"]["shadow"]["thick"])
                            ]]

                        # bone
                        if Toogle.data["esp"]["enemy"]["bone"]["enable"]:
                            
                            [pm.draw_line(startPosX=bone[0], startPosY=bone[1], endPosX=bone[2], endPosY=bone[3], color=colors.get(bone[4]), thick=bone[5]) for bone in [
                                (entity.neck["x"], entity.neck["y"], entity.right_shoulder["x"], entity.right_shoulder["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.neck["x"], entity.neck["y"], entity.left_shoulder["x"], entity.left_shoulder["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_shoulder["x"], entity.left_shoulder["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_shoulder["x"], entity.right_shoulder["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_hand["x"], entity.right_hand["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_hand["x"], entity.left_hand["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.neck["x"], entity.neck["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.left_feet["x"], entity.left_feet["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.right_feet["x"], entity.right_feet["y"], Toogle.data["esp"]["enemy"]["bone"]["color"], Toogle.data["esp"]["enemy"]["bone"]["thick"])
                            ]]
                    # friend
                    else:
                        # box
                        if Toogle.data["esp"]["friend"]["box"]["enable"]:
                            pm.draw_rectangle_rounded_lines(
                                posX=entity.head_pos_2d["x"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2),
                                posY=entity.head_pos_2d["y"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2,
                                width=box_width,
                                height=box_height,
                                roundness=Toogle.data["esp"]["friend"]["box"]["rounded"],
                                segments=1,
                                color=colors.get(Toogle.data["esp"]["friend"]["box"]["color"]),
                                lineThick=1.5
                            )

                        # name
                        if Toogle.data["esp"]["friend"]["name"]["enable"]:
                            pm.draw_font(
                                fontId=1,
                                text=entity.name().lower() if entity.name() != "" else "unknown",
                                posX=entity.head_pos_2d["x"] - 10,
                                posY=entity.head_pos_2d["y"] + box_height + 5,
                                fontSize=10,
                                spacing=0.0,
                                tint=colors.get(Toogle.data["esp"]["friend"]["name"]["color"])
                            )
                        
                        # weapon
                        if Toogle.data["esp"]["friend"]["weapon"]["enable"]:
                            pm.draw_font(
                                fontId=2,
                                text=entity.weapon(),
                                posX=entity.head_pos_2d["x"] - 10,
                                posY=entity.head_pos_2d["y"] + box_height + 15,
                                fontSize=15,
                                spacing=0.0,
                                tint=colors.get(Toogle.data["esp"]["friend"]["weapon"]["color"])
                            )

                        # line
                        if Toogle.data["esp"]["friend"]["line"]["enable"]:
                            pm.draw_line(
                                startPosX=pm.get_screen_width() / 2,
                                startPosY=pm.get_screen_height() - 50,
                                endPosX=entity.waist["x"],
                                endPosY=entity.right_feet["y"],
                                color=colors.get(Toogle.data["esp"]["friend"]["line"]["color"]),
                                thick=Toogle.data["esp"]["friend"]["line"]["thick"]
                            )

                        # health
                        if Toogle.data["esp"]["friend"]["health"]:
                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) - 8,
                                posY=entity.head_pos_2d["y"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2 + ((entity.pos_2d["y"] - entity.head_pos_2d["y"]) * 0 / 100),
                                width=3,
                                height=(entity.pos_2d["y"] - entity.head_pos_2d["y"]) + (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2 - ((entity.pos_2d["y"] - entity.head_pos_2d["y"]) * 0 / 100),
                                color=pm.get_color("#db4a56")
                            )

                            # health fill
                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) - 8,
                                posY=entity.head_pos_2d["y"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2 + ((entity.pos_2d["y"] - entity.head_pos_2d["y"]) * (100 - entity.health()) / 100),
                                width=3,
                                height=(entity.pos_2d["y"] - entity.head_pos_2d["y"]) + (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2 - ((entity.pos_2d["y"] - entity.head_pos_2d["y"]) * (100 - entity.health()) / 100),
                                color=pm.get_color("#41e295"),
                            )
                        
                        # shadow
                        if Toogle.data["esp"]["friend"]["shadow"]["enable"]:
                            [pm.draw_line(startPosX=bone[0], startPosY=bone[1], endPosX=bone[2], endPosY=bone[3], color=colors.get(bone[4]), thick=bone[5]) for bone in [
                                (entity.neck["x"], entity.neck["y"], entity.right_shoulder["x"], entity.right_shoulder["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.neck["x"], entity.neck["y"], entity.left_shoulder["x"], entity.left_shoulder["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_shoulder["x"], entity.left_shoulder["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_shoulder["x"], entity.right_shoulder["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_hand["x"], entity.right_hand["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_hand["x"], entity.left_hand["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.neck["x"], entity.neck["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.left_feet["x"], entity.left_feet["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.right_feet["x"], entity.right_feet["y"], Toogle.data["esp"]["friend"]["shadow"]["color"], Toogle.data["esp"]["friend"]["shadow"]["thick"])
                            ]]

                        # bone
                        if Toogle.data["esp"]["friend"]["bone"]["enable"]:
                            [pm.draw_line(startPosX=bone[0], startPosY=bone[1], endPosX=bone[2], endPosY=bone[3], color=colors.get(bone[4]), thick=bone[5]) for bone in [
                                (entity.neck["x"], entity.neck["y"], entity.right_shoulder["x"], entity.right_shoulder["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.neck["x"], entity.neck["y"], entity.left_shoulder["x"], entity.left_shoulder["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_shoulder["x"], entity.left_shoulder["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_shoulder["x"], entity.right_shoulder["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_hand["x"], entity.right_hand["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_hand["x"], entity.left_hand["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.neck["x"], entity.neck["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.waist["x"], entity.waist["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.left_feet["x"], entity.left_feet["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.right_feet["x"], entity.right_feet["y"], Toogle.data["esp"]["friend"]["bone"]["color"], Toogle.data["esp"]["friend"]["bone"]["thick"])
                            ]]
        except:
            pass

        pm.end_drawing()