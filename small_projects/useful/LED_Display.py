def show(numbers: str, symbol: str) -> str:
    numbers_dict: dict[str, str] = {"0": "111 101 101 101 111",
                                    "1": "001 001 001 001 001",
                                    "2": "111 001 111 100 111",
                                    "3": "111 001 111 001 111",
                                    "4": "101 101 111 001 001",
                                    "5": "111 100 111 001 111",
                                    "6": "111 100 111 101 111",
                                    "7": "111 001 001 001 001",
                                    "8": "111 101 111 101 111",
                                    "9": "111 101 111 001 111"}
    leds: str = ""
    lines: int = len(numbers_dict["0"].split())
    spaces: int = 3
    symbol_len = len(symbol)
    for i in range(lines):
        line: str = ""
        for n in numbers:
            line += numbers_dict[n].split()[i] + " " * spaces
        leds += line + "\n"
    leds = leds.rstrip().replace("0", " "*symbol_len).replace("1", symbol)
    return leds


def main() -> None:
    while True:
        numbers: str = input("Enter the number you want to display: ")
        if numbers.isdigit():
            symbol: str = input("Enter the symbol you want to display the numbers with: ")
            break
        print("--- You did not enter a number. Try again!")
    print(show(numbers, symbol))


if __name__ == "__main__":
    main()
