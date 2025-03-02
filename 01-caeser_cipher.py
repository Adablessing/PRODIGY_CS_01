def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift  
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char
    
    return result


while True:
    message = input("\nEnter your message: ")
    shift_value = int(input("Enter shift value: "))
    operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if operation not in ['encrypt', 'decrypt']:
        print("Invalid operation. Please type 'encrypt' or 'decrypt'.")
    else:
        output = caesar_cipher(message, shift_value, operation)
        print("Result:", output)
    
    again = input("\nDo you want to run again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Goodbye!")
        break
