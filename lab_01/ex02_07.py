print("input paragrahps ('done for end'): ")
lines = []
while True:
    line = input()
    if line == 'done':
        break
    lines.append(line)
print("paragrahps inputed: ")
for line in lines:
    print(line.upper())