def draw_triangle(num):
    for i in range(1, num + 1):
        result = []
        for j in range(1, i + 1):
            result.append(j)
        print(*(str(n) for n in result))

    for i in range(num, 1, -1):
        result = []
        for j in range(1, i):
            result.append(j)
        print(*(str(n) for n in result))


