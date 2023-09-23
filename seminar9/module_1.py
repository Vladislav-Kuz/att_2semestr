def tri(h, a):
    return 0.5*h*a


def rect(a, b):
    return a*b


def circ(r):
    return 3.14 * r ** 2



# def main():
#     print("Начало модуля 1")
#     print("Начало вычисления площади сложной фигуры: ")
#     area = rect(20, 30) + tri(5, 10) - circ(5)
#     print(area)
#     print("конец модуля 1")


# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    print("Начало модуля 1")
    print("Начало вычисления площади сложной фигуры: ")
    area = rect(20, 30) + tri(5, 10) - circ(5)
    print(area)
    print("конец модуля 1")