# Keyword arguments = an argument preceded by an identifier
#                     helps with readibility
#                     order of arguments does not matter
#                     1.positio nal 2.default 3.Keyword 4.arbitary


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title = 'Mr.', last = "John",first = 'Doe') #positional arguments stand first

def get_phone(country, area, first, last):
    print(f"{country}-{area}-{first}-{last}")

phone_num = get_phone(country=1, area = 123, first=456, last=7890)
print(phone_num)