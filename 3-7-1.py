with open('sample.txt', 'r') as f:
    lines = f.readlines()
print(lines)

with open('sample.txt', 'r') as f:
    lines = list(f)
print(lines)

