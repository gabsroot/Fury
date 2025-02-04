import random, string, unicodedata

class Utils:

    @staticmethod
    def random_string(size):
        return "".join(random.choices(string.ascii_letters, k=size))

    @staticmethod
    def clean_text(text, size=10):
        text = "".join(char for char in unicodedata.normalize("NFD", text) if not unicodedata.combining(char))
        return text[:size]
    
    @staticmethod
    def weapon_icon(index):
        icons = {
            1: "A",   # deagle
            2: "B",   # dual
            3: "C",   # five
            4: "D",   # glock
            7: "W",   # ak47
            8: "U",   # aug
            9: "Z",   # awp
            10: "R",  # famas
            11: "X",  # g3sg1
            13: "Q",  # galil
            14: "a",  # m249
            17: "K",  # mac10
            19: "P",  # p90
            23: "?",  # mp5
            24: "L",  # ump45
            25: "\\", # xm1014
            26: "M",  # bizon
            27: "^",  # mag7
            28: "`",  # negev
            29: "]",  # sawedoff
            30: "H",  # tec 9
            31: "b",  # zeus
            32: "E",  # p2000
            33: "O",  # mp7
            34: "N",  # mp9
            35: "_",  # nova
            36: "F",  # p250
            38: "Y",  # scar20
            39: "V",  # sg556
            40: "[",  # ssg08
            42: ">",  # ct_knife
            43: "c",  # flashbang
            44: "d",  # hegrenade
            45: "e",  # smokegrenade
            46: "f",  # molotov
            47: "&",  # decoy
            48: "%",  # incgrenade
            49: "$",  # c4
            16: "S",  # m4a4
            61: "G",  # usp
            60: "T",  # m4a1
            63: "I",  # cz75a
            64: "J",  # r8
            59: ":",  # t_knife
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
            528: "3" # navaja
        }

        return icons.get(index, "")
