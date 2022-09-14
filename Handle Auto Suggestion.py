import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class a():
    def autosuggest(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        # First Way
        depart = driver.find_element(By.ID, "BE_flight_origin_city")
        depart.click()
        time.sleep(3)
        depart.clear()
        time.sleep(3)
        depart.send_keys("New Delhi")
        time.sleep(3)
        depart.send_keys(Keys.ENTER)
        time.sleep(3)
        # Second Way
        goingto = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        goingto.send_keys("New")
        time.sleep(4)
        c = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(c))
        for results in c:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break
b = a()
b.autosuggest()