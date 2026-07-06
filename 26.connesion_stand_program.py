#Concession stand program

menu = {"pizza": 3,
        "nachos": 4.5,
        "popcorn": 6,
        "fries": 2.5,
        "chips": 1,
        "pretzel": 3.5,
        "soda": 3,
        "lemonade": 4.25
        }
# print(menu.get("pizza"))

cart = []
total = 0

print("------------MENU-------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------------")

while True:
    food = input("Enter the food you want q to quit: ").lower().replace(" ", "")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------Your order---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()

print(f"Your total cost is ${total:.2f}")


