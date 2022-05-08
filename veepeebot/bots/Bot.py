from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Bot:
    def __init__(self, hide):
        # Configuration
        options = Options()
        if hide:
            options.add_argument('--headless')

        # Open browser
        self.driver = webdriver.Chrome(options=options)
    
    def shutdown(self):
        self.driver.close()

    def go(self, url):
        self.driver.get(url)

    def click(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click() 

    def write(self, xpath, text):
        self.driver.find_element(By.XPATH, xpath).send_keys(text)