import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"embed\/(\w+)\"", s):
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()