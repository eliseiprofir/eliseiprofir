import requests
import hashlib
import sys


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check the API and try again.")
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main():
    print("\nHello to my program! Here you can check if your password was pwned and how many times.\n(I am using pwnedpasswords.com API.)\n")
    print("Enter how many passwords you want to check, and when you're finished, hit ENTER.")

    passwords = []

    while True:
        password = input("Enter password to check: ")
        if password == '':
            break
        passwords.append(password)

    print()

    for password in passwords:
        count = pwned_api_check(password)
        if count:
            print(f"- {password} was found {count} times... you should probably change your password.")
        else:
            print(f"- {password} was NOT found. Carry on!")

    return "\nThank you for using my program & take care of your passwords!!\n"


if __name__ == "__main__":
    sys.exit(main())
