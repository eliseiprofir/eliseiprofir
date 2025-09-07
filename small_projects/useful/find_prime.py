def prime_from_range() -> str:
    # Finding prime numbers from a range
    maximum: int = int(input('\nEnter the maximum (positive) number up to which you want to find the prime numbers: '))
    prime: list = []
    if maximum < 0:
        result: str = 'You did not enter a positive number.'
    elif maximum == 0:
        result: str = 'Haha, nice try. There are no positive numbers up until 0.'
    elif maximum == 1:
        result: str = 'There are no prime numbers up until 1.'
    elif maximum == 2:
        result: str = 'All prime numbers up until 2 are: 1.'
    else:
        for n in range (2, maximum):
            for x in range (2, n):
                if n % x == 0:
                    break
            else:
                prime.append(n)
        prime_str: str = ', '.join(list(map(str, prime)))
        result: str = f'All prime numbers up until {maximum} are: {prime_str}.'
    return result


def prime_num() -> str:
    # Finding if a specific number is prime or not
    num: int = int(input('\nEnter the number you want to check if it\'s prime or not: '))
    if num < 0:
        result: str = 'You did not enter a positive number.'
    elif num == 1 or num == 2:
        result: str = 'The number IS prime.'
    elif num == 0:
        result: str = 'Haha, nice try. Zero is neither prime nor composite.'
    else:
        is_prime: str = ""
        for x in range(2, num):
            if num % x == 0:
                is_prime = 'IS NOT'
                break
            else:
                is_prime = 'IS'
        result: str = f'The number {is_prime} prime.'
    return result


print('––––––––––')
print('Hello to my program who finds prime numbers. 😊\n')

choose: str = input('Choose one option from below.\n'
                    '- Type \'r\' for finding all prime numbers from a range.\n'
                    '- Type \'n\' for checking if a specific number is prime or not.\n'
                    '- Type \'done\' when you want to close the program.\n'
                    'Your answer: ')

while choose != 'done':
    try:
        if choose == 'r':
            print(prime_from_range())
            print('––––––––––')
            choose = input('Range (\'r\'), number (\'n\') or close the program (\'done\'): ')
        elif choose == 'n':
            print(prime_num())
            print('––––––––––')
            choose = input('Range (\'r\'), number (\'n\') or close the program (\'done\'): ')
        else:
            print("You didn't choose an available option.")
            print('––––––––––')
            choose = input('Range (\'r\'), number (\'n\') or close the program (\'done\'): ')
    except ValueError:
        print('You did not enter a positive number.')

print('\nThank you for using my program! 😊')
print('––––––––––')
