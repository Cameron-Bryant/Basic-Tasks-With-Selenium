from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import tkinter as tk
import time
###login to LinkedIn, navigate to the jobs, enter a search and get the results. Proof of Concept
#webdriver init
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("window-size=1200x1000")
chrome_options.add_argument("--start-maximized")
url ='https://www.linkedin.com/home'
driver = webdriver.Chrome("C://Users//camer//Desktop//chromedriver.exe", options = chrome_options)
driver.get(url)
driver.implicitly_wait(10)
#home -> sign in
sign_in_button = driver.find_element_by_class_name('nav__button-secondary')
sign_in_button.click()
#email and password entry:
username = '------------'
password = '------------'
login_entry = driver.find_element_by_xpath("//input[@id='username']")
login_entry.send_keys(username)

pass_entry = driver.find_element_by_xpath("//input[@id='password']")
pass_entry.send_keys(password)

login_button = driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']")
login_button.click()
##navigate from homepage to jobs button
jobs_button = driver.find_element_by_xpath("//a[@data-test-global-nav-link='jobs']")
jobs_button.click()
#job search entry, city/state/zip entry, search button
search_entry =  driver.find_element_by_xpath("//input[@id='jobs-search-box-keyword-id-ember285']")
search_entry.send_keys("entry level data scientist")
location_entry =  driver.find_element_by_xpath("//input[@id='jobs-search-box-location-id-ember285']")
location_entry.send_keys("Evergreen, Colorado")
#click down messaging popup if it is open:
drop_messaging_popup_button = driver.find_elements_by_xpath("//button[@class='msg-overlay-bubble-header__control msg-overlay-bubble-header__control--new-convo-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view']")
drop_messaging_popup_button[-1].click()
search_button = driver.find_element_by_xpath("//button[@class='jobs-search-box__submit-button artdeco-button artdeco-button--3 jobs-home-soho__mvp-button']")
search_button.click()
#search and gather all jobs so they can be filtered
time.sleep(3)
job_listing_elems = driver.find_elements_by_xpath("//a[@data-control-id and @href and @class='disabled ember-view job-card-container__link job-card-list__title']")
job_titles = []

for elem in job_listing_elems:
    job_titles.append(elem.text)

for i in range(len(job_titles)):
    print(job_titles[i])
#display the jobs in a tkinter window. Going refactor and build this out into a way larger GUI
root = tk.Tk()
root.geometry("600x600")
root.title("Top Job Listings")
for i in range(len(job_titles)):
    tk.Label(root,text=job_titles[i]).grid(row=i, column=0)
root.mainloop()
