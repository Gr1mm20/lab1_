def compare():
    n = int(input("Введите число эллементов списка: "))
    list1 = [0] * n
    for i in range(n):
        print("Введите целое число для ", i + 1, "элемента списка")
        list1[i] = int(input())
    x = int(input("Введите целое число х: "))


compare()