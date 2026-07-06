import random

low = 1
high = 100

opitons = ("rock", "paper", "scissors")
cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

# number = random.randint(low, high)
# number = random.random() # it will return 0 to 1 decimal numbers
# option = random.choice(opitons) # give a random option
random.shuffle(cards) # it have to contains array and it will shuffle array
print(cards)


