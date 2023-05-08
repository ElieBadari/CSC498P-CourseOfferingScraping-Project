from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from getpass import getpass
from selenium.webdriver.support.ui import Select


def getLogin():
    login_info = {}
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    login_info["username"] = username
    login_info["password"] = password
    return login_info

def getCourseOfferings(login_info):
    chrome = wd.Chrome()
    chrome.get("https://banweb.lau.edu.lb/")

    userlogin = chrome.find_element(by="id",value="username")
    passlogin = chrome.find_element(by="id",value="password")

    userlogin.send_keys(login_info["username"])
    passlogin.send_keys(login_info["password"])

    chrome.find_element(by=By.CSS_SELECTOR,value='[type="submit"]').click()

    chrome.get("https://banweb.lau.edu.lb/prod/bwskfcls.p_sel_crse_search")
    term = Select(chrome.find_element(by="id",value="term_input_id"))
    term.select_by_visible_text("Fall 2023 (View only)")

    chrome.find_element(by=By.CSS_SELECTOR,value='[value="Submit"]').click()
    chrome.find_element(by=By.CSS_SELECTOR,value='[value="Advanced Search"]').click()

    subject = Select(chrome.find_element(by="id", value="subj_id"))
    subject.select_by_visible_text("Computer Science")

    chrome.find_element(by=By.CSS_SELECTOR,value='[value="Section Search"]').click()
    
    offerings = chrome.page_source
    return offerings

def extractToCSV(offerings):
    html = BeautifulSoup(offerings,"html.parser")
    table = html.find("table",{"class":"datadisplaytable"})
    rows = list()
    for row in table.findAll("tr"):
        rows.append(row)
    
    

login_info = getLogin()
course_offerings = getCourseOfferings(login_info)

