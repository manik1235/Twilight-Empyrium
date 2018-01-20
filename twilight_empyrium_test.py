""" twilight_empyrium.py test module
"""
# tabs for indentation for use with jota+ text editor on my phone            80
import unittest
import twilight_empyrium as te
from functools import namedtuple


class Test_twilight_empyrium(unittest.TestCase):
    """ Collection of tests for the twilight_empyrium game
    """

    def test_hex_tile_generator_known_answer(self):
        Ans = namedtuple('Ans', ['input', 'ans'])
        known_answers = [
            Ans('builtin1', [2, 1, 4, 3, 5]),
            Ans('ordered5', [1, 2, 3, 4, 5]),
            ]

        for ans in known_answers:
            test_te = list(te.hex_tile_generator(ans.input))
            self.assertListEqual(ans.ans, test_te)

    def test_hex_tile_generator_random(self):
        RandBuiltins = namedtuple('RandBuiltins', ['builtin', 'n', 'tile_stack'])

        known_answers = [
            RandBuiltins('random', 29, None),
            RandBuiltins('random', 10, None),
            RandBuiltins('random', 13, None),
            ]

        for ans in known_answers:
            test_te = list(te.hex_tile_generator(builtin=ans.builtin, n=ans.n, tile_stack=ans.tile_stack))      
            print('n={}, output={}'.format(ans.n, test_te))
            self.assertEqual(len(test_te), ans.n)