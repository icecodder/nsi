def char_utf8(base, nb):
    for i in range(base, base + nb):
        print(f"{i}\t{hex(i)}\t{chr(i)}")

char_utf8(8200, 200)
