import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class a():
    def b(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        time.sleep(5)
        #username
        # driver.find_element(By.ID,"login-input").send_keys('anugya02@gmail.com')
        # time.sleep(5)
        text = driver.find_element(By.LINK_TEXT, "Yatra for Business").get_attribute("text")
        print(text)
        time.sleep(5)

findbyid = a()
findbyid.b()