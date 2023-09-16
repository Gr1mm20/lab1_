def count_matches():
    str1 = input('Введите первую строку ')
    str2 = input("Введите вторую строку ")
    count = 0
    for i in range(len(str1)-1):
        pair = str1[i:i+2]
        print(pair)
        if pair in str2:
            count += 1
    print("Количество совпадений:", count)
count_matches()