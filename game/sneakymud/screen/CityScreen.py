from sneakymud.loader import Loader
from sneakymud.player import Player
from sneakymud.screen import Screen

class CityScreen(Screen):
    def __init__(self, cityName):
        self.cityRaw = Loader.getCity(cityName)
        if not self.cityRaw:
            raise Exception
        super(CityScreen, self).__init__(travel=self.travel, visit=self.visit, talk=self.talk)

    def printDisplay(self):
        travelLocs = '\n'.join(['    - {x}'.format(x=i) for i in self.cityRaw['travel']])
        visitLocs = '\n'.join(['    - {x}'.format(x=i) for i in self.cityRaw['visit']])
        npcs = '\n'.join(['    - {x}'.format(x=i) for i in self.cityRaw['npcs']])
        msg = (
"""
welcome to {city}
{desc}
what would you like to do?
  - travel
{travelLocs}
  - visit
{visitLocs}
  - talk
{npcs}
"""
).format(city=self.cityRaw['name'], desc=self.cityRaw['desc'], travelLocs=travelLocs, visitLocs=visitLocs, npcs=npcs)
        return msg

    def travel(self, location):
        pass

    def visit(self, location):
        pass

    def talk(self, person):
        pass
