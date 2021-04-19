data = str(input("String: "))
answer = ""
for y in data:
    if y.isdigit():
        answer += y
print(answer)