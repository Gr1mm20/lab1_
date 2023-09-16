def list_summ_without13__():
    n = int( input("Введите число эллементов списка: "))
    list1 = [0]*n
    for i in range (n):
        print("Введите целое число для ", i+1, "элемента списка")
        list1[i] = int(input())
    for i  in range (n):
        if list1[i] == 13:
            while i <= len(list1)-1:
                list1[i] = 0
                i=i+1
    print(list1)
    summ=sum(list1)
    print("Сумма всех элементов списка равна = ", summ)
list_summ_without13__()