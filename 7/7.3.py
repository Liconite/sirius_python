newspaper = set(range(1, 76))
magazine = set(range(77, 104))
both = set(range(21, 34))
print(len((newspaper | magazine) - both))
