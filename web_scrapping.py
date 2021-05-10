#selenium import
import selenium
from selenium import webdriver

#원활한 동작을 위한 옵션 설정
chrome_options = webdriver.ChromeOptions()    #설정을 원활하게 하기 위해 설정
chrome_options.add_argument('--headless')     #colab을 통해 웹 window를 띄울 수 없으므로 설정하는 것
chrome_options.add_argument('--no-sandbox')   #보안기능을 비활성화
chrome_options.add_argument('--disable-dev-shm-usage')    #제한된 자원문제를 해결하기위함.
driver = webdriver.Chrome('chromedriver', options = chrome_options)

driver.get('https://www.nate.com')