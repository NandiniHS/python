def encrypt_message(plaintext, shift):
    encrypted_message = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(ciphertext, shift):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
            elif char.islower():
                decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message

if __name__ == "__main__":
    message = "Hello, World hey!" 
    shift_value = 3  
    
    encrypted = encrypt_message(message, shift_value)
    print(f"Encrypted Message: {encrypted}")
    
    decrypted = decrypt_message(encrypted, shift_value)
    print(f"Decrypted Message: {decrypted}")
