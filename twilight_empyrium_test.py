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
        known_answers_hex_tile_generator = [
            Ans('builtin1', [2, 1, 4, 3, 5]),
            Ans('ordered5', [1, 2, 3, 4, 5]),
            ]

        for ans in known_answers_hex_tile_generator:
            test_te = list(te.hex_tile_generator(ans.input))
            self.assertListEqual(ans.ans, test_te)

    def test_hex_tile_generator_random(self):