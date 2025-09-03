# 1
# 2 3
# 2 3 4
# 2 3 4 5


rows = 4
for i in range(1, rows + 1):
    num = 1 if i == 1 else 2  
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
