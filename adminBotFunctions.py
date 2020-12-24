def adminhelp(update, context):
    from initFunctions import getStatus
    if getStatus(update.message.from_user.id) > 2:
        message = """
adminhelp - get advanced help
toall - message all with signature
setstatus - set user status (0-1-2-3) (/setgroup N userName)
getjson - get local db
[DISABLED] sudo - execute command
[DISABLED] scd - change directory
getip - get public ip
setgroup - set user group (/setgroup groupName userName)
"""
        update.message.reply_text(message)
    pass


################################################################################
def toall(update, context):
    from initFunctions import getUserData, getStatus
    if getStatus(update.message.from_user.id) > 1:
        from var import userdata
        from publicBotHeader import telegramSettings, messageLang
        if update.message.text == "/toall":
            update.message.reply_text(messageLang("toall_error", update))
            return False
        message = update.message.text[7:] + " - @{}"
        username = update.message.from_user.username
        for user in userdata:
            id = getUserData(user, "id")
            context.bot.send_message(id, message.format(username))
        print("Message: '"+message.format(username)+"' sent to all users")
        return True
    pass

################################################################################
def setstatus(update, context):
    from initFunctions import getStatus, getUserData
    if getStatus(update.message.from_user.id) > 2:
        from publicBotHeader import messageLang, userLang
        from adminBotHeader import idIs, setStatus
        username = update.message.text[14:]
        str_id = idIs(username)
        if str_id == "error":
            update.message.reply_text(messageLang("setstatus_error", update).format(username))
            return False
        else:
            status = int(update.message.text[11:12])
            setStatus(str_id, status)
            you_are = userLang("status", int(str_id))
            he_is = messageLang("status", update)
            update.message.reply_text(messageLang("setstatus", update).format(username, he_is[status], status))
            context.bot.send_message(int(str_id), userLang("you_are", int(str_id)).format(you_are[status]))
            return True
    pass

################################################################################
def getjson(update, context):
    from initFunctions import getStatus
    if getStatus(update.message.from_user.id) > 2:
        context.bot.send_document(update.message.from_user.id, open("./userdata.json","rb"))
        return True
    pass

################################################################################
def setgroup(update, context):
    from initFunctions import getStatus, getUserData
    if getStatus(update.message.from_user.id) > 2:
        from publicBotHeader import messageLang, userLang
        from adminBotHeader import idIs, setGroup
        split_message = update.message.text.split(" ")
        group = split_message[1]
        username = split_message[2][1:]
        str_id = idIs(username)
        if str_id == "error":
            update.message.reply_text(messageLang("setstatus_error", update).format(username))
            return False
        else:
            setGroup(str_id, group)
            update.message.reply_text(messageLang("setgroup", update).format(username, group))
            if(group != ""):
                print("Group: user '"+username+"', added to: '"+group+"'")
                context.bot.send_message(int(str_id), userLang("your_group", int(str_id)).format(group))
            else:
                print("Group: user '"+username+"', removed from '"+group+"'")
                context.bot.send_message(int(str_id), userLang("removed_group", int(str_id)))
            return True
    pass

# DISABLED #####################################################################
def sudo(update, context):
    from publicBotHeader import telegramSettings
    if update.message.from_user.id == telegramSettings("master"):
        from var import systemOS
        if systemOS == "linux":
            command = update.message.text[1:]
        else:
            command = update.message.text[6:]
        import os
        update.message.reply_text(os.popen(command).read())
        return True
    else:
        context.bot.send_message(telegramSettings("master"), "Illegal access:")
        context.bot.forward_message(
            telegramSettings("master"),
            update.message.chat.id,
            update.message.message_id
        )
        return False
    pass

# DISABLED #####################################################################
def cd(update, context):
    from publicBotHeader import telegramSettings
    if update.message.from_user.id == telegramSettings("master"):
        import os
        dir = update.message.text[4:]
        os.chdir(dir)
        return True
    pass

################################################################################
def getip(update, context):
    from publicBotHeader import telegramSettings
    if update.message.from_user.id == telegramSettings("master"):
        import os
        command = os.popen("curl -s ipinfo.io/ip").read()
        update.message.reply_text(command)
        return True
    pass

################################################################################
################################################################################
