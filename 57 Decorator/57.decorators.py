# Decorator = A function that extends the behavior of another function
#             without modifying the base function
#             PAss the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")


#sceleton stand always like that
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print('**You add sprinkles**')
        func(*args, **kwargs)
    return wrapper

def add_fudges(func):
    def wrapper(*args, **kwargs):
        print('**You add fudges**')
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudges
def get_ice_cream(flavor):
    print(f"Here is the {flavor} your ice cream")

get_ice_cream('flavor')