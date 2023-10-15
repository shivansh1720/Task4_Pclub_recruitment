def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            # Convert the character to uppercase for processing
            char = char.upper()
            # Calculate the shifted position
            shifted = ord(char) + shift
            # Wrap around if needed
            if shifted > ord('Z'):
                shifted -= 26
            # Convert back to lowercase if the original character was lowercase
            if not is_upper:
                shifted = chr(shifted).lower()
            else:
                shifted = chr(shifted)
            result += shifted
        else:
            # If it's not an alphabet character, keep it as it is
            result += char
    return result

# Example usage
text = "KJRZM ZHKGJT XCDGY KDNOJG"
shift = 5
encrypted_text = caesar_cipher(text, shift)
print("Original text:", text)
print("Encrypted text:", encrypted_text)
