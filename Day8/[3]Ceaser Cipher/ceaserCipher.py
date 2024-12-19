import ceaserCipherArt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(ceaserCipherArt.logo)


def ceaser(cipher_direction,start_text,shift):
    end_text = ""
    if cipher_direction == "decode":
            shift *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift

            end_text += alphabet[new_position]
        else:
            end_text += char


    
    print(f"The {cipher_direction}d text is: {end_text}")


should_continue = True
while should_continue:
    choice = input("Type 'Encode' to encrypt, 'Decode' to decrypt:\n").lower()
    message = input("Enter your message: \n").lower()
    shift_number = int( input("Enter the shift number: \n") )
    shift_number = shift_number % 26  #This wraps shift within 0-25 if they enter huge number say 100


    ceaser(choice,message,shift_number)
    result = input("Do you want to continue? Press Yes if yes press No if no.: \n").lower()
    if result == "no":
        should_continue = False

