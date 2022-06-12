from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Bot:
    def __init__(self, hide):
        # Configuration
        options = Options()
        if hide:
            options.add_argument('--headless')

        # Open browser
        self.driver = webdriver.Chrome(options=options)
    
    
    # METHODS
    
    def get(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def getContent(self, xpath):
        return self.get(xpath).get_attribute('innerHTML')

    def exist(self, xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False


    # ACTIONS

    def go(self, url):
        self.driver.get(url)

    def click(self, xpath):
        self.get(xpath).click() 

    def write(self, xpath, text):
        self.get(xpath).send_keys(text)

    def shutdown(self):
        self.driver.close()