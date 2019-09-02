def idIs(username):
    from var import userdata
    for user in userdata:
        if userdata[user]["username"] == username:
            return user
    return "error"
    pass

################################################################################
def setStatus(str_id, status):
    from var import userdata
    from initFunctions import updateJson
    userdata[str_id]["status"] = status
    updateJson(userdata, "userdata.json")
    print(str_id+"'s status is set to", status)
    pass
