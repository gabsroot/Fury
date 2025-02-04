import pyMeow as pm
from ui.config import *
from core.offsets import *
from core.utils import *
from features.entity import *

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
            if Switch.queue.get("crosshair"):
                # x
                pm.draw_line(
                    startPosX=pm.get_screen_width() / 2 - 5,
                    startPosY=pm.get_screen_height() / 2,
                    endPosX=pm.get_screen_width() / 2 + 5,
                    endPosY=pm.get_screen_height() / 2,
                    color=pm.fade_color(ColorPicker.queue.get("crosshair").get("color"), 0.7),
                    thick=1.7
                )

                # y
                pm.draw_line(
                    startPosX=pm.get_screen_width() / 2,
                    startPosY=pm.get_screen_height() / 2 - 5,
                    endPosX=pm.get_screen_width() / 2,
                    endPosY=pm.get_screen_height() / 2 + 5,
                    color=pm.fade_color(ColorPicker.queue.get("crosshair").get("color"), 0.7),
                    thick=1.7
                )
            
            # fov
            if Switch.queue.get("draw_fov") and Switch.queue.get("aimbot_enable"):
                pm.draw_circle_lines(
                    centerX=pm.get_screen_width() / 2,
                    centerY=pm.get_screen_height() / 2,
                    radius=Slider.queue.get("fov"),
                    color=pm.fade_color(ColorPicker.queue["fov"]["color"], 0.5)
                )
                
            for entity in self.entities.enumerate():
                if entity.world_to_screen(view_matrix) and entity.health() != 0:
                    box_x = entity.head_pos_2d["x"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2)
                    box_y = entity.head_pos_2d["y"] - (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2
                    box_width = (entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2
                    box_height = (entity.pos_2d["y"] - entity.head_pos_2d["y"]) + (((entity.pos_2d["y"] - entity.head_pos_2d["y"]) / 2) / 2) / 2
                    corner_length = min(box_width, box_height) * 0.2
                    name = Utils.clean_text(entity.name())

                    # enemy
                    if entity.team() != local_player_team:

                        # bone
                        if Switch.queue.get("enemy_bone"):

                            [pm.draw_line(startPosX=bone[0], startPosY=bone[1], endPosX=bone[2], endPosY=bone[3], color=pm.fade_color(ColorPicker.queue["enemy_bone"]["color"], 0.7), thick=1.5) for bone in [
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


                        # box
                        if Switch.queue.get("enemy_box"):

                            box_color = pm.fade_color(ColorPicker.queue["enemy_box"]["color"], 0.7)

                            if Combo.queue["enemy_box_style"] == "normal":

                                # normal
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
                                [pm.draw_line(startPosX=line[0], startPosY=line[1], endPosX=line[2], endPosY=line[3], color=box_color, thick=1.2) for line in [
                                    (box_x, box_y, box_x + corner_length, box_y),
                                    (box_x, box_y, box_x, box_y + corner_length),
                                    (box_x + box_width, box_y, box_x + box_width - corner_length, box_y),
                                    (box_x + box_width, box_y, box_x + box_width, box_y + corner_length),
                                    (box_x, box_y + box_height, box_x + corner_length, box_y + box_height),
                                    (box_x, box_y + box_height, box_x, box_y + box_height - corner_length),
                                    (box_x + box_width, box_y + box_height, box_x + box_width - corner_length, box_y + box_height),
                                    (box_x + box_width, box_y + box_height, box_x + box_width, box_y + box_height - corner_length)
                                ]]

                        # line
                        if Switch.queue.get("enemy_line"):

                            pm.draw_line(
                                startPosX=pm.get_screen_width() / 2,
                                startPosY=pm.get_screen_height() - 100,
                                endPosX=entity.pos_2d["x"],
                                endPosY=entity.pos_2d["y"],
                                color=pm.fade_color(ColorPicker.queue["enemy_line"]["color"], 0.7),
                                thick=0.5
                            )

                        # name
                        if Switch.queue.get("enemy_name"):

                            pm.draw_font(
                                fontId=1,
                                text=name,
                                posX=entity.head_pos_2d["x"] - (pm.measure_text(text=name, fontSize=12) / 2),
                                posY=entity.head_pos_2d["y"] + box_height + 5,
                                fontSize=12,
                                spacing=0,
                                tint=pm.fade_color(ColorPicker.queue["enemy_name"]["color"], 0.7)
                            )

                        # weapon
                        if Switch.queue.get("enemy_weapon"):

                            pm.draw_font(
                                fontId=3,
                                text=entity.weapon(),
                                posX=entity.head_pos_2d["x"] - 10,
                                posY=entity.head_pos_2d["y"] + box_height + 20,
                                fontSize=10,
                                spacing=0.0,
                                tint=pm.fade_color(ColorPicker.queue["enemy_weapon"]["color"], 0.7)
                            )

                        # health
                        if Switch.queue.get("enemy_health"):

                            pm.draw_rectangle(
                                posX=box_x - 8,
                                posY=box_y,
                                width=2,
                                height=box_height,
                                color=pm.fade_color(ColorPicker.queue["enemy_health"]["color"], 0.7)
                            )

                            pm.draw_rectangle(
                                posX=box_x - 8,
                                posY=box_y + (box_height * (100 - entity.health()) / 100),
                                width=2,
                                height=box_height * (entity.health() / 100),
                                color=pm.fade_color(ColorPicker.queue["enemy_health_fill"]["color"], 0.7)
                            )

                        # armor
                        if Switch.queue.get("enemy_armor"):

                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (box_width / 2),
                                posY=box_y - 10,
                                width=box_width,
                                height=2,
                                color=pm.fade_color(ColorPicker.queue["enemy_armor_fill"]["color"], 0.7)
                            )

                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (box_width / 2),
                                posY=box_y - 10,
                                width=box_width * (entity.armor() / 100),
                                height=2,
                                color=pm.fade_color(ColorPicker.queue["enemy_armor"]["color"], 0.7)
                            )

                    else: 
                        # friend
                        # bone
                        if Switch.queue.get("friend_bone"):
                            
                            [pm.draw_line(startPosX=bone[0], startPosY=bone[1], endPosX=bone[2], endPosY=bone[3], color=pm.fade_color(ColorPicker.queue["friend_bone"]["color"], 0.7), thick=1.5) for bone in [
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

                        # box
                        if Switch.queue.get("friend_box"):

                            box_color = pm.fade_color(ColorPicker.queue["friend_box"]["color"], 0.7)

                            if Combo.queue["friend_box_style"] == "normal":
                                # normal
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
                                [pm.draw_line(startPosX=line[0], startPosY=line[1], endPosX=line[2], endPosY=line[3], color=box_color, thick=1.2) for line in [
                                    (box_x, box_y, box_x + corner_length, box_y),
                                    (box_x, box_y, box_x, box_y + corner_length),
                                    (box_x + box_width, box_y, box_x + box_width - corner_length, box_y),
                                    (box_x + box_width, box_y, box_x + box_width, box_y + corner_length),
                                    (box_x, box_y + box_height, box_x + corner_length, box_y + box_height),
                                    (box_x, box_y + box_height, box_x, box_y + box_height - corner_length),
                                    (box_x + box_width, box_y + box_height, box_x + box_width - corner_length, box_y + box_height),
                                    (box_x + box_width, box_y + box_height, box_x + box_width, box_y + box_height - corner_length)
                                ]]

                        # line
                        if Switch.queue.get("friend_line"):

                            pm.draw_line(
                                startPosX=pm.get_screen_width() / 2,
                                startPosY=pm.get_screen_height() - 100,
                                endPosX=entity.pos_2d["x"],
                                endPosY=entity.pos_2d["y"],
                                color=pm.fade_color(ColorPicker.queue["friend_line"]["color"], 0.7),
                                thick=0.5
                            )

                        # name
                        if Switch.queue.get("friend_name"):

                            pm.draw_font(
                                fontId=1,
                                text=name,
                                posX=entity.head_pos_2d["x"] - (pm.measure_text(text=name, fontSize=12) / 2),
                                posY=entity.head_pos_2d["y"] + box_height + 5,
                                fontSize=12,
                                spacing=0,
                                tint=pm.fade_color(ColorPicker.queue["friend_name"]["color"], 0.7)
                            )

                        # weapon
                        if Switch.queue.get("friend_weapon"):

                            pm.draw_font(
                                fontId=3,
                                text=entity.weapon(),
                                posX=entity.head_pos_2d["x"] - 10,
                                posY=entity.head_pos_2d["y"] + box_height + 20,
                                fontSize=10,
                                spacing=0.0,
                                tint=pm.fade_color(ColorPicker.queue["friend_weapon"]["color"], 0.7)
                            )

                        # health
                        if Switch.queue.get("friend_health"):

                            pm.draw_rectangle(
                                posX=box_x - 8,
                                posY=box_y,
                                width=2,
                                height=box_height,
                                color=pm.fade_color(ColorPicker.queue["friend_health"]["color"], 0.7)
                            )

                            pm.draw_rectangle(
                                posX=box_x - 8,
                                posY=box_y + (box_height * (100 - entity.health()) / 100),
                                width=2,
                                height=box_height * (entity.health() / 100),
                                color=pm.fade_color(ColorPicker.queue["friend_health_fill"]["color"], 0.7)
                            )

                        # armor
                        if Switch.queue.get("friend_armor"):

                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (box_width / 2),
                                posY=box_y - 10,
                                width=box_width,
                                height=2,
                                color=pm.fade_color(ColorPicker.queue["friend_armor_fill"]["color"], 0.7)
                            )

                            pm.draw_rectangle(
                                posX=entity.head_pos_2d["x"] - (box_width / 2),
                                posY=box_y - 10,
                                width=box_width * (entity.armor() / 100),
                                height=2,
                                color=pm.fade_color(ColorPicker.queue["friend_armor"]["color"], 0.7)
                            )
        except:
            pass

