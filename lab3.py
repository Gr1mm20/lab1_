#Написать функцию, которая принимает список, состоящий из n элементов,
# и целое число x и с помощью генераторной функции выводит на консоль только те элементы
# входящего списка, которые больше числа x.
def list_full(list_n):
    list1 = []
    for i in range(list_n):
        print("Введите целое число для ", i + 1, "элемента списка")
        num = int(input())
        list1.append(num)
    return list1
def compare_yield (list1,x):
    generator = (element for element in list1 if element > x)
    for element in generator:
        print(element)

n = int(input("Введите число элементов списка: "))
list1 = list_full(n)
x = int(input("Введите целое число х: "))
compare_yield(list1,x)
