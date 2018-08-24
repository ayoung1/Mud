

class Screen(object):
    def __init__(self, **options):
        self.options = options
        self.options['exit'] = self.exit

    def printDisplay(self):
        raise NotImplementedError

    def onPlayerInput(self, playerinput):
        tokens = playerinput.split(' ')
        if tokens[0] in self.options.keys():
            return self.options[tokens[0]](tokens[1:])

    def attach(self, ge):
        self.gameEngine = ge

    def exit(self, tokens):
        return 'EXIT'
