def char_utf8(base, nb):
    for i in range(base, base + nb):
        char_decimal = i
        char_hex = hex(char_decimal)
        char = chr(char_decimal)
        print(f"{char_decimal}\t{char_hex}\t{char}")

char_utf8(8200, 200)

