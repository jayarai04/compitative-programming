# *        *
# **      **
# ***    ***
# ****  ****
# **********


rows = 5
for i in range(1, rows + 1):
    # left stars
    print("*" * i, end="")
    # spaces
    print(" " * (2 * (rows - i)), end="")
    # right stars
    print("*" * i)
