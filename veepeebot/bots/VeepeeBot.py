

from veepeebot.bots.SlowBot import SlowBot
from veepeebot.bots.SlowBot import SlowBot

class VeepeeBot(SlowBot):
    def __init__(self, hide):
        super().__init__(1, 1.5, hide)

    def connectToAccount(self, user, password):
        #self.go('http://www.veepee.fr')
        if self.exist('//*[@id="txtMail"]') and  self.exist('//input[@id="txtPassword"]'):
            self.write('//*[@id="txtMail"]', user)
            self.write('//input[@id="txtPassword"]', password)
            self.click('//*[@id="loginBt"]')

    def addToBasket(self, category, product):
        self.go('https://www.veepee.fr/gr/product/' + category + '/' + product)
        #self.bot.click('/html/body/div[1]/div/div[2]/div/div/section/div[2]/div/div[2]/div/div[4]/div/div[2]/div[2]/button')

