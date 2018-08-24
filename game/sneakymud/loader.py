import pkg_resources
import json
import os

DATA_PATH = pkg_resources.resource_filename('sneakymud', 'data_files/')

class Loader(object):
    __cache = None

    @staticmethod
    def getResourceList(resource):
        try:
            return Loader.__cache[resource].keys()
        except:
            return []

    @staticmethod
    def getCity(city):
        return Loader.getRaw('cities', city)

    @staticmethod
    def getMob(mob):
        return Loader.getRaw('mobs', mob)

    @staticmethod
    def getRace(race):
        return Loader.getRaw('races', race)

    @staticmethod
    def getRaw(r, e):
        try:
            return Loader.__cache[r][e]
        except:
            return None

    @staticmethod
    def buildCache():
        if Loader.__cache:
            return
        Loader.__cache = {}
        for resource in Loader.listResources(''):
            if resource != '__init__':
                Loader.__cache[resource] = {}
                for r in Loader.listResources(resource):
                    if r != '__init__':
                        r = r.replace('_', ' ')
                        Loader.__cache[resource][r] = Loader.loadFromName(resource+'/'+r)

    @staticmethod
    def listResources(dirName):
        l = os.listdir(DATA_PATH + dirName)
        l = [i.split('.')[0] for i in l]
        return l

    @staticmethod
    def loadFromName(name):
        data = None
        filename = DATA_PATH + name + '.json'
        with open(filename.replace(' ', '_')) as fin:
            data = json.load(fin)
        return data

Loader.buildCache()
