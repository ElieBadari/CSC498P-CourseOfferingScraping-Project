from selenium import webdriver as wd
from selenium.webdriver.common.by import By

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

    userlogin = chrome.find_element(by="id",value="username")
    passlgin = chrome.find_element(by="id",value="password")

    userlogin.send_keys(login_info["username"])
    passlogin.send_keys(login_info["password"])

    chrome.find_element(by=By.CSS_SELECTOR,value='[type="submit"]').click()

    chrome.get("https://banweb.lau.edu.lb/prod/bwskfcls.p_sel_crse_search")
    term = Select(chrome.find_element(by="id",value="term_input_id"))
    term.select_by_visible_text("Fall 2023 (View only)")

    chrome.find_element(by=By.CSS_SELECTOR,value='[value="Submit"]').click()
    chrome.find_element(by=By.CSS_SELECTOR,value='[value="Advanced Search"]').click()
