import pyMeow as pm, time
from ui.config import *
from ui.menu import *

class Draw:

    @staticmethod
    def draw_tabs():

        for i, item in enumerate(Navigation.queue):
            hover = (Menu.x + item["x"]) <= Mouse.x <= (Menu.x + item["x"] + item["width"]) and (Menu.y + item["y"]) <= Mouse.y <= (Menu.y + item["y"] + item["height"])

            if pm.mouse_pressed() and hover:
                if Navigation.active != i:
                    Navigation.transition_pos = Navigation.queue[Navigation.active]["y"]

                Navigation.active = i

        active = Navigation.queue[Navigation.active]
        
        Navigation.transition_pos += (active["y"] - Navigation.transition_pos) * 0.1

        # tab bg
        pm.draw_rectangle_rounded(
            posX=Menu.x + active["x"],
            posY=Menu.y + Navigation.transition_pos,
            width=active["width"],
            height=active["height"],
            roundness=0.3,
            segments=1,
            color=pm.fade_color(pm.get_color("#1C252F"), 0.99),
        )

        for item in Navigation.queue:
            # tab icon
            pm.draw_font(
                fontId=2,
                text=item["icon"],
                posX=Menu.x + item["x"] + 7,
                posY=Menu.y + item["y"] + 7,
                fontSize=item["size"],
                spacing=1,
                tint=pm.get_color("#1b90c4")
            )

    @staticmethod
    def draw_menu():

        Draw.draw_notifications()

        if Menu.show:

            # bg
            pm.draw_rectangle_rounded(
                posX=Menu.x,
                posY=Menu.y,
                width=510,
                height=400,
                roundness=0.03,
                segments=1,
                color=pm.fade_color(pm.get_color("#0B0C0E"), 0.99)
            )

            # sidebar
            pm.draw_rectangle_rounded(
                posX=Menu.x,
                posY=Menu.y,
                width=50,
                height=400,
                roundness=0.2,
                segments=1,
                color=pm.fade_color(pm.get_color("#111316"), 0.99)
            )

            # tabs
            Draw.draw_tabs()

            # content
            Content.draw()

    @staticmethod
    def draw_spectators():

        if Switch.queue.get("spectators") and Switch.queue["spectators"]:

            spectators_list = ["gabe", "pingu"]

            # bg
            pm.draw_rectangle_rounded(
                posX=Spectators.x,
                posY=Spectators.y,
                width=140,
                height=25,
                roundness=0.2,
                segments=1,
                color=pm.fade_color(pm.get_color("#0B0C0E"), 0.99)
            )

            # label
            pm.draw_font(
                fontId=1,
                text="Spectators",
                posX=Spectators.x + 8,
                posY=Spectators.y + 6,
                fontSize=14,
                spacing=1,
                tint=pm.get_color("#8e9aa3")
            )

            for i, name in enumerate(iterable=spectators_list):
                # bg
                pm.draw_rectangle_rounded(
                    posX=Spectators.x,
                    posY=Spectators.y + (27 * (i + 1)),
                    width=140,
                    height=25,
                    roundness=0.2,
                    segments=1,
                    color=pm.fade_color(pm.get_color("#0B0C0E"), 0.8)
                )
                
                # label
                pm.draw_font(
                    fontId=1,
                    text=name[:18].lower(),
                    posX=Spectators.x + 8,
                    posY=Spectators.y + (27 * (i + 1)) + 5,
                    fontSize=14,
                    spacing=1,
                    tint=pm.get_color("#747f87")
                )

    @staticmethod
    def draw_notifications():
        current_time = time.time()
        posY = 100

        for notification in Notification.queue[:]:

            if notification["time"] > current_time:
                notification["posY"] = posY
                posY += notification["height"] + 10
                current_posX = notification["posX"]

                # start
                if current_posX > notification["tempX"]:
                    notification["posX"] -= (current_posX - notification["tempX"]) * 0.05
            else:
                # end
                if notification["posY"] > 100:
                    notification["posY"] -= 10

                Notification.queue.remove(notification)

            # bg
            pm.draw_rectangle_rounded(
                posX=notification["posX"],
                posY=notification["posY"],
                width=notification["width"],
                height=notification["height"],
                roundness=0.1,
                segments=1,
                color=pm.get_color("#111316")
            )

            # left bar
            pm.draw_rectangle_rounded(
                posX=notification["posX"],
                posY=notification["posY"],
                width=5,
                height=notification["height"],
                roundness=0.5,
                segments=1,
                color=pm.get_color(notification["color"] or "#1b90c4")
            )

            # title
            pm.draw_font(
                fontId=1,
                text=notification["title"],
                posX=notification["posX"] + 12,
                posY=notification["posY"] + 4,
                fontSize=13,
                spacing=1,
                tint=pm.get_color("#808d96")
            )

            # text
            for i, line in enumerate(notification["message"]):
                pm.draw_font(
                    fontId=1,
                    text=line,
                    posX=notification["posX"] + 12,
                    posY=notification["posY"] + 22 + (i * 18),
                    fontSize=14,
                    spacing=1,
                    tint=pm.get_color("#9faab3")
                )
