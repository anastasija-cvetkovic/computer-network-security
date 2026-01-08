from text_utils import text_to_numbers, prepare_text_blocks, blocks_to_numbers, numbers_to_text
from math_utils import matrix_multiply
from key_validation import read_key_from_input, validate_key

def decrypt_text(ciphertext, key_matrix):
    inverse_matrix = validate_key(key_matrix)[1]

    numbers = text_to_numbers(ciphertext)
    blocks = prepare_text_blocks(numbers, 4)

    decrypted_blocks = []
    for block in blocks:
        decrypted_block = matrix_multiply(inverse_matrix, block, 27)
        decrypted_blocks.append(decrypted_block)

    decrypted_numbers = blocks_to_numbers(decrypted_blocks)
    plaintext = numbers_to_text(decrypted_numbers)

    return plaintext

def main():
    print("=" * 50)
    print("HILL SHIFRATOR - DESIFRIRANJE")
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

    print("Unesite tekst za desifriranje:")
    ciphertext = input("> ")

    if not ciphertext:
        print("GRESKA: Tekst ne moze biti prazan.")
        print()
        input("Pritisnite Enter za izlaz...")
        return

    plaintext = decrypt_text(ciphertext, key_matrix)

    print()
    print("=" * 50)
    print("REZULTAT:")
    print("=" * 50)
    print(f"Sifrovani tekst:  {ciphertext}")
    print(f"Desifrovani tekst: {plaintext}")
    print("=" * 50)
    print()
    input("Pritisnite Enter za izlaz...")

if __name__ == "__main__":
    main()
