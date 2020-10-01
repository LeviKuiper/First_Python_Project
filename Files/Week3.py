import turtle
import math

# First ten

# 1-2
# day = int(input("What day is it today? "))
# stay = int(input("How long is your stay? "))
#
# day = ((day+stay) % 7)
#
# dayArray = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print(dayArray[day])
#
# # 6
# numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
# for number in numbers:
#     if number >= 75:
#         print(number, "First")
#     elif 70 <= number < 75:
#         print(number, "Upper Second")
#     elif 60 <= number < 70:
#         print(number, "Second")
#     elif 50 <= number < 60:
#         print(number, "Third")
#     elif 45 <= number < 50:
#         print(number, "F1 Supp")
#     elif 40 <= number < 45:
#         print(number, "F2")
#     elif number < 40:
#         print(number, "F3")
#
# # 7
# a = int(input("length of side 1: "))
# b = int(input("length of side 2: "))
#
# c = ((a**2) + (b**2))**0.5
# print(c)

# # 8
# threshold = 1e-7
#
# a = int(input("length short side 1"))
# b = int(input("length short side 2"))
# c = int(input("length long side"))
#
# if (c-(a**2 + b**2)**0.5) < threshold:
#     print("The triangle is right-angled")

# 9
# threshold = 1e-7
#
# a = int(input("length side 1: "))
# b = int(input("length side 2: "))
# c = int(input("length side 3: "))
#
#
# if c >= a and c >= b and (c-(a**2 + b**2)**0.5) < threshold:
#     print("The triangle is right-angled")
#
# if b >= a and b >= c and (b-(a**2 + c**2)**0.5) < threshold:
#     print("The triangle is right-angled")
#
# if a >= b and a >= c and (a-(c**2 + b**2)**0.5) < threshold:
#     print("The triangle is right-angled")

# 10

# a = math.sqrt(2.0)
# print(a, a*a)
# print(a*a == 2)


# # Second ten
#
# # 1
# for i in range(1000):
#     print("We like Python's turtles!")
#
# # 2
# for month in ["January", "February", "March"]:
#     print("One of the months of the year is:", month)
#
# # 3
# window = turtle.Screen()
# window.bgcolor("light gray")
#
# tess = turtle.Turtle()
# tess.speed(0)
#
# tess.left(3645)
#
# window.mainloop()

# 4
# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# total = 0
# product = 1
#
# for number in numbers:
#     print(number)
#     print(number, number**2)
#     total += number
#     product *= number
# print(total)
# print(product)

# # 5
# screen = turtle.Screen()
# screen.bgcolor("light gray")
#
# tony = turtle.Turtle()
# tony.color("blue")
# leo = turtle.Turtle()
# leo.color("red")
# rafael = turtle.Turtle()
# rafael.color("orange")
# tania = turtle.Turtle()
# tania.color("green")
#
# for i in range(3):
#     tony.forward(120)
#     tony.left(120)
#
# for i in range(4):
#     leo.forward(90)
#     leo.left(90)
#
# for i in range(5):
#     rafael.forward(72)
#     rafael.left(72)
#
# for i in range(6):
#     tania.forward(60)
#     tania.left(60)
# screen.mainloop()
#
# # alt
#
# angles = int(input("How many corners do you want to draw: "))
#
# window = turtle.Screen()
# window.bgcolor("light gray")
#
# coroner = turtle.Turtle()
# coroner.color("green")
#
# for i in range(angles):
#     coroner.forward(360/angles)
#     coroner.left(360/angles)
#
# window.mainloop()
#
# # 6, 7
#
# screen = turtle.Screen()
# screen.bgcolor("light gray")
#
# drunk = turtle.Turtle()
#
# turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# heading = 0
#
# for turn in turns:
#     drunk.forward(100)
#     drunk.left(turn)
#     heading += turn
#
# print(720+heading)
#
# screen.mainloop()
#
# # 8
#
# corner = int(input("How many corners in a polygon: "))
# angle = 360/corner
# print(angle)
#
# # 10
#
# side = int(input("How big will the star be: "))
# corners = int(input("How many corners on the triangle: "))
#
# screen = turtle.Screen()
# screen.bgcolor("light gray")
#
# star = turtle.Turtle()
#
# for i in range(corners):
#     star.forward(side)
#     star.right(720/corners)
#
# screen.mainloop()
#
# # 11
#
# screen = turtle.Screen()
# screen.bgcolor("light gray")
# clock1 = turtle.Turtle()
# clock2 = turtle.Turtle()
#
# clock1.penup()
# clock1.shape("turtle")
# clock2.penup()
#
# clock1.left(90)
# clock1.forward(200)
#
# for i in range(12):
#     clock1.stamp()
#     clock1.left(90)
#     clock1.left(360/24)
#     clock1.forward(100)
#     clock1.left(360/24)
#     clock1.right(90)
#
# clock2.forward(120)
#
# for i in range(12):
#     clock2.pendown()
#     clock2.forward(30)
#     clock2.forward(-30)
#     clock2.penup()
#     clock2.left(90)
#     clock2.left(360 / 24)
#     clock2.forward(62)
#     clock2.left(360 / 24)
#     clock2.right(90)
#
# screen.mainloop()
#
# # Third set of 10
#
# numbers = [1 , 3, 5, 65, -9, 7, 973, 823, -2, 2, 54, 64, -7, 7, 8, 2, 35, 23]
# words = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "fiven", "fiver"]
#
# # 1 2
# odd = 0
# even = 0
#
# for number in numbers:
#     odd += number % 2 == 1
#     if number % 2 == 0:
#         odd += 1
#
# print(odd)
# print(even)
#
# # 3
# neg = 0
#
# for number in numbers:
#     if number < 0:
#         neg += number
#
# # 4
# sum = 0
#
# for word in words:
#     if len(word) == 5:
#         sum += 1
#
# print(sum)
#
# # 5
# count = 0
# for number in numbers:
#     if number % 2 == 0:
#         break
#     count += 1
# print(count)
#
# # 6
# count = 0
# for word in words:
#     if word == "Sam":
#         count += 1
#         break
#     count += 1
# print(count)
#
# # 7
# n = 25
# threshold = 0.001
# approximation = n/2 # Start with some or other guess at the answer
# while True:
#     better = (approximation + n/approximation)/2
#     if abs(approximation - better) < threshold:
#         print(better)
#         break
#     print(better)
#     approximation = better
#
# # 8
#
# triangular = 0
# n = 0
# for i in range(100):
#     triangular += n
#     n += 1
#     print(i, triangular)
#
# # 9
#
# n = 100
# for i in range(n+1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#
# # 10
#
# a = 100
# b = (a**2 + a**2)**0.5
#
# screen = turtle.Screen()
# screen.bgcolor("light gray")
# house = turtle.Turtle()
#
#
# house.left(90)
# house.forward(a)
# house.right(90)
# house.forward(a)
# house.right(135)
# house.forward(b)
# house.left(135)
# house.forward(a)
# house.left(90)
# house.forward(a)
# house.left(45)
# house.forward(b/2)
# house.left(90)
# house.forward(b/2)
# house.left(90)
# house.forward(b)
#
# screen.mainloop()
#
# # 11
# n = -10
# count = 0
# if n < 0:
#     n = -1*n
# if n != 0:
#     while n != 0:
#         count = count + 1
#         n = n // 10
#     print(count)
# if n == 0:
#     print(1)

