from selenium import webdriver
import urllib.request
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
words = ["mcdonalds"]
word = words[0]+"food"
url = "http://images.google.com/search?q="+word+"&tbm=isch&sout=1"
driver.get(url)
imageXpathSelector = '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img'
img = driver.find_element_by_xpath(imageXpathSelector)

src = (img.get_attribute('src'))
urllib.request.urlretrieve(src, word+".jpg")
driver.close()
