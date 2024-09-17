lst = ["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"]
n = int(input("Son kiriting: "))

result = []

for i in range(0, len(lst), n):
    result.append(lst[i:i+n])

print(result)
