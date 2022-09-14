import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


class a():
    def dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dd_demo = driver.find_element(By.ID, "multi-select")
        dd_multi = Select(dd_demo)

        dd_multi.select_by_index(1)
        dd_multi.select_by_value()
        dd_multi.select_by_visible_text()
        
b = a()
b.dropdown()



