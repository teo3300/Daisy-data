def toall(bot, update):
    from initFunctions import getUserData, getStatus
    if getStatus(update.message.from_user.id) > 1:
        from var import userdata
        from publicBotHeader import telegramSettings
        message = update.message.text[7:] + " - @{}"
        username = update.message.from_user.username
        for user in userdata:
            id = getUserData(user, "id")
            bot.send_message(id, message.format(username))
        print("Message: '"+message.format(username)+"' sent to all users")
    pass

################################################################################
def setstatus(bot, update):
    from initFunctions import getStatus, getUserData
    if getStatus(update.message.from_user.id) > 2:
        from publicBotHeader import messageLang, userLang
        from adminBotHeader import idIs, setStatus
        username = update.message.text[14:]
        str_id = idIs(username)
        if str_id == "error":
            update.message.reply_text(messageLang("setstatus_error", update).format(username))
        else:
            status = int(update.message.text[11:12])
            setStatus(str_id, status)
            you_are = userLang("status", int(str_id))
            he_is = messageLang("status", update)
            update.message.reply_text(messageLang("setstatus", update).format(username, he_is[status], status))
            bot.send_message(int(str_id), userLang("you_are", int(str_id)).format(you_are[status]))
    pass

################################################################################
def getjson(bot, update):
    from initFunctions import getStatus
    if getStatus(update.message.from_user.id) > 2:
        bot.send_document(update.message.from_user.id, open("./userdata.json","rb"))
    pass

################################################################################
def sudo(bot, update):
    from publicBotHeader import telegramSettings
    if update.message.from_user.id == telegramSettings("master"):
        from var import systemOS
        if systemOS == "linux":
            command = update.message.text[1:]
        else:
            command = update.message.text[6:]
        import os
        update.message.reply_text(os.popen(command).read())
    else:
        bot.send_message(telegramSettings("master"), "Illegal access:")
        bot.forward_message(
            telegramSettings("master"),
            message.chat.id,
            message.message_id
        )
    pass

################################################################################
def cd(bot, update):
    from publicBotHeader import telegramSettings
    if update.message.from_user.id == telegramSettings("master"):
        import os
        dir = update.message.text[4:]
        os.chdir(dir)
    pass

################################################################################
################################################################################