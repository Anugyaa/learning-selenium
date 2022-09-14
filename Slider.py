import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class slider():
    def sliding(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.snapdeal.com/products/mobiles-cases-covers?sort=plrty")
        driver.maximize_window()
        time.sleep(3)
        elem1 = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
        elem2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")
        ActionChains(driver).drag_and_drop_by_offset(elem1, 50, 0).perform()
        time.sleep(3)
        #ActionChains(driver).click_and_hold(elem2).pause(1).move_by_offset(-50, 0).release().perform()
        #ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(80, 0).release().perform()
        ActionChains(driver).drag_and_drop_by_offset(elem2, -30, 0).perform()
        time.sleep(4)

a = slider()
a.sliding()



