import re


def main():
    credit_card = input("Number: ")
    sum_digits = every_other_digit(int(credit_card))
    amex = isValidAmex(credit_card)
    master_card = isValidMasterCard(credit_card)
    visa = isValidVisa(credit_card)
    if sum_digits % 10 != 0:
        print("INVALID")
    elif amex == True:
        print("AMEX")
    elif master_card == True:
        print("MASTERCARD")
    elif visa == True:
        print("VISA")
    else:
        print("INVALID")


def every_other_digit(credit_card):
    sum = 0
    isAlternateDigit = False
    while credit_card > 0:
        if isAlternateDigit == True:
            last_digit = credit_card % 10
            product = multiplyAndSum(last_digit)
            sum += product
        else:
            last_digit = credit_card % 10
            sum += last_digit
        isAlternateDigit = not isAlternateDigit
        credit_card = credit_card // 10
    return sum


def multiplyAndSum(last_digit):
    multiply = last_digit * 2
    sum = 0
    while multiply > 0:
        last_digit_multiply = multiply % 10
        sum += last_digit_multiply
        multiply = multiply // 10
    return sum


def isValidAmex(credit_card):
    if re.match(r"^((34|37)[0-9]{13})$", credit_card):
        return True
    return False


def isValidMasterCard(credit_card):
    if re.match(r"^(([5][0-5])[0-9]{14})$", credit_card):
        return True
    return False


def isValidVisa(credit_card):
    if re.match(r"^4(([0-9]{15})|([0-9]{12}))$", credit_card):
        return True
    return False


if __name__ == "__main__":
    main()
