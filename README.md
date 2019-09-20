# Daisy-data
Second attempt to create a telegram bot to manage 3D-printing files

What this bot can do:
- Upload *STL* files on a personal GoogleDrive folder
- Extract Printing data (duration, type and quantity of material used ecc...) from *GCODE* files and save them on a printing sheet
- Resize Images and file to a 512*512 (or smaller) resolution to easily create Telegram stickers

Differences from the old version:
- Responses based on user's saved language
- All users' data can be edited during the execution from an Admin account and are stored in an external file
- Changed Telegram API from *telepot* to *python-telegram-bot*
