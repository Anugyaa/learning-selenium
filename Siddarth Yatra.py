import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        time.sleep(5)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        time.sleep(5)
        driver.find_element(By.ID,'login-input').send_keys('sid.bhadoriya@gmail.com')
        time.sleep(5)


fid = DemoFindElementByID()
fid.locate_by_id_demo()