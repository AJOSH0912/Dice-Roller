import random

def roll_dice(num_dice):
    """Rolls the specified number of dice and returns the results."""
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def main():
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (1-3): "))
            if num_dice < 1 or num_dice > 3:
                print("Please enter a number between 1 and 3.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

    results = roll_dice(num_dice)
    print(f"Rolling {num_dice} dice: {results}")

if __name__ == "__main__":
    main()
