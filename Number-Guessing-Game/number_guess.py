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

print(f"{Style.BOLD}{Style.CYAN}----- Welcome to the Number Guessing Game! -----{Style.RESET}")

# Difficulty Selection
print("Choose a difficulty level:")
print(f"{Style.GREEN}[1] Easy: (1-10, unlimited attempts){Style.RESET}")
print(f"{Style.YELLOW}[2] Medium: (1-50, 10 attempts){Style.RESET}")
print(f"{Style.RED}[3] Hard: (1-100, 7 attempts){Style.RESET}")

choice = input("Enter your choice: ")

# Set range based on difficulty
if choice == "1":
    number = random.randint(1, 10)
    attempts = None
elif choice == "2":
    number = random.randint(1, 50)
    attempts = 10
elif choice == "3":
    number = random.randint(1, 100)
    attempts = 7
else:
    print(f"{Style.RED}----- Invalid choice. Exiting Game. -----{Style.RESET}")
    exit()

attempts_count = 0

# Game Loop
while True:
    try:
        guess = int(input(f"{Style.BLUE}Enter your guess: {Style.RESET}"))
        attempts_count += 1

        if guess < number:
            print(f"{Style.YELLOW}Too Low! Try Again.{Style.RESET}")
        elif guess > number:
            print(f"{Style.MAGENTA}Too High! Try Again.{Style.RESET}")
        else:
            print(f"{Style.GREEN}{Style.BOLD} Congratulations! You guessed it in {attempts_count} tries.{Style.RESET}")
            break

        # For Limited attempts
        if attempts is not None and attempts_count >= attempts:
            print(f"{Style.RED}{Style.BOLD}Game Over! The number was {number}.{Style.RESET}")
            break

    except ValueError:
        print("Please enter a valid number.")
