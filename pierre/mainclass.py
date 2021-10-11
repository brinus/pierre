''' Main module providing the class used for storing values with their errors
'''

# pylint: disable=missing-function-docstring

PREFIX = {
    'p' : 1e-12,
    'n' : 1e-09,
    'u' : 1e-06,
    'm' : 1e-03,
    '' : 1,
    'k' : 1e+03,
    'M' : 1e+06,
    'G' : 1e+09,
}

PREFIX_INVERSE = {
    1e-12: 'p',
    1e-09: 'n',
    1e-06: 'u',
    1e-03: 'm',
    1: '',
    1e+03: 'k',
    1e+06: 'M',
    1e+09: 'G',
}

class Var:
    ''' Main class
    '''

    def __init__(self, var=''):
        self._central, self._error, self._unit = var.split(' ')
        self._un = self._unit[0]
        self._it = self._unit[1:]

    def __str__(self):
        return f'{self} = {self._central} +/- {self._error} {self._unit}'

    @property
    def central(self):
        return self._central

    @property
    def error(self):
        return self._error

    @property
    def unit(self):
        return self._unit
