from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
#first selenium project so lots of notes too
#allows browser to stay open after all the commands are done
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
#make a driver and give it those options
driver = webdriver.Chrome("C://Users//camer//Desktop//chromedriver.exe", options=chrome_options)
driver.get("https://www.coloradodls.org/login")
#give it time to load the page
time.sleep(1)#navigate to the iframe that contains the login box
#have to navigate to the frame to access it
driver.switch_to.frame(driver.find_element_by_class_name('_3HLqS'))
#find elements
pass_box = driver.find_element_by_name('tbPassword')
login_button = driver.find_element_by_name('btLogin')
user_box = driver.find_element_by_name('tbLogin')

#password and username 
username = #########
password = #########
#send_keys puts info into the fields
user_box.send_keys(username)
pass_box.send_keys(password)
login_button.click()#.click() clicks a button
fem_hrefs = driver.find_elements_by_xpath('//a[@href="FEMessages.aspx"]')
#def find_right_href(hrefs, corr_text):
#    for i in range(len(hrefs)):
#        if hrefs[i].text == corr_text:
#            return i
#ind =  find_right_href(fem_hrefs, '4')#change '4' if need to find again to the num on the website
##num_messages = fem_hrefs[ind].text
#print(num_messages)
#print(ind)
num_messages = fem_hrefs[1].text
print(num_messages)

#all links in class box go to the same page, so i will use english
time.sleep(1)
enter_link = driver.find_element_by_link_text("English 12 - Semester 2")
enter_link.click()
#now logged into main page for my classes
time.sleep(15)
