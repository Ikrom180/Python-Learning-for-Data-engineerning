# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#                   * unpacking operator
#                   1.positional 2.default 3. keyword 4. Arbitrary


# def add (a, b):
#     return a + b
#
# print(add(1, 2))


#But what if if we want to give more than 1 value
# Then we use: *args => args type tuple

# def add (*args):    # => name args does not matter
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
# print(add(1, 2,3,5,6,7))


# def display_name(*names):
#     for name in names:
#         print(name.capitalize() , end=' ')
#
# display_name('John', 'Doe', 'makhmud', 'izzat', 'ikrom')

# With **Kwargs

# .value() => shows value
# if we lopp  only yourself kwargs it will return keys

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_address(first="John", last="Doe")


# def print_address(**kwargs):
#     for key in kwargs:
#         print(f"{key}")
#
# print_address(first="John", last="Doe")

# =>Arges values should given first

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end = ' ')
#     print()
#     for value in kwargs.values():
#         print(value, end = ' ')
#
# shipping_label("ikrom",'Bakhtiyarov',
#                first="Shipping Label",
#                last="Shipping text", )


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = ' ')
    print()
    if 'apt' in kwargs:
        print(f'{kwargs.get('street')} {kwargs.get('apt')}')
    elif 'probox' in kwargs:
        print(f'{kwargs.get('street')}')
        print(f'{kwargs.get('probox')}')
    else:
        print(f'{kwargs.get('state')}')
    print(f'{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}')

shipping_label("Ikrom",'Bakhtiyarov',
               probox ="PO box #1001",
               street = "132 Fake Street",
               city ="Detroit",
               apt = '#100',
               zip = '54321')

