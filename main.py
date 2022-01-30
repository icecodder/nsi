def aire(x: (int or float), y: (int or float)) -> (int or float):
    assert x >= 0 and y >= 0, "La longueur ou la largeur ne peut pas être negative"

    return x * y

print(aire(2, 3))
print(aire(2.5, 3.7))
#print(aire("deux", "trois"))
assert aire(2, 3) == 6
print("test ok")
#print(aire(-2, 3))
