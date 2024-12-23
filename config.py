class Config:
    aimbot = {
        "enable": False,
        "only_visible": False,
        "draw_fov": False,
        "key": "shift",
        "fov": 10,
        "smooth": 0,
        "distance": 5000
    }
    
    trigger = {
        "enable": False,
        "target_chicken": False,
        "key": "none",
        "delay": 0.05
    }

    esp = {
        "enemy": {
            "bone": {
                "enable": False,
                "color": {"r": 28, "g": 182, "b": 230, "a": 255},
                "thick": 1
            },
            "line": {
                "enable": False,
                "color": {"r": 161, "g": 131, "b": 39, "a": 255},
                "thick": 1
            },
            "box": {
                "enable": False,
                "color": {"r": 58, "g": 202, "b": 63, "a": 255},
                "style": "normal"
            },
            "name": {
                "enable": False,
                "color": {"r": 255, "g": 255, "b": 255, "a": 255}
            },
            "weapon": {
                "enable": False,
                "color": {"r": 219, "g": 23, "b": 23, "a": 255}
            },
            "health": {
                "enable": False
            },
            "armor": {
                "enable": False
            }
        },
        "friend": {
            "bone": {
                "enable": False,
                "color": {"r": 28, "g": 182, "b": 230, "a": 255},
                "thick": 1
            },
            "line": {
                "enable": False,
                "color": {"r": 161, "g": 131, "b": 39, "a": 255},
                "thick": 1
            },
            "box": {
                "enable": False,
                "color": {"r": 58, "g": 202, "b": 63, "a": 255},
                "style": "normal"
            },
            "name": {
                "enable": False,
                "color": {"r": 255, "g": 255, "b": 255, "a": 255}
            },
            "weapon": {
                "enable": False,
                "color": {"r": 219, "g": 23, "b": 23, "a": 255}
            },
            "health": {
                "enable": False
            },
            "armor": {
                "enable": False
            }
        }
    }

    crosshair = {
        "enable": False,
        "color": {"r": 219, "g": 30, "b": 83, "a": 255}
    }

    misc = {
        "ignore_team": False
    }

    config = {
        "slot": "slot1"
    }
