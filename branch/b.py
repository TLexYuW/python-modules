import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# import c # main.py -> error

# from teach import d
# from . import c


def print_Self():
    print("b -> true")


print(sys.path)

from same_level_package import d

d.print_Self()
