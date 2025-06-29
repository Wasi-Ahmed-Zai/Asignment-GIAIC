import random as rd

stages = [
    """
     _______
     |     
     |     
     |     
     |    
     |
    === 
    """,
    """
     _______
     |     |
     |     O
     |     
     |    
     |
    ===
    """,
    """
     _______
     |     |
     |     O
     |     |
     |    
     |
    ===
    """,
    """
     _______
     |     |
     |     O
     |    /|
     |    
     |
    ===
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    
     |
    ===
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / 
     |
    ===
    """,
    """
     _______
     |     |
     |     O
     |    /|\\
     |    / \\
     |
    === 
    """
]

words = ["apple", "banana", "mango", "orange", "grape", "pineapple", "watermelon", "strawberry", "kiwi", "papaya"]

chosen_word = rd.choice(words)
word_display = ["_" for _ in chosen_word]
guessed_letters = []
lives = len(stages) - 1

print("🎉 Welcome to Hangman!")
print("🧠 Guess the Fruit Word!")

while True:
    print("\n" + " ".join(word_display))
    guess = input("🔤 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a valid single letter.\n")
        continue
    if guess in guessed_letters:
        print("🔁 You already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(f"✅ Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"❌ Sorry, '{guess}' is not in the word.")
        print(stages[len(stages) - lives - 1])
        lives -= 1
        print(f"❤️ You have {lives} lives left.")

        if lives == 0:
            print(stages[lives])
            print(f"💥 You lose! The word was '{chosen_word}'.")
            break

    if "_" not in word_display:
        print("\n🎉 Congratulations! You guessed the word: " + "".join(word_display))
        break
