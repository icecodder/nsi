from math import sqrt

def f(a, b):
    print(f"{'a':<10}{'b':<10}{'b-a':<10}{'m':<10}{'m²':<15}{'Test m² > a'}")

    while b - a > 0.1:
        m = (a + b) / 2

        print(f"{a:<10}{b:<10}{b-a:<10}{m:<10}{m ** 2:<15}{m ** 2 > a!s}")

        if m ** 2 > sqrt(3):
            b = m
        else:
            a = m
    
    return(a, b)

print(f(1, 2)) # -> 1.375, 1.4375
