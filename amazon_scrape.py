from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from mysql.connector import connect, Error
from bs4 import BeautifulSoup
import time
#goal: collect Amazon reviews to use for sentiment analysis.
#driver initialization
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("window-size=1200x1000")
url ='https://www.amazon.com/'
driver = webdriver.Chrome("C://Users//camer//Desktop//chromedriver.exe", options = chrome_options)
driver.get(url)
driver.implicitly_wait(30)
#get search and search it
search = input(":>")#search
search_bar = driver.find_element_by_id('twotabsearchtextbox')
search_bar.send_keys(search)
search_button = driver.find_element_by_id('nav-search-submit-button')
search_button.click()
#get text from product and the link element
product_texts = driver.find_elements_by_class_name("a-size-base-plus.a-color-base.a-text-normal")
product_texts = [product_texts[i].text for i in range(len(product_texts))]
#iterate through each link, click, let it load, then gather more data
product_reviews = []
reviews = []
print(len(product_texts))

for i in range(len(product_texts)):
    try:#have to find each element each time because they become stale when page is left
        next_page = driver.find_element_by_link_text(product_texts[i])
        if next_page.is_displayed() and next_page.is_enabled():#make sure element is interactable
            next_page.click()
            product_reviews = driver.find_elements_by_class_name("a-expander-content.reviewText.review-text-content.a-expander-partial-collapse-content")
            product_reviews = [product_reviews[i].text for i in range(len(product_reviews))]
            reviews.append(product_reviews)
            driver.back()
            print(i)#stale element would say somethings wrong and no reviews would show up, no such happens every now and then from the page changing.
    except (StaleElementReferenceException, NoSuchElementException):
        reviews.append(0)
print(reviews)
#clean the data:
cleaned_reviews = []
for i in range(len(reviews)):#0 if element threw an error, [] if no reviews were there
    if reviews[i] != 0 and reviews[i] != []:
        cleaned_reviews.append(reviews[i])
print("Uncleaned reviews Len:>" + str(len(reviews)))
print("Cleaned reviews Len:>" + str(len(cleaned_reviews)))
print(cleaned_reviews)
try:#make a database, make a table in the database
    with connect(host='localhost',
                 user= input("Username:>"),
                 password= input("Password:>"),
                 database = "amazon_reviews",
    ) as connection:
        db_create = "CREATE DATABASE amazon_reviews"
        table_create =  "CREATE TABLE amazon_reviews.raw_reviews(review TEXT)"
        with connection.cursor() as cursor:
            #cursor.execute(db_create)
            #cursor.execute(table_create)
            sql = 'INSERT INTO raw_reviews (review) VALUES (%s)'
            #insert data/clear data from test runs
            cursor.execute("TRUNCATE TABLE raw_reviews")#clear the table
            connection.commit()
            for i in range(len(cleaned_reviews)):
                for j in range(len(cleaned_reviews[i])):
                    val = cleaned_reviews[i][j]
                    cursor.execute(sql, (val,))
                    connection.commit()#tuple above, single element is (elem,)
            cursor.close()
            connection.close()
            
except Error as e:
    print(e)
    connection.rollback()
