from veepeebot.bots.VeepeeBotController import VeepeeBotController
import json

def run() :
    # Load data
    f = open('veepeebot/resources/credentials.json')
    data = json.load(f)
    user = data['user']
    password = data['password']

    # Execute my bot
    controller = VeepeeBotController(user, password)
    controller.makeMoney()