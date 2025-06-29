import random as rd

print("🎮 Welcome to the Rock, Paper, Scissor Game! ✊📄✂️")

choices = ["rock", "paper", "scissor"]

user_score = computer_score = 0
print("🤖 Let's Play!\n")

while True:
    user_input = input("👉 Type Rock, Paper, Scissor or Q to Quit: ").lower()

    if user_input == "q":
        print(f"\n🏁 Final Score — You: {user_score} 🧍 | Computer: {computer_score} 🤖")
        print("🙏 Thanks for playing! See you next time!")
        break

    if user_input not in choices:
        print("⚠️ Invalid input. Please type Rock, Paper, or Scissors.")
        continue

    computer_choice = rd.choice(choices)
    print(f"🤖 Computer chose: {computer_choice.capitalize()}.")

    if user_input == computer_choice:
        print("🤝 It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissor") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissor" and computer_choice == "paper"):
        print("🎉 You Win this round!")
        user_score += 1
    else:
        print("😅 Computer Wins this round!")
        computer_score += 1

    print(f"📊 Current Score — You: {user_score} | Computer: {computer_score}\n")
