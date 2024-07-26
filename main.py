from string import ascii_letters
from colorama import init, Fore

init(True)

letters = ascii_letters[:26].upper()


def caesar_encryption(plain_text: str, key: int = 3) -> str:
    encrypted_string = ""
    for plain_letter in plain_text.upper():
        if not plain_letter.isalpha():
            encrypted_string += plain_letter
            continue
        letter_index = letters.index(plain_letter) + key
        if letter_index >= len(letters):
            letter_index = letter_index - len(letters)
        encrypted_string += letters[letter_index]
    return encrypted_string


def caesar_decryption(cipher_text: str, key: int = 3) -> str:
    decrypted_string = ""
    for cipher_letter in cipher_text.upper():
        if not cipher_letter.isalpha():
            decrypted_string += cipher_letter
            continue
        letter_index = letters.index(cipher_letter) - key
        decrypted_string += letters[letter_index]
    return decrypted_string


if __name__ == "__main__":
    print(f"{Fore.LIGHTCYAN_EX}Do you want to (E)ncrypt or (D)ecrypt the Data?")
    query = input().lower()
    if query not in ["d", "e"]:
        print(
            f"{Fore.LIGHTRED_EX}Please Choose either E for Encryption or D for Decryption."
        )
        exit()

    while True:
        if query == "e":
            print(f"\n{Fore.LIGHTCYAN_EX}What is your Plain Text? (\E - To exit)")
        else:
            print(f"\n{Fore.LIGHTCYAN_EX}What is your Cipher Text? (\E - To exit)")

        data = input()
        if data == "\e":
            exit()

        result = caesar_encryption(data) if query == "e" else caesar_decryption(data)

        if query == "e":
            print(f"\n{Fore.GREEN}Your cipher text is\n{Fore.LIGHTGREEN_EX}{result}")
        else:
            print(f"\n{Fore.GREEN}Your plain text is\n{Fore.LIGHTGREEN_EX}{result}")
