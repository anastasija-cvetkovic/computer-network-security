from text_utils import text_to_numbers, prepare_text_blocks, blocks_to_numbers, numbers_to_text
from math_utils import matrix_multiply
from key_validation import read_key_from_input, validate_key

def encrypt_text(plaintext, key_matrix):
    numbers = text_to_numbers(plaintext)
    blocks = prepare_text_blocks(numbers, 4)

    encrypted_blocks = []
    for block in blocks:
        encrypted_block = matrix_multiply(key_matrix, block, 27)
        encrypted_blocks.append(encrypted_block)

    encrypted_numbers = blocks_to_numbers(encrypted_blocks)
    ciphertext = numbers_to_text(encrypted_numbers)

    return ciphertext

def main():
    print("=" * 50)
    print("HILL SHIFRATOR - SIFRIRANJE")
    print("=" * 50)
    print()

    key_matrix = read_key_from_input()

    is_valid, result = validate_key(key_matrix)

    if not is_valid:
        print("GRESKA: Kljuc nije validan!")
        print(result)
        print()
        input("Pritisnite Enter za izlaz...")
        return

    print("Kljuc je validan!")
    print()

    print("Unesite tekst za sifriranje:")
    plaintext = input("> ")

    if not plaintext:
        print("GRESKA: Tekst ne moze biti prazan.")
        print()
        input("Pritisnite Enter za izlaz...")
        return

    ciphertext = encrypt_text(plaintext, key_matrix)

    print()
    print("=" * 50)
    print("REZULTAT:")
    print("=" * 50)
    print(f"Originalni tekst: {plaintext}")
    print(f"Sifrovani tekst:  {ciphertext}")
    print("=" * 50)
    print()
    input("Pritisnite Enter za izlaz...")

if __name__ == "__main__":
    main()
