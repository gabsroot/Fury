import pyMeow as pm
from config import *
from core.offsets import *
from core.utils import *
from cheat.features.entity import *

class ESP:
    def __init__(self, process, module):
        self.process = process
        self.module = module
        self.entities = Entities(self.process, self.module)

    def update(self):
        try:
            view_matrix = pm.r_floats(self.process, self.module + dwViewMatrix, 16)
            local_player_controller = pm.r_int64(self.process, self.module + dwLocalPlayerController)
            local_player_team = pm.r_int(self.process, local_player_controller + m_iTeamNum)

            # crosshair
            if Config.crosshair["enable"]:
                pm.draw_circle_lines(
                    centerX=pm.get_screen_width() / 2,
                    centerY=pm.get_screen_height() / 2,
                    radius=3,
                    color=pm.fade_color(Config.crosshair["color"], 0.7)
                )

            # fov
            if Config.aimbot["draw_fov"] and Config.aimbot["enable"]:
                pm.draw_circle_lines(
                    centerX=pm.get_screen_width() / 2,
                    centerY=pm.get_screen_height() / 2,
                    radius=Config.aimbot["fov"],
                    color=pm.fade_color(pm.get_color("#ffffff"), 0.5)
                )
                
            for entity in self.entities.enumerate():
                
                if entity.world_to_screen(view_matrix) and entity.health() != 0:
                    
                    box_x = entity.head_pos_2d["x"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2)
                    box_y = entity.head_pos_2d["y"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2
                    box_width = (entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2
                    box_height = (entity.pos_2d["y"] - entity.head_pos_2d["y"]) + (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2
                    corner_length = min(box_width, box_height) * 0.2
                    name = Utils.normalize_name(entity.name())

                    # enemy
                    if entity.team() != local_player_team:
                        
                        # bone
                        if Config.esp["enemy"]["bone"]["enable"]:
                            [pm.draw_line(startPosX=bone[0], startPosY=bone[1], endPosX=bone[2], endPosY=bone[3], color=pm.fade_color(Config.esp["enemy"]["bone"]["color"], 0.5), thick=Config.esp["enemy"]["bone"]["thick"]) for bone in [
                                (entity.neck["x"], entity.neck["y"], entity.right_shoulder["x"], entity.right_shoulder["y"]),
                                (entity.neck["x"], entity.neck["y"], entity.left_shoulder["x"], entity.left_shoulder["y"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_shoulder["x"], entity.left_shoulder["y"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_shoulder["x"], entity.right_shoulder["y"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_hand["x"], entity.right_hand["y"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_hand["x"], entity.left_hand["y"]),
                                (entity.neck["x"], entity.neck["y"], entity.waist["x"], entity.waist["y"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.waist["x"], entity.waist["y"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.waist["x"], entity.waist["y"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.left_feet["x"], entity.left_feet["y"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.right_feet["x"], entity.right_feet["y"])
                            ]]

                        # line
                        if Config.esp["enemy"]["line"]["enable"]:
                            pm.draw_line(
                                startPosX=pm.get_screen_width() / 2,
                                startPosY=pm.get_screen_height() - 100,
                                endPosX=entity.pos_2d["x"],
                                endPosY=entity.pos_2d["y"],
                                color=pm.fade_color(Config.esp["enemy"]["line"]["color"], 0.5),
                                thick=Config.esp["enemy"]["line"]["thick"]
                            )

                        # box
                        if Config.esp["enemy"]["box"]["enable"]:
                            box_color = pm.fade_color(Config.esp["enemy"]["box"]["color"], 0.5)

                            # normal
                            if Config.esp["enemy"]["box"]["style"] == "normal":
                                pm.draw_rectangle_rounded_lines(
                                    posX=box_x,
                                    posY=box_y,
                                    width=box_width,
                                    height=box_height,
                                    roundness=0.05,
                                    segments=1,
                                    color=box_color,
                                    lineThick=1.2
                                )
                            
                            else:
                                # corner
                                pm.draw_line(box_x, box_y, box_x + corner_length, box_y, box_color, 1.2)
                                pm.draw_line(box_x, box_y, box_x, box_y + corner_length, box_color, 1.2)
                                pm.draw_line(box_x + box_width, box_y, box_x + box_width - corner_length, box_y, box_color, 1.2)
                                pm.draw_line(box_x + box_width, box_y, box_x + box_width, box_y + corner_length, box_color, 1.2)
                                pm.draw_line(box_x, box_y + box_height, box_x + corner_length, box_y + box_height, box_color, 1.2)
                                pm.draw_line(box_x, box_y + box_height, box_x, box_y + box_height - corner_length, box_color, 1.2)
                                pm.draw_line(box_x + box_width, box_y + box_height, box_x + box_width - corner_length, box_y + box_height, box_color, 1.2)
                                pm.draw_line(box_x + box_width, box_y + box_height, box_x + box_width, box_y + box_height - corner_length, box_color, 1.2)

                        # name
                        if Config.esp["enemy"]["name"]["enable"]:
                            pm.draw_font(
                                fontId=1,
                                text=name,
                                posX=entity.head_pos_2d["x"] - ((len(name) * 5) / 2),
                                posY=entity.head_pos_2d["y"] + box_height + 5,
                                fontSize=12,
                                spacing=0,
                                tint=pm.fade_color(Config.esp["enemy"]["name"]["color"], 0.7)
                            )

                        # weapon
                        if Config.esp["enemy"]["weapon"]["enable"]:
                            pm.draw_font(
                                fontId=2,
                                text=entity.weapon(),
                                posX=entity.head_pos_2d["x"] - 10,
                                posY=entity.head_pos_2d["y"] + box_height + 20,
                                fontSize=10,
                                spacing=0.0,
                                tint=pm.fade_color(Config.esp["enemy"]["weapon"]["color"], 0.5)
                            )

                        # health
                        if Config.esp["enemy"]["health"]["enable"]:
                            pm.draw_rectangle(
                                posX=box_x - 8,
                                posY=box_y,
                                width=2,
                                height=box_height,
                                color=pm.fade_color(pm.get_color("#db4a56"), 0.5)
                            )

                            pm.draw_rectangle(
                                posX=box_x - 8,
                                posY=box_y + (box_height * (100 - entity.health()) / 100),
                                width=2,
                                height=box_height * (entity.health() / 100),
                                color=pm.fade_color(pm.get_color("#41e295"), 0.5)
                            )

                        # armor
                        if Config.esp["enemy"]["armor"]["enable"]:
                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (box_width / 2),
                                posY=box_y - 10,
                                width=box_width,
                                height=2,
                                color=pm.fade_color(pm.get_color("#db4a56"), 0.5)
                            )

                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (box_width / 2),
                                posY=box_y - 10,
                                width=box_width * (entity.armor() / 100),
                                height=2,
                                color=pm.fade_color(pm.get_color("#32ace5"), 0.5)
                            )

                    else:
                        # friend

                        # bone
                        if Config.esp["friend"]["bone"]["enable"]:
                            [pm.draw_line(startPosX=bone[0], startPosY=bone[1], endPosX=bone[2], endPosY=bone[3], color=pm.fade_color(Config.esp["friend"]["bone"]["color"], 0.5), thick=Config.esp["friend"]["bone"]["thick"]) for bone in [
                                (entity.neck["x"], entity.neck["y"], entity.right_shoulder["x"], entity.right_shoulder["y"]),
                                (entity.neck["x"], entity.neck["y"], entity.left_shoulder["x"], entity.left_shoulder["y"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_shoulder["x"], entity.left_shoulder["y"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_shoulder["x"], entity.right_shoulder["y"]),
                                (entity.right_arm["x"], entity.right_arm["y"], entity.right_hand["x"], entity.right_hand["y"]),
                                (entity.left_arm["x"], entity.left_arm["y"], entity.left_hand["x"], entity.left_hand["y"]),
                                (entity.neck["x"], entity.neck["y"], entity.waist["x"], entity.waist["y"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.waist["x"], entity.waist["y"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.waist["x"], entity.waist["y"]),
                                (entity.left_knees["x"], entity.left_knees["y"], entity.left_feet["x"], entity.left_feet["y"]),
                                (entity.right_knees["x"], entity.right_knees["y"], entity.right_feet["x"], entity.right_feet["y"])
                            ]]

                        # line
                        if Config.esp["friend"]["line"]["enable"]:
                            pm.draw_line(
                                startPosX=pm.get_screen_width() / 2,
                                startPosY=pm.get_screen_height() - 100,
                                endPosX=entity.pos_2d["x"],
                                endPosY=entity.pos_2d["y"],
                                color=pm.fade_color(Config.esp["friend"]["line"]["color"], 0.5),
                                thick=Config.esp["friend"]["line"]["thick"]
                            )

                        # box
                        if Config.esp["friend"]["box"]["enable"]:
                            box_color = pm.fade_color(Config.esp["friend"]["box"]["color"], 0.5)

                            # normal
                            if Config.esp["friend"]["box"]["style"] == "normal":
                                pm.draw_rectangle_rounded_lines(
                                    posX=box_x,
                                    posY=box_y,
                                    width=box_width,
                                    height=box_height,
                                    roundness=0.05,
                                    segments=1,
                                    color=box_color,
                                    lineThick=1.2
                                )
                            
                            else:
                                # corner
                                pm.draw_line(box_x, box_y, box_x + corner_length, box_y, box_color, 1.2)
                                pm.draw_line(box_x, box_y, box_x, box_y + corner_length, box_color, 1.2)
                                pm.draw_line(box_x + box_width, box_y, box_x + box_width - corner_length, box_y, box_color, 1.2)
                                pm.draw_line(box_x + box_width, box_y, box_x + box_width, box_y + corner_length, box_color, 1.2)
                                pm.draw_line(box_x, box_y + box_height, box_x + corner_length, box_y + box_height, box_color, 1.2)
                                pm.draw_line(box_x, box_y + box_height, box_x, box_y + box_height - corner_length, box_color, 1.2)
                                pm.draw_line(box_x + box_width, box_y + box_height, box_x + box_width - corner_length, box_y + box_height, box_color, 1.2)
                                pm.draw_line(box_x + box_width, box_y + box_height, box_x + box_width, box_y + box_height - corner_length, box_color, 1.2)

                        # name
                        if Config.esp["friend"]["name"]["enable"]:
                            pm.draw_font(
                                fontId=1,
                                text=name,
                                posX=entity.head_pos_2d["x"] - ((len(name) * 5) / 2),
                                posY=entity.head_pos_2d["y"] + box_height + 5,
                                fontSize=12,
                                spacing=0,
                                tint=pm.fade_color(Config.esp["friend"]["name"]["color"], 0.7)
                            )

                        # weapon
                        if Config.esp["friend"]["weapon"]["enable"]:
                            pm.draw_font(
                                fontId=2,
                                text=entity.weapon(),
                                posX=entity.head_pos_2d["x"] - 10,
                                posY=entity.head_pos_2d["y"] + box_height + 20,
                                fontSize=10,
                                spacing=0.0,
                                tint=pm.fade_color(Config.esp["friend"]["weapon"]["color"], 0.5)
                            )

                        # health
                        if Config.esp["friend"]["health"]["enable"]:
                            pm.draw_rectangle(
                                posX=box_x - 8,
                                posY=box_y,
                                width=2,
                                height=box_height,
                                color=pm.fade_color(pm.get_color("#db4a56"), 0.5)
                            )

                            pm.draw_rectangle(
                                posX=box_x - 8,
                                posY=box_y + (box_height * (100 - entity.health()) / 100),
                                width=2,
                                height=box_height * (entity.health() / 100),
                                color=pm.fade_color(pm.get_color("#41e295"), 0.5)
                            )

                        # armor
                        if Config.esp["friend"]["armor"]["enable"]:
                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (box_width / 2),
                                posY=box_y - 10,
                                width=box_width,
                                height=2,
                                color=pm.fade_color(pm.get_color("#db4a56"), 0.5)
                            )

                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (box_width / 2),
                                posY=box_y - 10,
                                width=box_width * (entity.armor() / 100),
                                height=2,
                                color=pm.fade_color(pm.get_color("#32ace5"), 0.5)
                            )
        except:
            pass
