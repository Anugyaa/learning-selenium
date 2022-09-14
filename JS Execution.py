import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class js():
    def javascript(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver.get("https://training.rcvacademy.com/")
        driver.execute_script("window.open('https://training.rcvacademy.com/', '_self');")
        time.sleep(7)
        a = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", a)

JS = js()
JS.javascript()
