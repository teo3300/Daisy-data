def idIs(username):
    from var import userdata
    for user in userdata:
        if userdata[user]["username"] == username:
            return user
    return "error"

################################################################################
def setStatus(str_id, status):
    from var import userdata
    from initFunctions import updateJson
    userdata[str_id]["status"] = status
    updateJson(userdata, "userdata.json")
    print(str_id+"'s status is set to", status)
    pass

################################################################################
def setGroup(str_id, group):
    from var import userdata
    from initFunctions import updateJson
    userdata[str_id]["group"] = group
    updateJson(userdata, "userdata.json")
    print(str_id+"' group set to", group)
    pass
