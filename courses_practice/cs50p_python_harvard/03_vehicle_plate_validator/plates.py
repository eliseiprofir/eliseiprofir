characters = "!@#$%^&*()_+=-[]}{;'\:\"|,./ <?>"
numbers = "1234567890"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Maximum 6 characters, minimum 2
    if len(s) not in range(2,7):
        return False

    # It should start with 2 letters
    if s[0] not in letters or s[1] not in letters:
        return False

    # It should not have other characters than letters and numbers
    for l in s:
        if l in characters:
            return False

    # Numbers must not be separated by letters:
    s_l = len(s)
    for i in range(s_l):
        if s[i] in numbers:
            try:
                int(s[i:])
            except:
                return False

    # If it has numbers
    num = ""
    for l in s:
        if l in numbers:
            num += l

    if len(num) > 0:

        # The last character must be a number
        if s[-1] not in numbers:
            return False

        # The first number must not be 0
        if num[0] == "0":
            return False

    # If none of the above triggered, the plate is valid
    return True


main()