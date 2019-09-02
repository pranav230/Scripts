from selenium import webdriver
import time
browser = webdriver.Chrome("Full Path for chromedriver file with extension")

url = "Url for the specific site"
browser.get(url)

username = 'Add the username here'
browser.find_element_by_id('Find the element id for username through inspect element').send_keys(username)

password = 'Add password here'
browser.find_element_by_id('Find the element id for password through inspect element').send_keys(password)

xpath= 'Find the xpath or element id for username through inspect element'
# Or you can do browser.find_element_by_id(submitButton).click()  to click the button if you have the id of the submit button
browser.find_element_by_xpath(xpath).click()

#this is to wait for the site to open 
time.sleep(30)
#and then quit the browser by itself
browser.quit()