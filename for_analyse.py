import random

words = ("apple", "orange", "banana", "coconut", "pineapple")
answer = random.choice(words)

def display_hint(hint):
    print("Hint:", " ".join(hint))

hint = ["_"] * len(answer)
guessed = {}  # Track letter counts: {'p': 1} means 'p' guessed once
attempts = 6

print(f"Word has {len(answer)} letters")
display_hint(hint)

while attempts > 0 and "_" in hint:
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter!")
        continue

    # Count how many times this letter has been guessed
    guessed_count = guessed.get(guess, 0) # -> 0

    # Check if letter exists in word
    if guess in answer:
        # Count how many of this letter are in the word
        total_in_word = answer.count(guess)
        # print(total_in_word) -> harfnib turgan orinidigi indexini oladi


        # If already guessed all occurrences
        if guessed_count >= total_in_word:
            print(f"You've already found all '{guess}' letters in the word!")
            continue

        # Find the NEXT occurrence to fill (from left to right)
        found = False
        for i in range(len(answer)):
            if answer[i] == guess and hint[i] == "_":
                hint[i] = guess
                guessed[guess] = guessed_count + 1
                print(guessed)
                print(f"✅ Correct! Found one '{guess}'")
                found = True
                break  # Only fill ONE per guess

        if found:
            remaining = total_in_word - guessed[guess]
            if remaining > 0:
                print(f"   {remaining} more '{guess}' remaining in the word")
    else:
        attempts -= 1
        print(f"❌ Wrong! '{guess}' is not in the word. {attempts} attempts left")

    display_hint(hint)

if "_" not in hint:
    print(f"🎉 You win! The word was: {answer}")
else:
    print(f"💀 Game Over! The word was: {answer}")