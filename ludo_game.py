import random

def play_game():
    # Step 1: Start everyone at position 0
    players = {"Player 1": 0, "Player 2": 0, "Player 3": 0}

    # Step 2: Keep rolling the dice until someone wins
    while True:
        for player in players:
            input(f"\n{player}'s turn. Press Enter to roll the dice...")
            roll = random.randint(1, 6)  # Roll the dice (1 to 6)
            print(f"{player} rolled a {roll}!")

            # Step 3: Move the player forward
            players[player] += roll

            # Step 4: Make sure they don’t go above 100
            if players[player] > 100:
                players[player] -= roll
                print(f"{player} needs exact number to reach 100.")
            elif players[player] == 100:
                print(f"\n🎉 {player} wins the game! Congratulations! 🎉")
                return  # End the game

            else:
                print(f"{player} is now at position {players[player]}.")

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing the Ludo Dice Game. Goodbye!")
            break

main()
