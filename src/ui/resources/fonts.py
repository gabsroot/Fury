import pyMeow as pm, os, sys

class Fonts:
    
    @staticmethod
    def load(name, ref):
        try:
            font = os.path.join(sys._MEIPASS, "fonts")
        except:
            font = "../assets/fonts"

        pm.load_font(fileName=os.path.join(font, name), fontId=ref)
