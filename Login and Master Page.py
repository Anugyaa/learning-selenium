import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://vapdev.xlbyte.com/#/home")
        time.sleep(5)
        driver.maximize_window()
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
        #popup
        driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator mat-raised-button mat-button-base']").click()
        time.sleep(4)
        #master
        driver.find_element(By.XPATH, "//div[@class='card-counter blue']").click()
        time.sleep(4)
        driver.find_element(By.ID, "mat-select-value-1").click()
        time.sleep(3)
        #skill
        driver.find_element(By.XPATH, "//span[normalize-space()='Skills']").click()
        time.sleep(4)
        # Add skill
        driver.find_element(By.XPATH, "//mat-icon[normalize-space()='add_circle_outline']").click()
        time.sleep(3)
        driver.find_element(By.ID, "mat-input-4").click()
        time.sleep(2)
        driver.find_element(By.ID, "mat-input-4").send_keys("PS")
        time.sleep(3)
        driver.find_element(By.ID, "mat-input-5").click()
        time.sleep(2)
        driver.find_element(By.ID, "mat-input-5").send_keys("Python Selenium")
        time.sleep(3)
        driver.find_element(By.XPATH, "//mat-icon[normalize-space()='save']").click()
        time.sleep(4)
        # Edit Skill
        driver.find_element(By.XPATH, "//mat-row[1]//mat-cell[1]//button[1]//span[1]//mat-icon[1]").click()
        time.sleep(3)
        #z = driver.find_element(By.ID, "mat-input-6").get_attribute("text")
        #print(z)
        #v = driver.find_element(By.ID, "mat-input-7").get_attribute("text")
        #print(v)
        driver.find_element(By.ID, "mat-input-7").click()
        time.sleep(2)
        driver.find_element(By.ID, "mat-input-7").clear()
        time.sleep(3)
        driver.find_element(By.ID, "mat-input-7").send_keys("Amazon Web Services - Amazon Services")
        time.sleep(3)
        #driver.find_element(By.ID, "mat-input-7").get_attribute("text")
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[normalize-space()='Save']").click()
        time.sleep(4)
        # option id
        driver.find_element(By.ID, "mat-input-2").click()
        time.sleep(2)
        driver.find_element(By.ID, "mat-input-2").send_keys("aws")
        time.sleep(5)
        # Description
        driver.find_element(By.ID, "mat-input-3").click()
        time.sleep(2)
        driver.find_element(By.ID, "mat-input-3").send_keys("Amazon Web Services - Is amazon service")
        time.sleep(4)


findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()