import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class draganddrop():
    def dandd(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        elem1 = driver.find_element(By.XPATH, "//div[@id='draggable']")
        elem2 = driver.find_element(By.ID, "droppable")
        #ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        #ActionChains(driver).drag_and_drop_by_offset(elem1, 419, 238).perform()
        time.sleep(3)

dd = draganddrop()
dd.dandd()



