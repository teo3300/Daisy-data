def time_cv(time):
    hours = str(int(time / 3600))
    minutes = str(int((time % 3600) / 60))
    seconds = str(time % 60)
    return hours+":"+minutes+":"+seconds
    pass

def readDataMarlin(file, line_stop):
    import datetime
    now = datetime.datetime.now()
    date = "{:02d}/{:02d}/{}".format(now.day, now.month, now.year)
    from privateBotHeader import indexOf
    line = file.readline()
    time = int(line[indexOf(line, ":"):-1])
    duration = time_cv(time)
    line = file.readline()
    length = float(line[indexOf(line, ":"):line_stop-3])
    while line[0:4] != "M104":
        line = file.readline()
    t = line[6:9]
    if int(t) < 220:
        material = "PLA"
        weight = round(length * 3.0303)
    else:
        material = "ABS"
        weight = "??"
    length = round(length, 2)
    return ["??","??",duration,length,weight,material,"??","??",date,"??"]
    pass

def flavorExtract(path):
    from privateBotHeader import indexOf, fileName
    from var import systemOS
    row = []
    line_stop = 0
    if systemOS == "linux":
        line_stop = -2
    else:
        line_stop = -1
    folder, file_name = path
    file = open(folder+file_name,"r")
    line = file.readline()
    flavor = line[indexOf(line, ":"):line_stop].lower()
    if flavor == "marlin":
        row = readDataMarlin(file, line_stop)
        row[7] = fileName(file_name)
    file.close()
    return row
    pass

################################################################################
################################################################################
