def f(x):
  if 0 <= x <= 5:
    return 50 * x
  elif 5 < x <= 8:
    return 50 / 3 * (x - 5) + 250
  else:
    return None

a = 0
b = 8
p = 0.01
k = 260
c = 0

print(f"{'a':<10}{'b':<10}{'b-a':<10}{'m':<10}{'m²':<20}{'Test m² > a'}")

while b - a > 0.001:
    m = (a + b) / 2

    print(f"{a:<10}{b:<10}{b-a:<10}{m:<10}{m ** 2:<20}{m ** 2 > a!s}")

    if f(m) > k:
        b = m
    else:
        a = m
    
    c += 1

print(a, b, p, k, c) # 13 passages (ex6) donc + rapide que 561 passages (ex4)
