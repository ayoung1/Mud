from sneakymud.mob import Mob
from sneakymud.loader import Loader

class MobFactory(object):

    DIR = 'mobs/'
    LAZY = {}

    def getMobByName(self, name):
        raw = self._rawLoad(name)
        return Mob(raw)

    def _rawLoad(self, name):
        data = self.__lazyLoad(name)
        if not data:
            data = Loader.loadFromName(MobFactory.DIR + name)
            MobFactory.LAZY[name] = data
        data['name'] = name
        return data

    def __lazyLoad(self, name):
        try:
            return MobFactory.LAZY[name]
        except:
            return None

    def __str__(self):
        output = ''
        for k in self.__dict__.keys():
            output += k
        return output
