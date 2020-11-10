# when i open my pc, proly I will do this.


import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time

#browser = webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s')
browser = webdriver.Chrome()

browser.get('https://www.youtube.com')

browser.execute_script("window.open()") # make a new tab
browser.switch_to.window(browser.window_handles[1]) # swich to the new tab
browser.get('https://septeni.udemy.com/organization/home/')

#login
# to catch the CSS selector
elem_login_id = browser.find_element_by_css_selector('#email')
elem_login_id.send_keys('shogo.uchida.0888@gmail.com')
elem_login_id.submit()


browser.execute_script("window.open()") # make a new tab
browser.switch_to.window(browser.window_handles[2]) # swich to the new tab
browser.get('https://www.xfree.ne.jp/login/member.php')

# login 1
# to catch the CSS selector
elem_login_id = browser.find_element_by_css_selector('#login_form > form > table > tbody > tr:nth-child(1) > td > input[type=text]')
elem_login_pass = browser.find_element_by_css_selector('#login_form > form > table > tbody > tr:nth-child(2) > td > input[type=password]')
# type in the elements
elem_login_id.send_keys('shogo.u.j.2896@gmail.com')
elem_login_pass.send_keys('Shogo0888')
# submit
elem_login_submit = browser.find_element_by_css_selector('#login_form > form > div > input[type=image]:nth-child(6)')
elem_login_submit.click()

# next page click
elem_panel_login = browser.find_element_by_css_selector('#main > div > div > div > div.inner > div > table > tbody > tr:nth-child(16) > td:nth-child(4) > a > img')
elem_panel_login.click()


# next tab
time.sleep(2)
browser.get('https://secure.xfree.ne.jp/server_wp/?action_user_index=true')
elem_dashboard = browser.find_element_by_css_selector('#main > div > div > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(7) > a')
elem_dashboard.click()

# next tab
time.sleep(2)
# this is proly impossible cuz chrome gives me warning message
browser.get('https://shogo2896.com/wp-admin/')
elem_advance = browser.find_element_by_css_selector('#details-button')
elem_advance.click()

elem_proceed = browser.find_element_by_css_selector('#proceed-link')
elem_proceed.click()


#login 2
time.sleep(3)
browser.get('https://shogo2896.com/wp-login.php?redirect_to=https%3A%2F%2Fshogo2896.com%2Fwp-admin%2F&reauth=1')

# to catch the CSS selector
elem_login_id2 = browser.find_element_by_css_selector('#user_login')
elem_login_pass2 = browser.find_element_by_css_selector('#user_pass')
# type in the elements
elem_login_id2.send_keys('shogo.u.j.2896@gmail.com')
elem_login_pass2.send_keys('Shogo0888')
# submit
elem_login_submit2 = browser.find_element_by_css_selector('#wp-submit')
elem_login_submit2.submit()

for i in range(2):
    browser.switch_to.window(browser.window_handles[-1])
    browser.close()





