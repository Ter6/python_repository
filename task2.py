data = int(input("Напишы любое число: "))
answer = 1
while (data / 2) % 2 == 0:
    answer += 1
    data = data / 2
print(answer)