import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class a():
    def radio(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        time.sleep(4)
        d = driver.find_element(By.ID, "doi0").is_selected()
        print(d)
        driver.find_element(By.ID, "doi0").click()
        time.sleep(4)
        e = driver.find_element(By.ID, "doi0").is_selected()
        print(e)
        driver.find_element(By.ID, "doi1").click()
        time.sleep(4)



b = a()
b.radio()



