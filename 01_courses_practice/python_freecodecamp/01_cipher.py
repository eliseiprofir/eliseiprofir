def vigenere(message: str, key: str, direction: int = 1) -> str:
    key_index: int = 0
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    final_message: str = ''

    message: str = message.lower()
    key: str = key.lower()

    for char in message:

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char: str = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted/decrypted letter
            offset: int = alphabet.index(key_char)
            index: int = alphabet.find(char)
            new_index: int = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message: str, key: str) -> str:
    return vigenere(message, key)


def decrypt(message: str, key: str) -> str:
    return vigenere(message, key, -1)


def main() -> None:
    encrypt_id: str = 'e'
    decrypt_id: str = 'd'

    print(
        "\nHello to my encryption/decryption program. You will need a text and a key (both on lower characters) to do this.\n")
    print("But first of all, do you want to:")
    print(f"- [{encrypt_id}] ENCRYPT, or")
    print(f"- [{decrypt_id}] DECRYPT a text?")

    choice: str = ''
    while choice not in [encrypt_id, decrypt_id]:
        print()
        choice = input(f"Your choice [{encrypt_id} or {decrypt_id}]: ").lower().strip()

    if choice == encrypt_id:
        print()
        text: str = input("Please enter your text to encrypt: ")
        custom_key: str = input("Please enter your encryption key:  ")
        encryption: str = encrypt(text, custom_key)
        print(f'\nEncrypted text: {encryption}\n')

    if choice == decrypt_id:
        print()
        text: str = input("Please enter your text to decrypt: ")
        custom_key: str = input("Please enter your decryption key:  ")
        decryption: str = decrypt(text, custom_key)
        print(f'\nDecrypted text: {decryption}\n')


if __name__ == "__main__":
    main()
