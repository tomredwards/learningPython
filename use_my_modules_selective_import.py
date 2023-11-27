# An example class on how to use modules I created (not pip installed)

import top_module
from mod1 import mod1_a  # Still have to reference via:
from mod2.mod2_b import *


print("Calling say_hi")
top_module.say_hi()
mod1_a.say_hi()
say_hi()


print("Calling other moethods")
top_module.top_hi("my_example")
mod1_a.a_announcement()
b_hi()
b_announcement()
