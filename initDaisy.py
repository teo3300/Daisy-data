from initFunctions import getArchive, archiveDiffer, checkModule, getToken
from var import systemOS, settings
archiveDiffer(getArchive(),"./source/")
#    gitUpload("")

################################################################################
try:
    from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
except:
    checkModule("python-telegram-bot")
    from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from publicBotFunctions import start, help, sticker, endsticker, sticker_resize, document_handler
from privateBotFunctions import getpset, getgd, getgss
from adminBotFunctions import toall, setstatus, getjson, sudo, cd

updater = Updater(getToken())
dispatcher = updater.dispatcher
## public functions
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("sticker", sticker))
dispatcher.add_handler(CommandHandler("endsticker", endsticker))
## private functions
dispatcher.add_handler(CommandHandler("getpset", getpset))
dispatcher.add_handler(CommandHandler("getgd", getgd))
dispatcher.add_handler(CommandHandler("getgss", getgss))
## admin functions
dispatcher.add_handler(CommandHandler("toall", toall))
dispatcher.add_handler(CommandHandler("setstatus", setstatus))
dispatcher.add_handler(CommandHandler("getjson", getjson))
dispatcher.add_handler(CommandHandler("sudo", sudo))
dispatcher.add_handler(CommandHandler("cd", cd))
## messages handler
dispatcher.add_handler(MessageHandler(Filters.photo, sticker_resize))
dispatcher.add_handler(MessageHandler(Filters.document, document_handler))

################################################################################
print("Daisy is running\n")
updater.start_polling()

################################################################################
################################################################################
