from sneakymud.loader import Loader
from sneakymud.player import Player
from sneakymud.screen import Screen, CityScreen

class CharacterCreationScreen(Screen):
    def __init__(self):
        self.name = "Dumbass"
        self.race = "human"
        self.raceList = Loader.getResourceList('races')
        super(CharacterCreationScreen, self).__init__(set=self.set, finish=self.finish)

    def printDisplay(self):
        stats = Loader.getRace(self.race)
        msg = (
"""Character Creation Menu
Name: {name}
Race: {race}

Health:		{hp}
Strength:	{str}
Agility:	{agi}
Intellect:	{int}

Possible Races: {races}

Commands
  - set name [name]
  - set race [race]
  - finish
  - exit
"""
)
        return msg.format(name=self.name,
                          race=self.race,
                          races=self.raceList,
                          hp=stats['hp'],
                          str=stats['str'],
                          int=stats['int'],
                          agi=stats['agi'])

    def _parseName(self, name):
        return name[:24]

    def _parseRace(self, race):
        for r in self.raceList:
            if race.startswith(r):
                return race
        return 'human'

    def _verify(self):
        if len(self.name) > 0 and self.race in self.raceList:
            return True
        return False

    def set(self, tokens):
        option = tokens[0]
        if option == 'name':
            self.name = self._parseName(''.join(tokens[1:]))
        if option == 'race':
            self.race = self._parseRace(tokens[1:])

    def finish(self, tokens):
        if self._verify():
            self.gameEngine.updateScreen(CityScreen.CityScreen('libens'))
