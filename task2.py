data = str(input("String: "))
answer = 0
for y in data:
    if y.isdigit():
        answer += int(y)
print(answer)