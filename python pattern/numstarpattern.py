# 1
# 1 *
# 1 * 3
# 1 * 3 *
# 1 * 3 * 5

rows = 5
for i in range(1, rows + 1):
    num = 1
    for j in range(1, i + 1):
        if j % 2 != 0:   # Odd position → number
            print(num, end=" ")
            num += 2
        else:            # Even position → star
            print("*", end=" ")
    print()
