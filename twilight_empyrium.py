""" Twilight Emperium 
map generator
game

Start with a map generator
Find a hex grid template
Then maybe a generator for the tiles? 
Or a straight up iterator, that'd be fun to practice. 
"""

import functools
# from random import SystemRandom # can't get this to work yet
import random

def hex_tile_generator(builtin='ordered5', n=1, tile_stack=None):
    """ generates n tiles from list tilestack

    hex_tile_generator(builtin='builtin1')
    hex_tile_generator(builtin='builtin1')
    hex_tile_generator(builtin='builtin1')



    """
    rand = random.SystemRandom()
    built_ins = {'builtin1': [2, 1, 4, 3, 5],
                 'ordered5': [1, 2, 3, 4, 5],
                 'random': rand.sample(range(1, n + 1), n),
                 'ordered29': list(range(1,30)),
                 }

    if tile_stack == None:
        # set the default tile_stack
        tile_stack = built_ins['ordered5']

    if built_ins is not None:
        try:
            output_list = built_ins[builtin]
        except KeyError:
            print('builtin not found. Defaulting to builtin "ordered5"')
            output_list = built_ins['ordered5']
    
    for output in output_list:
        yield output
    
    

if __name__ == '__main__':
    """ get a generator
    """
    print('Available Built-ins:\nbuiltin1\nordered5\nrandom\nordered29\n')
    r_builtin = input("Hello! Which built-in would you like to use? ")
    if r_builtin == 'random':
        r_n = input("how many random tiles would you like to generate? ")
        r_n = int(r_n)
        te_gen = hex_tile_generator(builtin=r_builtin, n=r_n)
    else:
        te_gen = hex_tile_generator(builtin=r_builtin)

    print(list(te_gen))
