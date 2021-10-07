print("Стороны треугольника")
a = int(input("Сторона a = "))
b = int(input("Сторона b = "))
c = int(input("Сторона c = "))
if a + b > c:
    if a + c > b:
        if b + c > a:
            print("Треугольник")
        else:
            print("Не треугольник")