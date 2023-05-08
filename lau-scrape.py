from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from getpass import getpass
from selenium.webdriver.support.ui import Select
import csv


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
    with open("output.csv", "w") as output_file:
        writer = csv.writer(output_file)
        headers = rows[1]
        header_cells = list()
        header_cells = [cell.string.strip() if cell.string else i.string.strip() for cell in headers.findAll(["td", "th"]) for i in cell.findAll()]
        writer.writerow([cell for i, cell in enumerate(header_cells) if i != 0 and i < 20])
        
        for i in range(2, len(rows)):
            cells = list()
            row = rows[i]
            for cell in row.findAll(["td", "tr"]):
                if row.findAll(["td", "tr"]).index(cell) != 0 and row.findAll(["td", "tr"]).index(
                        cell) < 20:
                    if cell.string:
                        cells.append(cell.string.strip())
                    else:
                        children = cell.findAll()
                        for i in children:
                            cells.append(i.string.strip())
            if len(cells) > 4:
                if eval(cells[4]) == 2:
                    writer.writerow(cells)
            else:
                writer.writerow(cells)

        

login_info = getLogin()
course_offerings = getCourseOfferings(login_info)
extractToCSV(course_offerings)

