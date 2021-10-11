''' context file to provide import from pierre/pierre module
'''

#pylint: disable=wrong-import-position, unused-import

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pierre import mainclass
