import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class mousehover():
    def hover(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(4)
        morebutton = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        time.sleep(4)
        myaccount = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        time.sleep(4)
        achains = ActionChains(driver)
        achains.move_to_element(myaccount).perform()
        time.sleep(4)
        achains.move_to_element(morebutton).perform()
        time.sleep(4)
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        time.sleep(4)

a = mousehover()
a.hover()