#! /usr/bin/env python

from sneakymud.screen import StartingScreen

class GameEngine(object):
    def __init__(self):
        self.updateScreen(StartingScreen.StartingScreen())

    def updateScreen(self, screen):
        self.screen = screen
        self.screen.attach(self)

    def getPlayerInput(self, playerinput):
        return self.screen.onPlayerInput(playerinput)

    def display(self):
        return self.screen.printDisplay()

if __name__ == '__main__':
    game = GameEngine()
    pin = ''
    while True:
        print game.display()
        pin = raw_input()
        if game.getPlayerInput(pin) == 'EXIT':
            break
        
