def start(update, context):
    user = update.message.from_user
    id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    language_code = user.language_code
    from publicBotHeader import addUser, messageLang, telegramSettings
    if not addUser(id, first_name, last_name, username, language_code):
        message = update.message
        context.bot.forward_message(
            telegramSettings("master"),
            message.chat.id,
            message.message_id
        )
    update.message.reply_text(
        messageLang("start", update).format(
            first_name,
            telegramSettings("master_username")
        )
    )
    pass

################################################################################
def help(update, context):
    from publicBotHeader import messageLang
    update.message.reply_markdown(messageLang("help", update))
    pass

################################################################################
def sticker(update, context):
    from publicBotHeader import messageLang, getSticker, setSticker
    id = str(update.message.from_user.id)
    setSticker(id, True)
    update.message.reply_text(messageLang("sticker", update))
    pass

################################################################################
def endsticker(update, context):
    from publicBotHeader import messageLang, getSticker, setSticker
    id = str(update.message.from_user.id)
    setSticker(id, False)
    update.message.reply_text(messageLang("endsticker", update))
    pass

################################################################################
def sticker_resize(update, context):
    from initFunctions import getUserData
    message = update.message
    id = message.from_user.id
    chat_id = message.chat.id
    if  chat_id > 0 and getUserData(id, "sticker"):
        from publicBotHeader import downloadFile, resizePhoto
        photo = message.photo[-1]
        path = downloadFile(context.bot, photo)
        resized = resizePhoto(path, photo)
        context.bot.send_document(chat_id, open(resized,"rb"))
    pass

################################################################################
def document_handler(update, context):
    document = update.message.document
    type = document.mime_type
    if type == "image/png":
        from publicBotHeader import pngResize
        pngResize(update, context)
    else:#if type == "text/plain" or type == "text/x-matlab":
        from privateBotHeader import processFileType
        processFileType(update, context)
    #else:
        #print("Unknown file type:", type)
    pass
################################################################################
################################################################################
