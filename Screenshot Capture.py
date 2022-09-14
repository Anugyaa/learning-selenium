import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class screenshot():
    def ss(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        continuedemo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continuedemo.screenshot(".\\test.png")
        continuedemo.click()
        time.sleep(4)
        driver.get_screenshot_as_file(".\\error.jpg")
        driver.save_screenshot(".\\test1.png")

a = screenshot()
a.ss()