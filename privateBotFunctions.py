def getpset(update, context):
    from initFunctions import getStatus
    if getStatus(update.message.from_user.id) > 0:
        from publicBotHeader import messageLang
        from privateBotHeader import getDriveInfo, notPermittedResponse
        update.message.reply_markdown(
            messageLang("getpset", update).format(
                getDriveInfo("url"),
                getDriveInfo("profiles")
            )
        )
    else:
        notPermittedResponse(update)
    pass

################################################################################
def getgd(update, context):
    from initFunctions import getStatus, getUserData
    if getStatus(update.message.from_user.id) > 0:
        from var import userdata
        from publicBotHeader import messageLang
        from privateBotHeader import getDriveInfo, notPermittedResponse
        id = update.message.from_user.id
        update.message.reply_markdown(
            messageLang("getgd", update).format(
                getUserData(id, "first_name"),
                getDriveInfo("url"),
                getUserData(id, "folder_id")
            )
        )
    else:
        notPermittedResponse(update)
    pass

################################################################################
def getgss(update, context):
    from initFunctions import getStatus
    if getStatus(update.message.from_user.id) > 0:
        from publicBotHeader import messageLang
        from privateBotHeader import getDriveInfo, notPermittedResponse
        update.message.reply_markdown(
            messageLang("getgss", update).format(
                getDriveInfo("sheets_url")
            )
        )
    else:
        notPermittedResponse(update)
    pass

################################################################################
################################################################################
