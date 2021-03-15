from selenium import webdriver
import urllib.request
import random
from selenium.webdriver.common.keys import Keys

restaurant = random.randint(0, 13)
print(restaurant)

driver = webdriver.Chrome('chromedriver.exe')
words = ["mcdonalds", "kfc", "dominos", "subway",
         "burger king", "pizza hut", "krispy kreme"]
word = words[0]+" foods"
url = "http://images.google.com/search?q="+word+"&tbm=isch&sout=1"
driver.get(url)
imageXpathSelector = '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img'
img = driver.find_element_by_xpath(imageXpathSelector)

src = (img.get_attribute('src'))
urllib.request.urlretrieve(src, word+".jpg")
driver.close()
