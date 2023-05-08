from selenium import webdriver as wd

def getLogin():
    login_info = {}
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_info["username"] = username
    login_info["password"] = password
    return login_info

def getCourseOfferings(login_info):
    chrome = wd.Chrome()
    chrome.get("https://banweb.lau.edu.lb/")
    chrome.find_element(by="id",value="username").send_keys(login_info["username"])
    chrome.find_element(by="id",value="password").send_keys(login_info["password"])
    chrome.find_element(by="css selector",value='[type="submit"]').click()