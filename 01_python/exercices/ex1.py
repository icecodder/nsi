def v(h):
    if 0 <= h < 5:
        return 50 * h
    if 5 <= h <= 8:
        return 250 + 50 / 3 * (h - 5)
    else:
        print("impossible")

print(0, v(0))
print(5, v(5))
print(8, v(8))
