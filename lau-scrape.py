

def getLogin():
    login_info = {}
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_info["username"] = username
    login_info["password"] = password
    return login_info
