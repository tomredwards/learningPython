# An example class on how to use modules I created (not pip installed)

import top_module
import mod1.mod1_a
import mod2.mod2_b


print("Calling say_hi")
top_module.say_hi()
mod1.mod1_a.say_hi()
mod2.mod2_b.say_hi()


print("Calling other moethods")
top_module.top_hi("my_example")
mod1.mod1_a.a_announcement()
