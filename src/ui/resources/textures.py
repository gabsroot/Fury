import pyMeow as pm, os, sys

class Textures:

    @staticmethod
    def load(name):
        try:
            texture = os.path.join(sys._MEIPASS, "textures", name)
        except:
            texture = os.path.join("../", "assets", "textures", name)

        return pm.load_texture(fileName=texture)
