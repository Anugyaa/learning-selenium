import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class jspopup():
    def alerts(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame("iframeResult")
        time.sleep(2)

        # Accept alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)

        # Dismiss alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        driver.switch_to.alert.dismiss()
        time.sleep(3)

        # Enter text
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        print(driver.switch_to.alert)
        driver.switch_to.alert.send_keys("Anugyaa")
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)


a = jspopup()
a.alerts()


