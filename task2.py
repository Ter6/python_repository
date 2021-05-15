

def print_field2048(field2048):
    string = ""
    for y in range(len(field2048)):
        string += " _"
    print(string)
    string = ""
    for y in field2048:
        for u in y:
            string += f"{u}|"
        print(f"|{string}")
        string = ""
    for y in range(len(field2048)):
        string += " ¯"
    print(string)


def move_right_field2048(field2048):
    for y in field2048:
        for u in range(len(y)):
            for t in range(len(y)):
                if y[u] == 0:
                    y[u] = y[t]
                    y[t] = 0
                if y[u] == y[t] and t != u:
                    y[t] += y[u]
                    y[u] = 0
    return field2048


def move_left_field2048(field2048):
    for r in range(len(field2048[0])):
        for y in field2048:
            for u in range(len(y) - 1, -1, -1):
                for t in range(len(y) - 1, -1, -1):
                    print(y[u], y[t], field2048)
                    if y[u] == 0:
                        y[u] = y[t]
                        y[t] = 0
                    if y[u] == y[t] and t != u:
                        y[t] += y[u]
                        y[u] = 0
    return field2048


field = [[0, 0, 2, 2], [0, 0, 2, 2], [0, 0, 2, 4], [8, 8, 4, 2]]
print_field2048(move_left_field2048(field))
