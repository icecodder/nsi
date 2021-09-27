def f(x):
  if 0 <= x <= 5:
    return 50 * x
  elif 5 < x <= 8:
    return 50 / 3 * (x - 5) + 250
  else:
    return None

x = 0
p = 0.01
k = 260
c = 0

while f(x) < k:
    x += p
    c += 1

print(x, f(x), c)
