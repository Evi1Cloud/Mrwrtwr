import random
n = -1
a = 0
b = 0
while n != 0:
    n = int(input("Выберите позицию: 1- камень, 2- Ножницы, 3- Бумага. : "))
    if n == 1:
        print("Игрок выбрал Камень")
    if n == 2:
        print("Игрок выбрал Ножницы")
    if n == 3:
        print("Игрок выбрал Бумага")
    comp = random.randint(1, 3)
    if comp == 1:
        print("компьютер выбрал Камень")
    if comp == 2:
        print("компьютер выбрал Ножницы")
    if comp == 3:
        print("компьютер выбрал Бумага")
    #Определяем победителя
    if n == comp:
        win = 0
    if n == 1 and comp == 2:
        win = 1
    if n == 1 and comp == 3:
        win = 2
    if n == 2 and comp == 1:
        win = 2
    if n == 2 and comp == 3:
        win = 1
    if n == 3 and comp == 1:
        win = 1
    if n == 3 and comp == 2:
        win = 2
    if win == 0:
        print("Ничья!")
        print("Счет: ", a, b)
    if win == 1:
        print("Игрок победил!")
        a += 1
        print("Счет: ", a, b)
    if win == 2:
        print("Компьютер победил!")
        b += 1
        print("Счет: ", a ,b)