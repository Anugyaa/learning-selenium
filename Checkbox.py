import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class a():
    def yatra(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/flights")
        driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").click()
        time.sleep(5)

        driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").click()
        time.sleep(5)
        d = driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").is_selected()
        print(d)

b = a()
b.yatra()



