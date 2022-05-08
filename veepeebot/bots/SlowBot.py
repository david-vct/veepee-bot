from veepeebot.bots.Bot import Bot
from time import sleep
import random

class SlowBot(Bot):
    def __init__(self, timeMin, timeMax, hide):
        super().__init__(hide)
        self.timeMin = timeMin
        self.timeMax = timeMax

    def sleep(self):
        time = random.uniform(self.timeMin, self.timeMax)
        sleep(time)
    
    def click(self, xpath):
        self.sleep()
        super().click(xpath)

    def write(self, xpath, text):
        self.sleep()
        super().write(xpath, text)
