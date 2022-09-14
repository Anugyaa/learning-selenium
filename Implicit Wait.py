import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class implicitwait():
    def iw(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.ID, "username").send_keys("Anugyaa")
        driver.find_element(By.ID, "password").send_keys("Shrivastava")

a = implicitwait()
a.iw()
