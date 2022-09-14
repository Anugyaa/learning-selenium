import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class a():
    def yatra(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/hotels")

        driver.find_element(By.XPATH, "//label[normalize-space()='Traveller and Hotel']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(5)
        b = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(b)
        time.sleep(5)

        driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]").click()
        time.sleep(5)
        c = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(c)

hiddenelement = a()
hiddenelement.yatra()


