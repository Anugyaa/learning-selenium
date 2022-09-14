import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class a():
    def b(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        time.sleep(2)
        c = driver.find_element(By.ID,"login_button").is_enabled()
        print(c)
        time.sleep(2)
        #username
        driver.find_element(By.ID,"user_name").send_keys('anugya02')
        time.sleep(2)
        #password
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("123456")
        time.sleep(2)
        d = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(c)


findbyid = a()
findbyid.b()