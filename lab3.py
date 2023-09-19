#Написать функцию, которая принимает список, состоящий из n элементов,
# и целое число x и с помощью генераторной функции выводит на консоль только те элементы
# входящего списка, которые больше числа x.

def list_full(list_n):

    list1 = []
    for i in range(list_n):
        print("Введите целое число для ", i + 1, "элемента списка")
        list1[i] = list1.append(input())
    return list1

def compare_yield (list_n,x,list1):
    for i in range(list_n):
        if x > list1[i]:
            continue
        else:
            yield


x = int(input("Введите целое число х: "))
n = int(input("Введите число элементов списка: "))
list1=list_full(n)
compare_generator = compare_yield(n,x,list1)
print(compare_generator)
