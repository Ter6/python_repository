def print_field2048(field2048):
    string = ""
    for line in range(len(field2048)):
        string += " _"
    print(string)
    string = ""
    for line in field2048:
        for u in line:
            string += f"{u}|"
        print(f"|{string}")
        string = ""
    for line in range(len(field2048)):
        string += " ¯"
    print(string)


def move_right_field2048(field2048):
    for line in field2048:
        for symbol in range(len(line) - 1):
            if line[symbol + 1] == 0:
                line[symbol] = line[symbol + 1]
                line[symbol + 1] = 0
            if line[symbol] == line[symbol + 1] and symbol + 1 != symbol:
                line[symbol + 1] += line[symbol]
                line[symbol] = 0
    return field2048


def move_left_field2048(field2048):
    for amount in range(len(field2048)):
        for line in field2048:
            for symbol in range(len(line) - 2, -2, -1):
                print(line[symbol], line[symbol + 1], line)
                if line[symbol + 1] == 0:
                    line[symbol + 1] = line[symbol]
                    line[symbol + 1] = 0
                if line[symbol] == line[symbol + 1] and symbol + 1 != symbol:
                    line[symbol + 1] += line[symbol]
                    line[symbol] = 0
    return field2048


field = [[2, 2, 4, 4], [0, 0, 0, 0], [6, 6, 12, 0], [8, 8, 8, 8]]
print_field2048(move_left_field2048(field))
