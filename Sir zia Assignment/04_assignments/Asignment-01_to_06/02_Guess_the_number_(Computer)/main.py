import random as rd

print("🎉 Welcome to the Number Guessing Game!")
print("🧠 Think of a number between 1 and 10. The computer will try to guess it!")

low = 1
high = 10

if low <= high:
    while True:
        if low > high:
            print("❌ It seems your number is not within the valid range. Please try again!")
            break

        guess = rd.randint(low, high)
        print(f"🤖 Computer's guess is: {guess}")

        feedback = input("📢 Is the guess too High (H), too Low (L), or Correct (C)? ").strip().upper()

        if feedback == "C":
            print("🎯 Yay! The computer guessed your number correctly! 🥳")
            break
        elif feedback == "H":
            high = guess - 1
            print("🔽 Got it! The computer will guess a lower number...")
        elif feedback == "L":
            low = guess + 1
            print("🔼 Alright! The computer will guess a higher number...")
        else:
            print("⚠️ Invalid input. Please enter only H (high), L (low), or C (correct).")
else:
    print("⚠️ Invalid range! The lower bound is higher than the upper bound.")

