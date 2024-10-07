from json import load, dumps
import os, ctypes, psutil, random, string, requests

class Utils:
    @staticmethod
    def load_config(data):
        try:
            if not os.path.exists(data.data["config"]["file"]):
                return False
            
            with open(file=data.data["config"]["file"], mode="r", encoding="utf-8") as config:
                return load(config)
        except:
            ctypes.windll.user32.MessageBoxW(0, "An error occurred while importing saved configuration", "Error", 0x10)

    @staticmethod
    def save_config(data):
        try:
            with open(data.data["config"]["file"], "w", encoding="utf-8") as config:
                config.write(dumps(data.data, indent=4))
        except:
            ctypes.windll.user32.MessageBoxW(0, "An error occurred while saving the configuration", "Error", 0x10)

    @staticmethod
    def download_fonts():
        try:
            fonts = [
                {"url": "https://github.com/gabsroot/Fury/raw/main/fonts/arial.ttf", "name": "arial.ttf"},
                {"url": "https://github.com/gabsroot/Fury/raw/main/fonts/pixel.ttf", "name": "pixel.ttf"},
                {"url": "https://github.com/gabsroot/Fury/raw/main/fonts/weapon.ttf", "name": "weapon.ttf"}
            ]

            for font in fonts:
                font_path = os.path.join("C:\\", "Fury", "fonts", font["name"])

                if not os.path.exists(font_path):
                    response = requests.get(font["url"])

                    if response.status_code == 200:
                        with open(font_path, "wb") as file:
                            file.write(response.content)
        except:
            ctypes.windll.user32.MessageBoxW(0, "An error occurred while downloading the fonts", "Error", 0x10)

    @staticmethod
    def process_running(name):
        return any(proc.info["name"] == name for proc in psutil.process_iter(["name"]) if proc.info["name"])

    @staticmethod
    def gen_random_string(length):
        return "".join(random.choices(string.ascii_letters, k=length))
    
    @staticmethod
    def get_id(item):
        ids = {
            "aimbot": {
                "shift": 16,
                "ctrl": 17,
                "mouse_1": 1
            },
            "trigger": {
                "shift": 16,
                "ctrl": 17
            },
            "weapon": {
                1: "A", # deagle
                2: "B", # dual
                3: "C", # five
                4: "D", # glock
                7: "W", # ak47
                8: "U", # aug
                9: "Z", # awp
                10: "R", # famas
                11: "X", # g3sG1
                13: "Q", # galil
                14: "a", # m249
                17: "K", # mac10
                19: "P", # p90
                23: "?", # mp5
                24: "L", # ump45
                25: "\\", # xm1014
                26: "M", # bizon
                27: "^", # mag7
                28: "`", # negev
                29: "]", # sawedoff
                30: "H", # tec 9
                31: "b", # zeus
                32: "E", # p2000
                33: "O", # mp7
                34: "N", # mp9
                35: "_", # nova
                36: "F", # p250
                38: "Y", # scar20
                39: "V", # sg556
                40: "[", # ssg08
                42: ">", # ct_knife
                43: "c", # flashbang
                44: "d", # hegrenade
                45: "e", # smokegrenade
                46: "f", # molotov
                47: "&", # decoy
                48: "%", # incgrenade
                49: "$", # c4
                16: "S", # m4a4
                61: "G", # usp
                60: "T", # m4a1
                63: "I", # cz75a
                64: "J", # r8
                59: ":", # t_knife
                500: "g", # bayo
                505: "1", # flip
                506: "2", # gut
                507: "4", # karambit
                508: "5", # m9
                512: "8", # stiletto
                514: "7", # skeleton
                515: "-", # survival
                516: "<", # ursus
                518: ",", # butterfly
                521: "9", # bowie
                520: "@", # shadow dg
                523: "=", # talon
                524: "/", # classic
                525: ".", # paracord
                527: "6", # nomad
                528: "3", # navaja
            }
        }

        return ids[item]