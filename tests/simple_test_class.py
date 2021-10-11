''' Simple test on pierre/mainclass.py using basic class and functions
'''

import unittest

from .context import mainclass

class TestVar(unittest.TestCase):
    ''' Testing class
    '''

    def _test_print(self):
        self.assertEqual(str(mainclass.Var('7.0 01 mA')), '7.0 0.1 mA')

if __name__ == '__main__':
    unittest.main(exit=False)
