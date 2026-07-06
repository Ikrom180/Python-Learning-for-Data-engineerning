import random as r

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘


# "┌─────────┐"
# "│         │"
# "│    ●    │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}



dice = []
total = 0
number_of_dice = int(input("How many dice do you want? "))



for number in range(number_of_dice):
    dice.append(r.randint(1, 6))

for die in range(number_of_dice):
    for art in dice_art.get(dice[die]):
        print(art)
# if you want to make all of them in one place

# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()



for die in dice:
    total += die

print(f"total: {total}")
#
print(dice_art.get(1)[0])
print(dice_art.get(1)[1])
print(dice_art.get(1)[2])

