# /n means starting a new line first
print("\nWORKED EXAMPLE 1")
capacity = 20 
# python sees 20 as an int
price = 12.5
# it has decimal, it's float
title = "Python Basics"
# anything inside quotes is a string (str)
is_open = True
cancelled_at = None
print(type(capacity).__name__)
# type(capacity) tells you the type- <class 'int'>
# .__name__ - takes only the name - int
print(type(price).__name__)
print(type(title).__name__)
print(is_open, cancelled_at)

# output 
# WORKED EXAMPLE 1
# int
# float
# str
# True None
# true is a boolean value
# none means there is currently no value


print("\nWORKED EXAMPLE 2")
capacity = 18
registered = 7
remaining = capacity - registered
print(remaining)
# 18 - 7 = (remaining)
print(18 / 4)
print(18 // 4)
# // remove the decimal part by rounding down
print(18 % 4)
# 4 x 4 = 16
# 18 - 16 = 2

# WORKED EXAMPLE 2
# 11
# 4.5
# 4
# 2

print("\nWORKED EXAMPLE 3")
total = 2 + 3 * 4
print(total)
total = (2 + 3) * 4
print(total)
registered = 4
registered += 1
print(registered)

# WORKED EXAMPLE 3
# 14
# 20
# 5