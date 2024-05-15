from core.utils import Utils
from json import load, dumps
import os

class Config:
    def __init__(self):
        self.utils = Utils()

    def Load(self, file):
        try:
            if not os.path.exists(file):
                return False
            else:
                with open(file, "r", encoding="utf-8") as file:
                    config = load(file)
                    return config
        except:
            self.utils.ShowMessageBox("Error", "An error occurred while importing saved configuration", 0x10)

    def Save(self, file, data):
        try:
            config = dumps(data.setup, indent=4)

            with open(file, "w", encoding="utf-8") as configFile:
                configFile.write(config)
        except:
            self.utils.ShowMessageBox("Error", "An error occurred while saving the configuration", 0x10)
