def addUser(id, first_name, last_name, username, language_code):
    from initFunctions import updateJson, getStatus, getUserData
    from var import userdata
    userInfo = {
        "status":0,
        "id":id,
        "first_name":first_name,
        "last_name":last_name,
        "username":username,
        "language_code":language_code,
        "sticker":True,
        "folder_id":""
    }
    was_known = str(id) in userdata
    if was_known:
        userInfo["status"] = getStatus(id)
        userInfo["sticker"] = getUserData(id, "sticker")
        userInfo["folder_id"] = getUserData(id, "folder_id")
        print("Refresh userInfo, ID:", id, "- username: @"+username)
    else:
        print("Added new user to 'userdata.json', ID: ", id, "- username: @"+username)
    userdata[str(id)] = userInfo
    updateJson(userdata, "userdata.json")
    return was_known
    pass

################################################################################
def messageLang(message_key, update):
    language = update.message.from_user.language_code[:2]
    from var import messages
    if not language == "it":
        language = "en"
    try:
        return messages[message_key][language]
    except KeyError as ke:
        print("ERROR: missing ", ke," key in messages.json fom 'messageLang'")
        return ("Errore interno (-.-')")
    pass

################################################################################
def userLang(message_key, user):
    from var import messages
    from initFunctions import getUserData
    language = getUserData(user, "language_code")
    if not language == "it":
        language = "en"
    try:
        return messages[message_key][language]
    except KeyError as ke:
        print("ERROR: missing ", ke," key in messages.json fom 'userLang'")
        return ("Errore interno (-.-')")
    pass

################################################################################
def telegramSettings(key="bot_username"):
    from var import settings
    return settings["telegram"][key]
    pass

################################################################################
def getSticker(update):
    from var import userdata
    return userdata[update]["sticker"]
    pass

################################################################################
def setSticker(id, value):
    from var import userdata
    userdata[id]["sticker"] = value
    pass

################################################################################
def downloadFile(bot, file, file_name = "tmp.png"):
    from initFunctions import tmpFolder
    from var import systemOS
    folder = tmpFolder(systemOS)
    target = folder+file_name
    file_id = file.file_id
    bot.get_file(file_id).download(target)
    return folder, file_name
    pass

################################################################################
def resizePhoto(path, photo):
    folder, file = path
    path = folder+file
    W = photo.width
    H = photo.height
    from var import systemOS
    from initFunctions import checkModule
    try:
        import PIL
    except ImportError:
        checkModule("Pillow")
        import PIL
    from PIL import Image
    if W > H:
        w = 512
        h = H * 512 / W
    else:
        h = 512
        w = W * 512/H
    img = Image.open(path)
    img = img.resize((int(w), int(h)), PIL.Image.ANTIALIAS)
    new_image = folder+"resized.png"
    img.save(new_image, quality=85)
    return new_image
    pass

################################################################################
def pngResize(update, context):
    from initFunctions import getUserData
    message = update.message
    id = message.from_user.id
    chat_id = message.chat.id
    if  chat_id > 0 and getUserData(id, "sticker"):
        document = message.document
        path = downloadFile(context.bot, document)
        resized = resizePhoto(path, document.thumb)
        context.bot.send_document(chat_id, open(resized,"rb"))
    pass

################################################################################
################################################################################
