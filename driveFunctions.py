def driveOpen():
    try:
        from pydrive.auth import GoogleAuth
        from pydrive.drive import GoogleDrive
    except:
        from initFunctions import checkModule
        checkModule("PyDrive")
        from pydrive.auth import GoogleAuth
        from pydrive.drive import GoogleDrive
    return GoogleDrive(GoogleAuth())
    pass

################################################################################
def sheetOpen():
    from initFunctions import checkModule
    try:
        import gspread
    except:
        checkModule("gspread")
        import gspread
    try:
        from oauth2client.service_account import ServiceAccountCredentials
    except:
        checkModule("oauth2client")
        from oauth2client.service_account import ServiceAccountCredentials
    from privateBotHeader import getDriveInfo
    creds = ServiceAccountCredentials.from_json_keyfile_name(getDriveInfo("credentials"),getDriveInfo("scope"))
    client = gspread.authorize(creds)
    return client.open(getDriveInfo("sheet")).sheet1
    pass

################################################################################
def fileToDrive(path, folder_id):
    from var import drive
    import datetime
    now = datetime.datetime.now()
    date = "{}-{:02d}-{:02d}-".format(now.year, now.month, now.day)
    folder, file_name = path
    metadata = {
        "title": date+file_name,
        "parents":[{
            "id":folder_id,
            "kind": "drive#childList"
        }]
    }
    to_upload = drive.CreateFile(metadata)
    to_upload.SetContentFile(folder+file_name)
    to_upload.Upload()
    pass

################################################################################
def firstFree(sheet):
    i = 2
    while sheet.cell(i,1).value != "":
        i = i + 10
    while sheet.cell(i,1).value == "":
        i = i - 1
    return i+1
    pass

################################################################################
def fileToSpreadsheets(update, path):
    from var import sheet
    from extractor import flavorExtract
    from initFunctions import getUserData
    row = flavorExtract(path)
    if len(row) == 0:
        return False
    else:
        to_fill = firstFree(sheet)
        file_from = getUserData(update.message.from_user.id, "first_name")
        try:
            caption = update.message.caption
        except:
            caption = file_from 
        row[0] = to_fill-1
        row[1] = file_from
        row[6] = caption
        sheet.insert_row(row, to_fill)
        return True
    pass

################################################################################
################################################################################
