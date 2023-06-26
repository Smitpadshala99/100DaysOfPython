import random

def encode(message):
    encoded_message = ""
    words = message.split()

    for word in words:
        if len(word) >= 3:
            first_letter = word[0]
            encoded_word = word[1:] + first_letter + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        else:
            encoded_word = word[::-1]

        encoded_message += encoded_word + " "

    return encoded_message.strip()


def decode(message):
    decoded_message = ""
    words = message.split()

    for word in words:
        if len(word) < 3:
            decoded_word = word[::-1]
        else:
            random_chars = word[:3]
            decoded_word = word[3:-1] + word[-1]

        decoded_message += decoded_word + " "

    return decoded_message.strip()


def main():
    choice = input("Do you want to code (C) or decode (D) a message? ")

    if choice.upper() == "C":
        message = input("Enter the message to encode: ")
        encoded_message = encode(message)
        print("Encoded message:", encoded_message)
    elif choice.upper() == "D":
        message = input("Enter the message to decode: ")
        decoded_message = decode(message)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid choice! Please select 'C' or 'D'.")

if __name__ == "__main__":
    main()
