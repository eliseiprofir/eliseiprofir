import sys
import csv


def main():
    check_arg()
    reading_writing()


def check_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

def reading_writing():
    output = []
    try:
        with open(sys.argv[1], "r") as before:
            reader = csv.DictReader(before)
            for row in reader:
                split_name = row["name"].split(',')
                output.append({'first': split_name[1].lstrip(), 'last': split_name[0], 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    try:
        with open(sys.argv[2], "w") as after:
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            for row in output:
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[2]}")

if __name__ == "__main__":
    main()