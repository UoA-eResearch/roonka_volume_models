
data = [-1, 2, 0, 24, -5, 3]

sorted = sorted(data, reverse=True, key=lambda v: abs(v))

print(sorted[0])