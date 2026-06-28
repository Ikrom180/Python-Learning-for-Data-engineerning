# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := place sign to leftmost position
# : = insert a place before positive numbers
# :, = comma separator

price1 = 31111.14159
price2 = -9822227.65
price3 = 133332.244

# print(f'Price 1 is {price1:.2f}')
# print(f'Price 2 is {price2:.2f}')
# print(f'Price 3 is {price3:.2f}')


# print(f'Price 1 is {price1:010}')
# print(f'Price 2 is {price2:010}')
# print(f'Price 3 is {price3:010}')

# print(f'Price 1 is {price1:>10}')
# print(f'Price 2 is {price2:>10}')
# print(f'Price 3 is {price3:^10}')

#Posiitve positive bob qoladi negative negative bolib
# print(f'Price 1 is {price1:+}')
# print(f'Price 2 is {price2:+}')
# print(f'Price 3 is {price3:+}')


# #commma make prettier and more readble
# print(f'Price 1 is {price1:,}')
# print(f'Price 2 is {price2:,}')
# print(f'Price 3 is {price3:,}')

print(f'Price 1 is {price1:,.2f}')
print(f'Price 2 is {price2:,.2f}')
print(f'Price 3 is {price3:,.2f}')