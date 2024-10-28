def custom_hash(plain_text: str) -> str:
    # Initialize a base hash value with a non-zero constant for entropy
    hash_value = 0x12345678
    prime = 31  # A prime multiplier to increase variability
    
    # Loop through each character in the plaintext
    for i, char in enumerate(plain_text):
        # Convert the character to ASCII and apply position-based transformation
        char_value = ord(char) * (i + 1) ** 3

        # Multiply by a prime to spread out values and reduce collisions
        char_value = char_value * prime

        # Mix the current character value into the hash with XOR and addition
        hash_value = (hash_value ^ char_value) + (hash_value << 3) & 0xFFFFFFFF
        
        # Add a bitwise rotation for extra scrambling
        hash_value = ((hash_value << 7) | (hash_value >> 25)) & 0xFFFFFFFF
        
        # Subtract the character's position multiplied by the prime, keeping variability high
        hash_value = (hash_value - (i * prime)) & 0xFFFFFFFF

    # XOR with a constant and rotate bits to further spread values
    final_constant = 0xABCDEF
    hash_value ^= final_constant
    hash_value = ((hash_value << 13) | (hash_value >> 19)) & 0xFFFFFFFF

    # Convert the integer hash value to a hexadecimal string
    hashed_text = hex(hash_value)[2:]
    
    # Ensure the hash is 8 characters long for consistent output length
    return hashed_text.zfill(8)

# List of names to hash
names = ["Edward Mills", "Gary Neville", "Jamie Carragher", "Roy Keane", "Vinicius Junior", "Cristiano Ronaldo"]

# Hash each name and print the result
for name in names:
    hashed_text = custom_hash(name)
    print(f"Plain Text: {name}")
    print(f"Enhanced Custom Hashed Text: {hashed_text}")
