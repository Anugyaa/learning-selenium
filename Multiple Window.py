import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class multiplewindows():
    def windows(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(4)
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Yatra Gift Cards']//img[@class='conta iner large-banner']").click()
        time.sleep(4)
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[normalize-space()='Shop Now']").click()
                time.sleep(4)
                driver.close()
                time.sleep(4)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Yatra Gift Cards']//img[@class='conta iner large-banner']").click()

a = multiplewindows()
a.windows()