from sneakymud.loader import Loader
from sneakymud.player import Player
from sneakymud.screen import Screen

class LocationScreen(Screen):
    def __init__(self, locationName):
        self.locRaw = Loader.getLocation(locationName)
        if not self.cityRaw:
            raise Exception
        super(CityScreen, self).__init__(travel=self.travel, encounter=self.encounter, talk=self.talk)

    def printDisplay(self):
        npcs = '\n'.join(['    - {x}'.format(x=i) for i in self.locRaw['npcs']])
        msg = (
"""
wandering through {name}
{desc}

  - encounter
  - talk
{npcs}
"""
).format(desc=self.locRaw['desc'], name=self.locRaw['name'])
        return msg

    def travel(self, travel):
        pass

    def talk(self, npc):
        pass

    def encounter(self, tokens):
        pass
