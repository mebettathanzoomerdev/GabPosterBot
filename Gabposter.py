# GabPoster
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from pathlib import Path

#need to disable anything that can popup
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=option)

driver.get("https://gab.com")

#Login Function
search = driver.find_element_by_css_selector("[class='_2IIhM _8iyry _1E64f _2mtbj _2QlHj _2YiJx _UuSG _3Ujf8 yigUm ALevz _1XpDY _81_1w _1o5Ge ig9Cs _1srFG _37dq4 _3mBt0 _3TwRa SslQJ _2G0fo _2dPcT")
search.send_keys(Keys.RETURN)
search = driver.find_element_by_id("user_email")
# insert email address
search.send_keys("YOUR EMAIL")
search = driver.find_element_by_id("user_password")
# insert password
search.send_keys("YOUR PASSWORD")
search.send_keys(Keys.RETURN)

# gets new link to post
driver.get("https://gab.com/compose")
search = driver.find_element_by_css_selector("[class='_UuSG yigUm OYzHA _2-XMp _1o5Ge _81_1w _1kAFo _2ZzNB w77Za _3PLpz SslQJ CS7dE _3tKl_ SQXrR']")
search.send_keys(Keys.RETURN)
# insert your content you want to be posted
search.send_keys("CONTENT FOR POST")
search = driver.find_element_by_css_selector("[class='_3hcKE SslQJ _1E64f _1KT4G _UuSG _3Ujf8 yigUm ALevz _1XpDY _81_1w _2WUpZ _28TaQ _3mBt0 _33UDc _1unCp SslQJ w77Za _1sTgh']")
search.send_keys(Keys.RETURN)

# goes to sleep after 5 seconds
time.sleep(5)
# Quits after sleep completed
driver.quit() 
