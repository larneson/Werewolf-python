from characters import *
from random import shuffle


def make_village():
    #takes in player names and formats them into a list
    player_names = input("List names of players: ")
    player_names = player_names.split(',')
    player_names = [x.strip() for x in player_names]
    shuffle(player_names)

    #sets right numbers for types of characters, not needed atm
    num_players = len(player_names)
    num_wolves = 1                  #change this
    num_seers = 1
    num_villagers = num_players - num_wolves - num_seers

    #creates instances and adds them to a dictionary #oops that's what I made the player class for
    player_dict = {}

    def make_chars(char_class, num):
        for i in range(num):
            p = player_names.pop()
            player_dict[p] = char_class(p)

    make_chars(Werewolf, 1)
    make_chars(Seer, 1)
    make_chars(Villager, len(player_names))

    village = Village(player_dict)
    Character.village = village

    return village

def night(village):
    print("Night is falling and the wolves are on the prowl!")
    for name, char in village.players.copy().items():
        char.action(village)
    print('{0} died tonight!'.format(village.newly_dead.name))
    village.newly_dead = None

def day(village):
    target = village.input_to_char("The day rises. Who will the villagers choose to lynch? ")
    #make vote function for mayor
    if target:
        print('The village lynched {0}!'.format(target.name))
        target.die()
    else:
        print("The village lynched no one.")
    #village.players.pop(village.newly_dead.name)
    #village.newly_dead = None



def check_win_conditions(village):
    village.wolves = {}
    village.villagers = {}
    for name, char in village.players.items():
        if isinstance(char, Werewolf):
            village.wolves[name] = char
        else:
            village.villagers[name] = char
    if len(village.wolves) == 0:
        print('Villagers win!')
        raise VillagersWinException()
    elif len(village.villagers) <= len(village.wolves):
        print('Wolves win!')
        raise WolvesWinException()
    else:
        print('People left alive: {0}'.format(village.players.keys()))

class GameOverException(Exception):
    """Base game over Exception."""
    pass

class VillagersWinException(GameOverException):
    """Exception to signal that the villagers win."""
    pass

class WolvesWinException(GameOverException):
    """Exception to signal that the wolves win."""
    pass

def main():
    village = make_village()
    while True:
        night(village)
        check_win_conditions(village)
        day(village)
        check_win_conditions(village)

if __name__ == '__main__':
    main()
    
