
#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#a = int (input("Input week day: "))

#if (a > 7):
    #print("nonexistance week day")
#elif (a < 6):
    #print ("This is not a weekend")
#else:
    #print("this is a weekend")

#2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# a = int (input("Введите число X: "))
# b = int (input("Введите число Y: "))
# if (a == 0 or b == 0):
#     print ("Введите число больше 0")
# if (a > 0 and b < 0):
#     print("Ось номер 4")
# if (a> 0 and b > 0):
#     print("Ось номер 1")
# if (a < 0 and b < 0):
#     print("Ось номер 3")
# if (a< 0 and b> 0):
#     print("Ось номер 2")

#1.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# a = int(input("Введите номер четверти: "))

# if(a == 1):
#     print ("x > 0 и y > 0")
# if(a == 2):
#     print ("x < 0 и y > 0")
# if(a == 3):
#     print ("x < 0 и y < 0")
# if(a == 4):
#     print ("x > 0 и y < 0")
# if(a > 4 or a < 1):
#     print("Такой оси не существует")

#2.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# from cmath import sqrt


# X1 = float(input("Введите координаты точки A на оси X: "))
# Y1 = float (input("Введите координты точки A на оси Y: "))
# X2 = float (input("Введите координты точки B на оси X: "))
# Y2 = float (input("Введите координты точки B на оси Y: "))
# print("Расстояние между двумя точками: ")
# print(sqrt(X1 - X2)**2 + (Y1 - Y2)**2)








