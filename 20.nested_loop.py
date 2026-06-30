#nasted loop = A loop within loop (outer, inner)
#              outer loop:
#                inner loop:

# if 5 in range(4):
#     print("Yes")
# else:
#     print("No")

# for x in range(1,11):
#     print(x, end=' ')


# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()


# with symbol


rows = int(input("Enter the # of number: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()