import json

def importFile():
    with open("profiles.json", "r") as f:
        profiles = f.read()
    return json.loads(profiles)

def exportFile(profiles):
    profiles = [
        {
            "name":"Harsh Sharma",
            "username":"BluNyte",
            "email":"goharsh007@gmail.com",
            "password":"blahblah"
        }
    ]
    
    with open("profiles.json", "w+") as f:
        f.write(json.dumps(profiles))

def isloginOK(email , password):
    profiles = importFile()

    tmp = []

    #Check email
    for i in profiles:
        tmp.append(i)
    
    if email.lower() in tmp:
        if profiles[tmp.index(email.lower())]["password"] == password:
            return True
        return False, "Wrong Password!"
    return False, "Wrong Email Address!"
            


print(importFile()[0]["name"])