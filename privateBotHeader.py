def getDriveInfo(key):
    from var import settings
    return settings["drive"][key]
    pass

################################################################################
def setLastCell(val):
    from var import settings
    settings["drive"]["last_cell"] = val
    pass

################################################################################
def notPermittedResponse(update):
    from publicBotHeader import messageLang
    update.message.reply_text(messageLang("not_permitted", update).format(update.message.from_user.first_name))
    pass

################################################################################
def indexOf(string, char="."):
    index = -1
    while (string[index] != char):
        index = index - 1
    return index+1
    pass

################################################################################
def fileExtention(file_name):
    return file_name[indexOf(file_name):].lower()
    pass

################################################################################
def fileName(file_name):
    return file_name[:indexOf(file_name)-1].lower()
    pass

################################################################################
def processFileType(bot, update):
    from initFunctions import getStatus, getUserData
    message = update.message
    id = message.from_user.id
    if getStatus(id) > 0:
        document = message.document
        from publicBotHeader import messageLang
        if document.file_size < 20971520:
            from publicBotHeader import downloadFile, telegramSettings
            file_name = document.file_name
            file_ext = fileExtention(file_name)
            path = downloadFile(bot, document, file_name)
            if file_ext == "stl":
                from driveFunctions import fileToDrive
                print("STL file from",id)
                fileToDrive(path, getUserData(id, "folder_id"))
                bot.forward_message(telegramSettings("manager"),message.chat.id,message.message_id)
                message.reply_text(messageLang("to_drive", update).format(file_name))
                print("File Loaded on GoogleDrive")
            elif file_ext == "gcode":
                from driveFunctions import fileToSpreadsheets
                print("GCode file from",id)
                done = fileToSpreadsheets(update, path)
                if not done:
                    message.reply_text(messageLang("unknown_flavor", update))
                    bot.forward_message(telegramSettings("master"),message.chat.id,message.message_id)
                    print("Unknown flavor")
                else:
                    message.reply_text(messageLang("to_spreadsheets", update).format(file_name))
                    bot.forward_message(telegramSettings("manager"),message.chat.id,message.message_id)
                    print("Sheet filled with print data")
            elif file_ext == "curaprofile" and id == telegramSettings("manager"):
                from driveFunctions import fileToDrive
                print("Curaprofile file")
                fileToDrive(path, getDriveInfo("profiles"))
                print("Profile loaded")
        else:
            message.reply_text(messageLang("too_big", update))
    pass

################################################################################
################################################################################
