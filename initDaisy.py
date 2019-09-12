from initFunctions import getArchive, archiveDiffer, checkModule, getToken
from var import systemOS, settings
archiveDiffer(getArchive(),"./source/")
#    gitUpload("")

################################################################################
try:
    from telegram.ext import Updater, CommandHandler, PrefixHandler, MessageHandler, Filters
except:
    checkModule("python-telegram-bot")
    from telegram.ext import Updater, CommandHandler, PrefixHandler, MessageHandler, Filters
from publicBotFunctions import start, help, sticker, endsticker, sticker_resize, document_handler
from privateBotFunctions import getpset, getgd, getgss
from adminBotFunctions import toall, setstatus, getjson, sudo, cd, getip
updater = Updater(getToken(), use_context=True)
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
dispatcher.add_handler(PrefixHandler("/","toall", toall))
dispatcher.add_handler(PrefixHandler("/","setstatus", setstatus))
dispatcher.add_handler(PrefixHandler("/","getjson", getjson))
dispatcher.add_handler(PrefixHandler("/","sudo", sudo))
dispatcher.add_handler(PrefixHandler("/","cd", cd))
dispatcher.add_handler(PrefixHandler("/","getip", getip))
## messages handler
dispatcher.add_handler(MessageHandler(Filters.photo, sticker_resize))
dispatcher.add_handler(MessageHandler(Filters.document, document_handler))

################################################################################
print("Daisy is running\n")
updater.start_polling()

################################################################################
################################################################################
