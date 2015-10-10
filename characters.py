class Character(object):
    def __init__(self, name):
        self.name = name
        self.alive = True

    evil = False
    weight = 0
    night_active = False
    village = None

    def action(self, village):
        '''What happens at night...'''
        #nothing = input("You're not a werewolf. Just type in someone's name. ")

    def kill(self, target):
        target.alive = False
        target.village.newly_dead = target

    def die(self):
        self.alive = False
        self.village.newly_dead = self
        self.village.players.pop(self.name)

class Villager(Character):
    weight = 1
    evil = False

class Werewolf(Character):
    evil = True
    weight = -6
    night_active = True

    def action(self, village):
        '''Wake up and kill someone'''
        print(self.name)
        target = self.village.input_to_char('Who do you want to kill? ')
        #target = village.players[target]
        target.die()
        

class Seer(Villager):
    weight = 7
    night_active = True

    def action(self, village):
        '''choose one player to find out evil or not'''
        print(self.name)
        target = self.village.input_to_char('Who do you want to see? ')
        if isinstance(target, Werewolf):
            print('Wolf')
        else:
            print('Villager')

class Player(object):
    def __init__(self, name, character):
        self.name = name
        self.character = character

class Village(object):
    '''keeping track of all the players and such'''
    def __init__(self, players):
        self.players = players
        self.wolves = {}
        self.villagers = {}
        #self.dead = {}
        self.newly_dead = None

    def input_to_char(self, text, exception='No one'):
        while True:
            char = input(text)
            if char == exception:
                return None
            try:
                char = self.players[char]
                return char
            except KeyError:
                print('Not a valid player! Type: {0} or "No one"'.format(self.players.keys()))