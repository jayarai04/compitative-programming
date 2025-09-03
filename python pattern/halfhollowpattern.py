# **********
# **** ****
# *** ***
# ** **
# * *


rows = 5
for i in range(rows):
    print("*" * (rows - i), end="")
    print(" " * (2 * i), end="")
    print("*" * (rows - i))
