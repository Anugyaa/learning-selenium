# driver.get()
# driver.current_url
# driver.back()
# driver.forward()
# driver.refresh()
# driver.title
# driver.maximize_window()
# driver.minimize_window()
# driver.fullscreen_window()
# driver.close()
# driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class a():
    def b(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.rcvacademy.com")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT, 'ALL COURSES').click()
        driver.back()
        driver.forward()
        driver.minimize_window()
        time.sleep(5)
        driver.quit()

demobrowser = a()
demobrowser.b()

