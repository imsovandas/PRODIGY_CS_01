def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'): 
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("\n------------------------- ")
    print("Implement Caesar Cipher By Sovan Das")
    print("------------------------- ")
    print("Choose Your Options \n1. Encrypt \n2. Decrypt \n")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = encrypt(message, shift)
        print("-------------------------")
        print("Your Encrypted message:", encrypted_message)
        print(" ")
        
    elif choice == 2:
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = decrypt(message, shift)
        print("-------------------------")
        print("Your Decrypted message:", decrypted_message)
        print(" ")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()