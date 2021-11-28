def distance(t):
    if 0 <= t < 2:
        return 10 * t
    elif 2 <= t < 4:
        return 20 + 30 * (t -2)
    elif 4 <= t < 7:
        return 80 + 20 / 3 * (t - 4)
    elif 7 <= t < 8:
        return 100 + 20 * (t - 7)
    elif 8 <= t < 12:
        return 120 + 15 * (t - 8)
    else:
        return None

valeur = [0, 2, 4, 7, 8, 12]
for i in valeur:
    print(i, distance(i))
