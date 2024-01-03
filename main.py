import sys
import a
import os
import alpha5.beta5.mymodule5 as m5
import alpha4.beta4.mymodule4 as m4
from branch import b
# from .branch import b


m4.say_hello()
m5.say_hello()


a.print_Self()


b.print_Self()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'teach'))

print(BASE_DIR)
# from ... import xxx
# import xxx
print(sys.path)
