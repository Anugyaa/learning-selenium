import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class iframe():
    def frame(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        # Switch with iframe locator
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        # Switch with index
        driver.switch_to.frame(0)
        driver.find_element(By.ID, "navbtn_exercises").click()
        time.sleep(5)

a = iframe()
a.frame()