class Mouse:
    x = 0
    y = 0

class Menu:
    x = 300
    y = 300
    show = False
    time = 0
    dragging = False
    offset_x = 0
    offset_y = 0

class Navigation:
    queue = [
        {"icon": "0", "x": 9, "y": 54, "width": 36, "height": 34, "size": 21},
        {"icon": "1", "x": 9, "y": 94, "width": 36, "height": 34, "size": 22},
        {"icon": "2", "x": 9, "y": 134, "width": 36, "height": 34, "size": 23},
        {"icon": "3", "x": 9, "y": 174, "width": 36, "height": 34, "size": 21}
    ]

    active = 0
    transition_pos = 0
    done = []

class Notification:
    queue = []

class Button:
    time = {}

class Switch:
    queue = {}
    pos = {}
    time = {}

class Slider:
    queue = {}
    time = {}

class Combo:
    queue = {}
    popup = {
        "open": False,
        "time": 0,
        "state": {}
    }

class ColorPicker:
    queue = {}
    color = {
        "r": 27,
        "g": 144,
        "b": 196,
        "a": 255
    }

class Spectators:
    x = 10
    y = 500
    dragging = False
    offset_x = 0
    offset_y = 0
