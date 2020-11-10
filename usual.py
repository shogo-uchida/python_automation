# when i open my pc, proly I will do this.

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
import pyautogui

# i think if i have more, id better use object class



##################### each function ###########################

def open_web(browser, urls):
    for url in urls:
        if url == urls[0]:
            browser.get(url)
        else:
            browser.execute_script("window.open()")
            browser.switch_to.window(browser.window_handles[-1])
            browser.get(url)

def login_id(browser, css_selector, login_id, css_submit):
    elem_login_id = browser.find_element_by_css_selector(css_selector)
    elem_login_id.send_keys(login_id)
    if css_submit == None:
        elem_login_id.submit()
    else:
        elem_login_submit = browser.find_element_by_css_selector(css_submit)
        elem_login_submit.click()

def login_id_pass(browser, css_selector_id, css_selector_pass, login_id, login_pass, css_submit):
    elem_login_id = browser.find_element_by_css_selector(css_selector_id)
    elem_login_id.send_keys(login_id)
    elem_login_pass = browser.find_element_by_css_selector(css_selector_pass)
    elem_login_pass.send_keys(login_pass)
    elem_login_submit = browser.find_element_by_css_selector(css_submit)
    elem_login_submit.click()


def click(browser, css_selector):
    elem = browser.find_element_by_css_selector(css_selector)
    elem.click()

def click_class(browser, CssClass):
    elem = browser.find_element_by_class_name(CssClass)
    elem.click()

def click_Id(browser, CssId):
    elem = browser.find_element_by_class_name(CssId)
    elem.click()

def open_another_web(browser, css_selector):
    browser.get(css_selector)

def switch_tab(browser, page):
    browser.switch_to.window(browser.window_handles[page])

def click_GUI(screenshot):
    width, height = pyautogui.locateCenterOnScreen(screenshot)





################ total function ###################






# def udemy(page):
#     switch_tab(page)
#     login_id('#email', 'shogo.uchida.0888@gmail.com', None)

# def gmail(page):
#     switch_tab(page)
#     login_id('#identifierId', 'shogo.uchida.0888@gmail.com', '#identifierNext > span')
#     #time.sleep(2)
#     #login_id('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'\
#      #        , 'Shogo0888', '#passwordNext > span > span')

def adjust(browser, page):
    switch_tab(browser, page)
    time.sleep(2)
    adjustId = ['#email' \
        , '#password' \
        , 'global_team@septeniamerica.com' \
        , 'septeni' \
        , 'body > div > div > div.content.content-login.flex-one > div.form-container.animate > div > form > div:nth-child(5) > button']
    login_id_pass(browser, *adjustId)
    time.sleep(5)


def af_EME(browser, page):
    switch_tab(browser,page)
    afId = ['#user-email' \
        , '#password-field' \
        , 'global_team@septeniamerica.com' \
        , 'Septeni777!' \
        , '#login-form > div.form-buttons > button']
    login_id_pass(browser, *afId)
    time.sleep(5)
    click(browser, '#app > div > div.app-frame-body > div.af-content > div > div > div > div.af-container.af-seamless-container.af-fixed-filter-container > div > div > div > div > div > div.af-dropdown-container.input-container > div > div > div > div.af-dropdown-input > div')
    time.sleep(1.5)
    click(browser, '#dropdown-list-0 > div > div:nth-child(3) > div')
    time.sleep(1)
    click(browser, '#reportrange')
    time.sleep(1)
    click(browser, 'body > div.daterangepicker.dropdown-menu.opensleft > div.ranges > button:nth-child(5)')


def af_Bokujo(browser, page):
    switch_tab(browser, page)
    afId = ['#user-email' \
        , '#password-field' \
        , 'global_team@septeniamerica.com' \
        , 'Septeni777!' \
        , '#login-form > div.form-buttons > button']
    login_id_pass(browser, *afId)
    time.sleep(5)
    click(browser, '#app > div > div.app-frame-body > div.af-content > div > div > div > div.af-container.af-seamless-container.af-fixed-filter-container > div > div > div > div > div > div.af-dropdown-container.input-container > div > div > div > div > div')
    time.sleep(1.5)
    click(browser, '#dropdown-list-0 > div > div:nth-child(2) > div')
    time.sleep(1)
    click(browser, '#reportrange')
    time.sleep(1)
    click(browser, 'body > div.daterangepicker.dropdown-menu.opensleft > div.ranges > button:nth-child(5)')


