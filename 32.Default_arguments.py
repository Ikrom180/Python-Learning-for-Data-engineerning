import time
#default args = A default value for certain parameters
#               default is used when that argument is ommited
#               make your functions more flexiable, reduces # of arguments
#               1. positional, 2.Default, 3. Keyword, 4. Arbitrary
#



# def net_price(list_price, dicount = 0, tax = 0.5):
#     return list_price * (1 - dicount) * (1 + tax)
#
# print(net_price(500))
# print(net_price(1000, 0.1))
# print(net_price(1000, 0.1, 0 ))


def count(end, start=1):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(30, 15)