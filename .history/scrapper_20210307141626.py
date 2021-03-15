from selenium import webdriver
import urllib
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
word = "coffee"
url = "http://images.google.com/search?q="+word+"&tbm=isch&sout=1"
driver.get(url)
imageXpathSelector = '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img'
img = driver.find_element_by_xpath(imageXpathSelector)

src = (img.get_attribute('src'))
urllib.urlretrieve(src, word+".jpg")
driver.close()
