from veepeebot.bots.SlowBot import SlowBot
from time import sleep

class VeepeeBotController:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.bot = SlowBot(1, 1.5, False)

    def connectToAccount(self):
        exit()
        self.driver.find_element('id', 'txtMail').send_keys(self.user)
        self.driver.find_element('id', 'txtPassword').send_keys(self.password)
        self.driver.find_element('id', 'stayConnected').click()
        self.driver.find_element('id', 'loginBt').click()

    def addToBasket(self, category, product):
        self.bot.go('https://www.veepee.fr/gr/product/' + category + '/' + product)
        #self.bot.click('/html/body/div[1]/div/div[2]/div/div/section/div[2]/div/div[2]/div/div[4]/div/div[2]/div[2]/button')

    def makeMoney(self):
        try:
            # Connexion
            self.bot.go('http://www.veepee.fr')
            self.bot.write('//*[@id="txtMail"]', self.user)
            self.bot.write('//input[@id="txtPassword"]', self.password)
            self.bot.click('//*[@id="loginBt"]')
            
            sleep(2)
            self.bot.go('https://www.veepee.fr/gr/home/fashion')

            # Add elements to basket
            #self.addToBasket('224918', '44084617')

        except Exception as exception:
            print('Exception:', exception)
        
        sleep(10)
        self.bot.shutdown()