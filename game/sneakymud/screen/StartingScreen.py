from sneakymud.screen import Screen, CharacterCreationScreen

class StartingScreen(Screen):
    def __init__(self):
        welcome = "Welcome to Aaron's MUD -- Its going to be a terrible ride"
        super(StartingScreen, self).__init__(
		newgame=self.newGame
        )

    def printDisplay(self):
        return (
"""
Welcome to my shitty MUD, Have fun

commands
  - newgame
  - exit
""")

    def newGame(self, tokens):
        temp = CharacterCreationScreen.CharacterCreationScreen()
        self.gameEngine.updateScreen(temp)
