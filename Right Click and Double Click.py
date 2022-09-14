import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class doubleclick():
    def rightclick(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(4)
        # Right Click
        # achains = ActionChains(driver)
        # right_click = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        # copy = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        # achains.context_click(right_click).perform()
        # time.sleep(2)
        # copy.click()
        # time.sleep(2)

        # Double Click
        achains1 = ActionChains(driver)
        double_click = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains1.double_click(double_click).perform()
        time.sleep(3)


a = doubleclick()
a.rightclick()