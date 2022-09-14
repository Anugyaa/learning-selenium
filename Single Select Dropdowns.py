import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


class a():
    def dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        d = driver.find_element(By.NAME, "UserTitle")
        dd = Select(d)
        time.sleep(4)

        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(4)

        dd.select_by_index(1)
        time.sleep(4)

        dd.select_by_value("CxO_General_Manager_AP")
        time.sleep(4)

b = a()
b.dropdown()



