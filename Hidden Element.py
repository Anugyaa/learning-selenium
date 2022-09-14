import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class a():
    def b(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        c = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(c)
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        d = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(d)

hiddenelement = a()
hiddenelement.b()


