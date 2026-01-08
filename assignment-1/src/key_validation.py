from math_utils import gcd, determinant_4x4, matrix_inverse

def validate_key(key_matrix):
    det = determinant_4x4(key_matrix)
    det = det % 27

    if det == 0:
        return False, "Determinanta matrice je 0. Matrica nema inverznu matricu po modulu 27."

    if gcd(det, 27) != 1:
        return False, f"gcd(determinanta, 27) = gcd({det}, 27) = {gcd(det, 27)} != 1. Determinanta nema multiplikativnu inverzu po modulu 27, pa matrica nema inverznu matricu po modulu 27."

    inverse = matrix_inverse(key_matrix, 27)
    if inverse is None:
        return False, "Nije moguce izracunati inverznu matricu po modulu 27."

    return True, inverse

def read_key_from_input():
    print("Unesite matricu kljuca 4x4.")
    print("Svaki element mora biti broj izmedju 0 i 26.")
    print()

    key_matrix = []

    for i in range(4):
        while True:
            try:
                print(f"Red {i+1}: unesite 4 broja odvojena razmakom")
                line = input("> ")
                values = line.split()

                if len(values) != 4:
                    print("GRESKA: morate uneti tacno 4 broja.")
                    continue

                row = []
                valid = True
                for val in values:
                    num = int(val)
                    if num < 0 or num > 26:
                        print(f"GRESKA: broj {num} nije u opsegu 0-26.")
                        valid = False
                        break
                    row.append(num)

                if not valid:
                    continue

                key_matrix.append(row)
                break

            except ValueError:
                print("GRESKA: unesite samo cele brojeve.")

    print()
    print("Uneta matrica kljuca:")
    for row in key_matrix:
        print(row)
    print()

    return key_matrix