def af_Mildom(browser,page):
    switch_tab(browser, page)
    afId = ['#user-email' \
        , '#password-field' \
        , 'account_gr@septeni.co.jp' \
        , 'Appsflyersepteni2019!' \
        , '#login-form > div.form-buttons > button']
    login_id_pass(browser, *afId)
    time.sleep(6)
    click(browser, '#app > div > div.app-frame-body > div.af-content > div > div > div > div.af-container.af-seamless-container.af-fixed-filter-container > div > div > div > div > div > div.af-dropdown-container.input-container > div > div > div > div.af-dropdown-input > div')
    time.sleep(3)
    click(browser, '#dropdown-list-0 > div > div:nth-child(6) > div')
    time.sleep(1)
    click(browser, '#reportrange')
    time.sleep(1)
    click(browser, 'body > div:nth-child(8) > div.ranges > button:nth-child(5)')


def af_Qoo10(browser, page):
    switch_tab(browser, page)
    afId = ['#user-email' \
        , '#password-field' \
        , 'account_gr@septeni.co.jp' \
        , 'Appsflyersepteni2019!' \
        , '#login-form > div.form-buttons > button']
    login_id_pass(browser, *afId)
    time.sleep(6)
    click(browser, '#app > div > div.app-frame-body > div.af-content > div > div > div > div.af-container.af-seamless-container.af-fixed-filter-container > div > div > div > div > div > div.af-dropdown-container.input-container > div > div > div > div.af-dropdown-input > div')
    time.sleep(3)
    click(browser, '#dropdown-list-4 > div > div:nth-child(8) > div')
    time.sleep(1)
    click(browser, '#reportrange')
    time.sleep(1)
    click(browser, 'body > div:nth-child(8) > div.ranges > button:nth-child(5)')


def af_17(browser, page):
    switch_tab(browser, page)
    afId = ['#user-email' \
        , '#password-field' \
        , 'account_gr@septeni.co.jp' \
        , 'Appsflyersepteni2019!' \
        , '#login-form > div.form-buttons > button']
    login_id_pass(browser, *afId)
    time.sleep(6)
    click(browser, '#app > div > div.app-frame-body > div.af-content > div > div > div > div.af-container.af-seamless-container.af-fixed-filter-container > div > div > div > div > div > div.af-dropdown-container.input-container > div > div > div > div.af-dropdown-input > div')
    time.sleep(3)
    click(browser, '#dropdown-list-4 > div > div:nth-child(12) > div')
    time.sleep(1)
    click(browser, '#reportrange')
    time.sleep(1)
    click(browser, 'body > div:nth-child(8) > div.ranges > button:nth-child(5)')




##########################  combined func ###############################

##################### GOOGLE DOES NOT WORK IN THIS WAY ########################

# def file_open(browser):
#     urls = ['https://docs.google.com/spreadsheets/d/1ifNcRfacyCeyisbyeQ0AjbB5hIhCfMDxYUgzwqGk8-k/edit?ts=5ecb6cf1#gid=1792753660'\
#             , 'https://docs.google.com/spreadsheets/d/12PVaPcxWHti0HETSvfjctFj_b1LqiAh0TDdLYjT1cfA/edit#gid=1391190528'\
#             , 'https://docs.google.com/spreadsheets/d/1ZqVopmP1Wj0eCDvENA7G-U5GZMtleRvGMUKqc_a3w2I/edit#gid=537291861']
#
#     open_web(browser, urls)



def run_ad_sepGP(browser):
    # put the URL you wanna open <Adjust, SEP GP only>
#    urls = ['https://dash.adjust.com/#/login', 'https://hq1.appsflyer.com/dashboard/export/id890664813'\
#            , 'https://hq1.appsflyer.com/dashboard/export/id1455950606']

    urls = ['https://hq1.appsflyer.com/dashboard/export/id890664813']

    open_web(browser, urls)

# put the func you wanna excute in order of above URL.
#    tabs = [adjust, af_EME, af_Bokujo]
    tabs = [af_EME]

    page = 0
    for tab in tabs:
        tab(browser, page)
        page += 1




def run_sepJP(browser):
# put the URL you wanna open <SEP JP>
    urls = ['https://hq1.appsflyer.com/dashboard/export/id1480809171', 'https://hq1.appsflyer.com/dashboard/export/id1054840040'\
            , 'https://hq1.appsflyer.com/dashboard/export/id988259048', ]
    open_web(browser, urls)

# put the func you wanna excute in order of above URL.
    tabs = [af_Mildom, af_Qoo10, af_17]

    page = 0
    for tab in tabs:
        tab(browser, page)
        page += 1


################### run #####################


def main():
    browser1 = webdriver.Chrome()
    browser1.maximize_window()
    run_ad_sepGP(browser1)

    browser2 = webdriver.Chrome()
    browser2.maximize_window()
    run_sepJP(browser2)

main()
