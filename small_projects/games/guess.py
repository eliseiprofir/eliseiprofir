import random


def user_guess(highest: int) -> None:
    random_number: int = random.randint(1, highest)
    guess: int = 0
    tries: int = 0
    while guess != random_number:
        guess: int = int(input(f"Guess a number between 1 and {highest}: "))
        tries += 1
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f"\nYay, congrats. You have guessed the number {random_number} correctly in {tries} tries.\n")


def computer_guess(highest: int):
    low: int = 1
    high: int = highest
    feedback: str = ""
    tries: int = 0
    while feedback != 'C':
        if low != high:
            guess: int = random.randint(low, high)
        else:
            guess: int = low
        feedback: str = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').upper()
        tries += 1
        if feedback == 'H':
            high: int = guess - 1
        elif feedback == 'L':
            low: int = guess + 1
    print(f'\nYay! The computer guessed your number {guess} correctly in {tries} tries.')


def main() -> None:
    print("\nHello to my little GUESSing game.\n")
    while True:
        choice: str = input("Choose from below:\n[C] if you want the computer to guess your number\n[U] if you want to guess the computer's number.\nYour choice: ").upper()
        if choice == 'C':
            highest_number: int = int(input("\nEnter the number up to which you want the computer to guess (and set your number in mind): "))
            computer_guess(highest_number)
            break
        elif choice == 'U':
            highest_number: int = int(input("\nEnter the number up to which you want to guess the computer's number: "))
            user_guess(highest_number)
            break
    print("\nThank you for playing my GUESSing game! :)\n")


if __name__ == "__main__":
    main()
