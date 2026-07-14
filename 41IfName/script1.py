# print(dir())
# print(__name__) # -> return __main__
#
#
# if __name__ == "__main__":
#     main()


# from script2 import *
# print(__name__)




def favorite_food(food):
    print(f'Your favorite food is {food}')


def main():
    print("This is script1")
    favorite_food('pizza')
    print("GoodBye")

if __name__ == "__main__":
    main()





























