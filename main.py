import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class a():
    def b(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://vapdev.xlbyte.com/#/home")
        time.sleep(5)
        #username
        driver.find_element(By.ID,"mat-input-0").send_keys('anugya02@gmail.com')
        time.sleep(5)
        #password
        driver.find_element(By.XPATH, "//input[@id='mat-input-1']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("123")
        time.sleep(2)
        #login
        driver.find_element(By.ID, "loginSubmit").click()
        time.sleep(5)

findbyid = a()
findbyid.b()