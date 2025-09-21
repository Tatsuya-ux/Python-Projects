import random

# ANSI Stylesheet
class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    # Colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

# ASCII art for 6-sided die
die_faces = {
    1: ["+-------+", "|       |", "|   ●   |", "|       |", "+-------+"],
    2: ["+-------+", "| ●     |", "|       |", "|     ● |", "+-------+"],
    3: ["+-------+", "| ●     |", "|   ●   |", "|     ● |", "+-------+"],
    4: ["+-------+", "| ●   ● |", "|       |", "| ●   ● |", "+-------+"],
    5: ["+-------+", "| ●   ● |", "|   ●   |", "| ●   ● |", "+-------+"],
    6: ["+-------+", "| ●   ● |", "| ●   ● |", "| ●   ● |", "+-------+"]
}

def print_die_face(value):
    """Prints the ASCII art of the die face corresponding to the rolled value."""
    for line in die_faces[value]:
        print(Style.CYAN + line + Style.RESET)

def roll_die(sides):
    """Rolls a die with the specified number of sides and returns the result."""
    return random.randint(1, sides)

def roll_custom_dice(x, y):
    total = 0
    for i in range(x):
        result = roll_die(y)
        print(f"Die {i+1}: {Style.CYAN}{result}{Style.RESET}")
        if y == 6:
            print_die_face(result)
        total += result
    print(f"{Style.BOLD}Total: {total}{Style.RESET}")

def roll_until_target(target):
    count = 0
    while True:
        result = roll_die(6)
        count += 1
        print(f"Roll {count}: {Style.GREEN}{result}{Style.RESET}")
        if result == target:
            break
    print(f"{Style.BOLD}It took {count} rolls to get a {target}.{Style.RESET}")

def main():
    print(f"{Style.BOLD}{Style.MAGENTA}Welcome to the Dice Simulator!{Style.RESET}")

    while True:
        print(f"""\n{Style.BOLD}Menu:{Style.RESET}
              [1] Roll a single die (1-6)
              [2] Roll a custom die (XdY format)
              [3] Roll until condition met
              [4] Quit""")
        
        choice = input(f"{Style.BLUE}Enter your choice: {Style.RESET}")

        if choice == "1":
            result = roll_die(6)
            print(f"{Style.GREEN}You rolled a {result}.{Style.RESET}")
            print_die_face(result)
        
        elif choice == "2":
            try:
                x, y = map(int, input(f"{Style.BLUE}Enter dice in XdY format (e.g., 3d6): {Style.RESET}").lower().split('d'))
                if x < 1 or y < 2:
                    print(f"{Style.RED}Invalid input. X must be >= 1 and Y must be >= 2.{Style.RESET}")
                    continue
                roll_custom_dice(x, y)
            except ValueError:
                print(f"{Style.RED}Invalid format. Please enter valid integers.{Style.RESET}")

        elif choice == "3":
            try:
                target = int(input("Enter target number (1-6): "))
                if target < 1 or target > 6:
                    print(f"{Style.RED}Target must be between 1 and 6.{Style.RESET}")
                    continue
                roll_until_target(target)
            except ValueError:
                print(f"{Style.RED}Invalid input. Please enter a valid integers.{Style.RESET}")

        elif choice == "4":
            print(f"{Style.BOLD}{Style.MAGENTA}Thank you for using the Dice Simulator! Goodbye!{Style.RESET}")
            break
        else:
            print(f"{Style.RED}Invalid choice. Please select a valid option.{Style.RESET}")

if __name__ == "__main__":
    main()