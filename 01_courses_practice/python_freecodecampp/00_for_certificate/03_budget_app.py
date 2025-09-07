class Category:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ledger: list[dict[str: int, str: str]] = []

    def deposit(self, amount: int | float, description: str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: int | float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> int:
        balance: int = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance

    def check_funds(self, amount: int) -> bool:
        return amount <= self.get_balance()

    def transfer(self, amount: int, category: 'Category') -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self) -> str:
        # SECOND BETTER METHOD
        title: str = f"{self.name:*^30}\n"
        items: str = ""
        for item in self.ledger:
            desc: str = item['description'][:23]
            amt: str = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total: str = f"Total: {self.get_balance():.2f}"
        return title + items + total + '\n'

        # FIRST METHOD
        # LEN = 30

        # # First line
        # category_len = len(self.name)
        # half_stars_len = int((LEN - category_len) / 2)
        # output = "*" * half_stars_len + self.name + "*" * half_stars_len + '\n'

        # # Entries
        # for entry in self.ledger:
        #     output += entry["description"][:23] + " "
        #     desc_len = len(entry["description"])
        #     amount = f"{entry['amount']:.2f}"
        #     amount_len = len(amount)
        #     output += " " * (LEN - amount_len - desc_len - 1) + amount
        #     output += "\n"

        # # Total
        # output += f"Total: {self.get_balance():.2f}"

        # return output


def create_spend_chart(categories: list[Category]) -> str:
    title: str = "Percentage spent by category\n"

    total_spent: int = 0
    category_spent: list[int] = []
    for category in categories:
        spent = sum([-item["amount"] for item in category.ledger if item["amount"] < 0])
        category_spent.append(spent)
        total_spent += spent

    percentages: list[float] = [((spend / total_spent) * 100) // 10 * 10 for spend in category_spent]

    chart: str = ""
    for i in range(100, -1, -10):
        line: str = f"{i:>3}|"
        for p in percentages:
            if p >= i:
                line += ' o '
            else:
                line += '   '
        chart += line + ' \n'
    chart += '    -' + '---' * len(categories) + '\n'

    max_len: int = max(len(category.name) for category in categories)
    names: list[str] = [category.name.ljust(max_len) for category in categories]
    for i in range(max_len):
        line: str = "     "
        for name in names:
            line += name[i] + "  "
        chart += line + '\n'

    return title + chart.rstrip('\n')


food: Category = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(20, "Shoes")

car = Category("Car")
car.deposit(2000, "deposit")
car.withdraw(40, "lights")

print(food)
print(clothing)
print(car)
print(create_spend_chart([food, clothing, car]))
