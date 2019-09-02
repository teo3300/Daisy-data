def getSystem():
    import platform
    system = platform.system().lower()
    print("System found: '"+system+"'")
    return system
    pass

################################################################################
def tmpFolder(system):
    tmp = "/tmp/"
    if system == "linux":
        return tmp
    else:
        return "."+tmp

################################################################################
def loadJson(target, folder="./"):
    """Returns settings from json"""
    path = folder + target
    import json
    try:
        with open(path) as jsonFile:
            json_data = json.load(jsonFile)
            jsonFile.close()
            print("'"+target+"' loaded")
            return json_data
    except IOError:
        print("ERROR: '"+target+"' is missing")
        input()
        exit()
    pass

################################################################################
def updateJson(dict, file="userdata.json"):
    import json
    with open(file, "w") as target:
        json.dump(dict, target)
        target.close()
    pass

################################################################################
def getArchive():
    from var import settings
    """Return settings info"""
    try:
        info = settings["archive"]
        name = info["name"]
        ext = info["ext"]
        version = info["major"]
        version = version + "." + info["minor"]
        version = version + "." + info["debug"]
        print("Current archive: '"+name+version+"."+ext+"'")
        return name, version, ext
    except KeyError as ke:
        print("ERROR: missing", ke, "key")
        input()
        exit()
    pass

################################################################################
def archiveDiffer(archive, folder="./source/"):
    name, version, extention = archive
    fileName = name+version+"."+extention
    path = folder + fileName
    import os
    if os.path.exists(path):
        print("Code packed to its last version")
        return False
    else:
        print("New version detected, packing source code:\n----------")
        command = "tar cvfz "+path+" ./*.*"# > /dev/null
        os.system(command)
        print("----------\nCreated new archive:",fileName)
        return True
    pass

################################################################################
def gitUpload(repo, folder="./"):
    print("Synchronizing git repository")
    pass

################################################################################
def checkModule(moduleName):
    from var import systemOS
    if systemOS == "linux":
        command = "sudo pip3.7 install "+moduleName#+" > /dev/null"
    elif systemOS == "windows":
        command = "python -m pip install "+ moduleName+ " --user"
    else:
        print("ERROR: unknown system: '"+systemOS+"'")
        exit()
    import os
    from os import system
    os.system(command)
    pass

################################################################################
def getToken():
    from var import settings
    return settings["bot_token"]
    pass

################################################################################
def getUserData(user, field):
    from var import userdata
    return userdata[str(user)][field]
    pass

################################################################################
def getStatus(id):
    from var import userdata
    return userdata[str(id)]["status"]
    pass

################################################################################
################################################################################
