from veepeebot.bots.VeepeeBot import VeepeeBot
from time import sleep

class VeepeeBotController:
    def __init__(self, user, password):
        # Variables initialisation
        self.user = user
        self.password = password

        # Bot initialisation
        self.bot = VeepeeBot(False)


    def makeMoney(self):
        # Connexion
        self.bot.go('http://www.veepee.fr')
        self.bot.connectToAccount(self.user, self.password)


        json = self.bot.get('//*[@id="__NEXT_DATA__"]').get_attribute('innerHTML')
        
        #sleep(2)
        #self.bot.go('https://www.veepee.fr/gr/home/fashion')

        # Add elements to basket
        #self.addToBasket('224918', '44084617')

        
        sleep(10)
        self.bot.shutdown()