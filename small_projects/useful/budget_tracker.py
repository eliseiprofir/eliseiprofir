import json


def add_expenses(expenses: list[dict[str, str | int]], description: str, amount: float) -> None:
    expenses.append({"description": description, "amount": amount})
    print(f"Added expenses: {description}, Amount: {amount}")


def get_total_expenses(expenses: list[dict[str, str | int]]) -> int:
    total: int = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def get_balance(budget: float, expenses: list[dict[str, str | int]]) -> float:
    return budget - get_total_expenses(expenses)


def show_budget_details(budget: float, expenses: list[dict[str, str | int]]) -> None:
    print(f"Total Budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense["description"]}: {expense["amount"]}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")


def load_budget_data(filepath: str) -> tuple[int, list[dict[str, int]]]:
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  # Return default values if the file doesn't exist or is empty/corrupted


def save_budget_details(filepath: str, initial_budget: float, expenses: list[dict[str, str | int]]) -> None:
    data: dict[str, float] = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    print("Welcome to the Budget App")
    filepath: str = 'budget_data.json'  # Define the path to your JSON file
    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0.0:
        initial_budget: float = float(input("Please enter your initial budget: "))
        expenses: list = []
    else:
        total_expenses: int = get_total_expenses(expenses)
        balance = get_balance(initial_budget, expenses)
        print(f"- Your current budget is: {initial_budget}.")
        print(f"- Your expenses are {total_expenses}.")
        print(f"- Your balance is: {balance}.")
        choice = input(f"Do you want to update your budget (y/n)? ").lower()
        if choice == 'y':
            initial_budget = float(input("Please update your budget: "))
    budget: float = initial_budget

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Delete all expenses")
        print("3. Show budget details")
        print("4. Exit")
        choice: str = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            description: str = input("Enter expense description: ")
            amount: float = float(input("Enter expense amount: "))
            add_expenses(expenses, description, amount)
        elif choice == "2":
            expenses: list = []
        elif choice == "3":
            show_budget_details(budget, expenses)
        elif choice == "4":
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting Budget App. Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")


if __name__ == "__main__":
    main()
