# Shopping card program

foods = []
prices = []
total = 0


while True:
    food = input("Enter the whatever food you want foods q to quit: ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the food: "))
        total = total + price
        prices.append(price)
        foods.append(food)

for food in foods:
    print(f'{food}', end=" ")

print()
print(f'You ordered {len(foods)} thing,and total {total} $')
print("Goodbye!")