from selenium import webdriver
import urllib.request
import random
import time
from selenium.webdriver.common.keys import Keys

current_time = time.strptime(time.ctime(time.time())).tm_hour
if current_time < 12:
    foodname = "BreakFast Ready - "
elif current_time > 12 and current_time < 18:
    foodname = "Lunch Ready - "
elif current_time >= 18:
    foodname = "Dinner Ready - "

restaurant = random.randint(0, 7)

driver = webdriver.Chrome('chromedriver.exe')
words = ["mcdonalds", "kfc", "dominos", "subway",
         "burger king", "pizza hut", "krispy kreme"]
word = words[restaurant]+" foods"
print("Your Rrestaurant : "+word)

url = "http://images.google.com/search?q="+word+"&tbm=isch&sout=1"
driver.get(url)
imageXpathSelector = '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img'
img = driver.find_element_by_xpath(imageXpathSelector)

src = (img.get_attribute('src'))
urllib.request.urlretrieve(src, foodname + word+".jpg")
driver.close()
