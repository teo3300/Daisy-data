from initFunctions import getSystem, loadJson
from driveFunctions import driveOpen, sheetOpen
systemOS = getSystem()
settings = loadJson("settings.json")
userdata = loadJson("userdata.json")
messages = loadJson("messages.json")
drive = driveOpen()
sheet = sheetOpen()
