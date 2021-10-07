''' Simple test on pierre/mainclass.py using basic class and functions
'''

from .context import pierre

x = pierre.mainclass.Var('7.01 01 mA')
print(x.central)
print(x.error)
print(x.unit)
