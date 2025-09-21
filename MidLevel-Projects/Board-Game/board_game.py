import random

# ANSI styles for feedback
class Styles:
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Game settings
BOARD_SIZE = 20
STARTING_COINS = 10

# Player setup
NUM_PLAYERS = int(input("Enter number of players (2-4): "))
players = []
for i in range(NUM_PLAYERS):
    name = input(f"Enter name for Player {i + 1}: ")
    players.append({"name": name, "position": 0, "coins": STARTING_COINS})


# Simulate a dice roll
def roll_dice():
    return random.randint(1, 6)

# Trigger a random event
def trigger_event(player):
    event = random.choice(["coin", "lose", "nothing"])
    if event == "coin":
        player["coins"] += 5
        print(f"{Styles.GREEN}{player['name']} found 5 coins!{Styles.RESET}")
    elif event == "lose":
        player["coins"] = max(0, player["coins"] - 3)
        print(f"{Styles.RED}{player['name']} lost 3 coins!{Styles.RESET}")
    else:
        print(f"{Styles.CYAN}{player['name']} found nothing.{Styles.RESET}")

# Display scoreboard
def display_scoreboard():
    print(f"\n{Styles.BOLD}Scoreboard:{Styles.RESET}")
    for player in players:
        print(f"{player['name']}: Position {player['position']} | Coins: {player['coins']}")

# Main game loop
def main():
    print(f"{Styles.BOLD}{Styles.CYAN}Welcome to the Board Game!{Styles.RESET}")
    winner = None

    while not winner:
        for player in players:
            input(f"\n{player['name']}, press Enter to roll the dice...")
            roll = roll_dice()
            print(f"{player['name']} rolled a {Styles.YELLOW}{roll}{Styles.RESET}!")
            player["position"] = min(player["position"] + roll, BOARD_SIZE)

            if player["position"] >= BOARD_SIZE:
                winner = player
                break

            print(f"{player['name']} moved to position {player['position']}.")
            trigger_event(player)
        
        display_scoreboard()

    print(f"\n{Styles.BOLD}{Styles.GREEN}Congratulations {winner['name']}! You win with {winner['coins']} coins!{Styles.RESET}")

    # Replay option
    replay = input("Do you want to play again? (y/n): ").strip().lower()
    if replay == 'y':
        for player in players:
            player["position"] = 0
            player["coins"] = STARTING_COINS
        main()
    else:
        print(f"{Styles.BOLD}Thanks for playing!{Styles.RESET}")

if __name__ == "__main__":
    main()