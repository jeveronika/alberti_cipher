# creating two alphabets:
outer_alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
inner_alphabet = "y a q x s w c d e v f r b g t n h z m j k u i l o p"

def alberti_cipher(message, key):
    encrypted_message = ""
    for one_letter in message:
        index = outer_alphabet.index(one_letter)
        index2 = inner_alphabet.index(one_letter)
        if key == "encrypt":
            alphabet = outer_alphabet
            encrypted_message += inner_alphabet[index]
        elif key == "decode":
            alphabet = inner_alphabet
            encrypted_message += outer_alphabet[index2]

    print(f"\nYour operation is {key} and the result is: {encrypted_message}")

# loop
lets_continue = "yes"
while lets_continue == "yes":
    crypt = input("\nType 'encrypt', if you want to encrypt the message. Type 'decode', if you want to decode the message.\n").lower()
    text = input("\nType your message (no spaces or special characters):\n").lower()
    alberti_cipher(message=text, key=crypt)
    lets_continue = input("\Type 'yes' if you want to continue encryption. Type 'no' if you want to exit the encryption program.\n")