import pyMeow as pm, time
from ui.config import *
from ui.resources.textures import *

class Components:

    @staticmethod
    def add_button(ref, text, posX, posY, width=100, height=20, callback=None):
        hover = (Menu.x + posX) < Mouse.x < (Menu.x + posX + width) and (Menu.y + posY) < Mouse.y < (Menu.y + posY + height)

        # bg
        pm.draw_rectangle_rounded(
            posX=Menu.x + posX,
            posY=Menu.y + posY,
            width=width,
            height=height,
            roundness=0.2,
            segments=1,
            color=pm.get_color("#202933" if hover else "#1C252F")
        )

        # label
        pm.draw_font(
            fontId=1,
            text=text,
            posX=Menu.x + posX + (width / 2) - (pm.measure_text(text=text, fontSize=14) / 2),
            posY=Menu.y + posY + (height / 2) - 7,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#747f87")
        )

        if ref not in Button.time:
            Button.time[ref] = 0

        current_time = time.time()

        if hover and pm.mouse_pressed() and (current_time - Button.time[ref] > 0.5):
            Button.time[ref] = current_time

            if callback:
                callback()

    @staticmethod
    def add_switch(ref, text, posX, posY, callback=None):

        if ref not in Switch.queue:
            Switch.queue[ref] = False
            Switch.pos[ref] = 156
            Switch.time[ref] = 0

        target_pos = 169 if Switch.queue[ref] else 156

        if abs(Switch.pos[ref] - target_pos) < 0.1:
            Switch.pos[ref] = target_pos
        else:
            Switch.pos[ref] += (target_pos - Switch.pos[ref]) * 0.3

        hover = (Menu.x + posX + 150) < Mouse.x < (Menu.x + posX + 175) and (Menu.y + posY) < Mouse.y < (Menu.y + posY + 13)

        # bg
        pm.draw_rectangle_rounded(
            posX=Menu.x + posX + 150,
            posY=Menu.y + posY + 3,
            width=25,
            height=10,
            roundness=0.5,
            segments=1,
            color=pm.get_color("#1C252F")
        )
        
        # circle
        pm.draw_circle(
            centerX=Menu.x + posX + Switch.pos[ref],
            centerY=Menu.y + posY + 8,
            radius=7,
            color=pm.get_color("#1b90c4" if Switch.queue[ref] else "#4B5660")
        )
        
        # label
        pm.draw_font(
            fontId=1,
            text=text,
            posX=Menu.x + posX,
            posY=Menu.y + posY,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#8e9aa3" if Switch.queue[ref] else "#747f87")
        )
        
        current_time = time.time()

        if hover and pm.mouse_pressed() and current_time - Switch.time[ref] > 0.2:
            Switch.queue[ref] = not Switch.queue[ref]
            Switch.time[ref] = current_time

            if callback:
                callback()

    @staticmethod
    def add_slider(ref, text, posX, posY, width, min_value, max_value, fmt=".0f", callback=None):

        if ref not in Slider.queue:
            Slider.queue[ref] = min_value
            Slider.time[ref] = 0
        
        hover = (Menu.x + posX + 60) < Mouse.x < (Menu.x + posX + 60 + width) and (Menu.y + posY - 7) < Mouse.y < (Menu.y + posY + 12)
        
        if hover and pm.mouse_pressed():
            Slider.queue[ref] = min(max(min_value, (Mouse.x - (Menu.x + posX + 60)) / width * (max_value - min_value) + min_value), max_value)

        # label
        pm.draw_font(
            fontId=1,
            text=text,
            posX=Menu.x + posX,
            posY=Menu.y + posY - 5,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#747f87")
        )

        # bar
        pm.draw_rectangle_rounded(
            posX=Menu.x + posX + 60,
            posY=Menu.y + posY,
            width=width,
            height=4,
            roundness=0.5,
            segments=1,
            color=pm.get_color("#1C252F")
        )
        
        # fill bar
        pm.draw_rectangle_rounded(
            posX=Menu.x + posX + 60,
            posY=Menu.y + posY,
            width=(Slider.queue[ref] - min_value) / (max_value - min_value) * width,
            height=4,
            roundness=0.5,
            segments=1,
            color=pm.get_color("#1b90c4")
        )
        
        # circle
        pm.draw_circle(
            centerX=Menu.x + posX + 60 + (Slider.queue[ref] - min_value) / (max_value - min_value) * width,
            centerY=Menu.y + posY + 2,
            radius=6,
            color=pm.get_color("#1b90c4")
        )

        # value
        pm.draw_font(
            fontId=1,
            text=f"{Slider.queue[ref]:{fmt}}",
            posX=Menu.x + posX + 60 + width + 8,
            posY=Menu.y + posY - 5,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#747f87")
        )
        
        current_time = time.time()

        if hover and pm.mouse_pressed() and current_time - Slider.time[ref] > 0.2:
            Slider.time[ref] = current_time

            if callback:
                callback(Slider.queue[ref])

        return float(f"{Slider.queue[ref]:{fmt}}") if fmt.endswith("f") else int(float(f"{Slider.queue[ref]:{fmt}}"))

    @staticmethod
    def add_combo(ref, label, posX, posY, items, width=100, spacing=70, default_value=""):

        hover = (Menu.x + posX + spacing) < Mouse.x < (Menu.x + posX + width + spacing) and (Menu.y + posY) < Mouse.y < (Menu.y + posY + 20)

        # label
        pm.draw_font(
            fontId=1,
            text=label,
            posX=Menu.x + posX,
            posY=Menu.y + posY + 3,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#747f87")
        )

        # button bg
        pm.draw_rectangle_rounded(
            posX=Menu.x + posX + spacing,
            posY=Menu.y + posY,
            width=width,
            height=20,
            roundness=0.2,
            segments=1,
            color=pm.get_color("#202933" if hover else "#1C252F")
        )

        # set default value
        default_value = items[0] if items else default_value

        if ref not in Combo.queue:
            Combo.queue[ref] = default_value

        # text
        pm.draw_font(
            fontId=1,
            text=Combo.queue.get(ref) or default_value[:10],
            posX=Menu.x + posX + 6 + spacing,
            posY=Menu.y + posY + 3,
            fontSize=14,
            spacing=1,
            tint=pm.get_color("#747f87")
        )

        # open popup
        if pm.mouse_pressed() and hover:
            current_time = time.time()
            last_popup_time = Combo.popup["state"].get(ref, {}).get("time", 0)
            
            if current_time - last_popup_time > 0.3:
                Combo.popup["state"][ref] = {"open": not Combo.popup["state"].get(ref, {}).get("open", False), "time": current_time}

        # popup
        if Combo.popup["state"].get(ref, {}).get("open", False):
            # popup bg
            pm.draw_rectangle_rounded(
                posX=Menu.x + posX + spacing,
                posY=Menu.y + posY + 23,
                width=width,
                height=len(items) * 22,
                roundness=0.1,
                segments=1,
                color=pm.get_color("#1C252F")
            )

            for i, item in enumerate(items):
                hover = (Menu.x + posX + spacing) < Mouse.x < (Menu.x + posX + width + spacing) and (Menu.y + posY + 23 + i * 22) < Mouse.y < (Menu.y + posY + 23 + (i + 1) * 22)

                # popup option
                pm.draw_font(
                    fontId=1,
                    text=item[:10],
                    posX=Menu.x + posX + 6 + spacing,
                    posY=Menu.y + posY + 27 + i * 22,
                    fontSize=14,
                    spacing=1,
                    tint=pm.get_color("#909396" if hover else "#797e82")
                )

                # select
                if pm.mouse_pressed() and hover:
                    Combo.queue[ref] = item
                    Combo.popup["state"][ref]["open"] = False
                    break

        return Combo.queue.get(ref)
    
    @staticmethod
    def add_color_picker(ref, posX, posY, default_color=ColorPicker.color):

        if ref not in ColorPicker.queue:
            ColorPicker.queue[ref] = {"open": False, "time": 0, "color": default_color}

        this = ColorPicker.queue[ref]
        hover = (Menu.x + posX) < Mouse.x < (Menu.x + posX + 15) and (Menu.y + posY) < Mouse.y < (Menu.y + posY + 14)

        # icon
        pm.draw_font(
            fontId=2,
            text="4",
            posX=Menu.x + posX,
            posY=Menu.y + posY,
            fontSize=15,
            spacing=1,
            tint=pm.fade_color(this["color"], 0.7) if hover else pm.fade_color(this["color"], 0.6)
        )

        # open popup
        if hover and pm.mouse_pressed():
            current_time = time.time()

            if current_time - this["time"] > 0.2:
                for item, data in ColorPicker.queue.items():
                    if item != ref:
                        data["open"] = False

                this["open"] = not this["open"]
                this["time"] = current_time

        # popup
        if this["open"]:
            hover = (Menu.x + 524) < Mouse.x < (Menu.x + 520 + 155) and (Menu.y + 242) < Mouse.y < (Menu.y + 238 + 155)
            color = pm.pixel_at_mouse()["color"] if hover else pm.get_color("#25292e")

            # popup bg
            pm.draw_rectangle_rounded(
                posX=Menu.x + 520,
                posY=Menu.y + 238,
                width=200,
                height=157,
                roundness=0.03,
                segments=1,
                color=pm.get_color("#111316")
            )

            # txd
            pm.draw_texture(
                texture=Textures.load("colorpicker.png"),
                posX=Menu.x + 524,
                posY=Menu.y + 242,
                tint=pm.get_color("#ffffff"),
                rotation=0,
                scale=0.5
            )

            # color preview label
            pm.draw_font(
                fontId=1,
                text="Color",
                posX=Menu.x + 680,
                posY=Menu.y + 242,
                fontSize=13,
                spacing=1,
                tint=pm.get_color("#747f87")
            )

            # color preview
            pm.draw_rectangle_rounded(
                posX=Menu.x + 680,
                posY=Menu.y + 258,
                width=35,
                height=25,
                roundness=0.08,
                segments=1,
                color=this["color"] or default_color
            )

            # hover preview label
            pm.draw_font(
                fontId=1,
                text="Hover",
                posX=Menu.x + 680,
                posY=Menu.y + 288,
                fontSize=13,
                spacing=1,
                tint=pm.get_color("#747f87")
            )

            # hover preview
            pm.draw_rectangle_rounded(
                posX=Menu.x + 680,
                posY=Menu.y + 305,
                width=35,
                height=25,
                roundness=0.08,
                segments=1,
                color=color
            )

            if hover and pm.mouse_pressed():
                this["color"] = color
                this["open"] = False

        return this["color"]

    @staticmethod
    def add_notification(title, message, color=None, show_time=2):
        text = []
        line = ""

        for word in message.split():
            temp = f"{line} {word}".strip()

            if pm.measure_text(text=temp, fontSize=14) <= 240:
                line = temp
            else:
                text.append(line)
                line = word

        if line:
            text.append(line)

        height = 45 + (18 * len(text) - 18)
        width = max(250, max((pm.measure_text(text=line, fontSize=14) for line in text), default=0) + 20)

        notification = {
            "posX": pm.get_screen_width(),
            "posY": Notification.queue[-1]["posY"] + Notification.queue[-1]["height"] + 10 if Notification.queue else 100,
            "tempX": pm.get_screen_width() - width - 10,
            "width": width,
            "height": height,
            "title": title,
            "message": text,
            "color": color,
            "time": time.time() + show_time
        }

        Notification.queue.append(notification)
