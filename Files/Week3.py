# import turtle
#
# # First ten
#
# # 1-2
# day = int(input("What day is it today? "))
# stay = int(input("How long is your stay? "))
#
# day = ((day+stay) % 7)
#
# if day == 0:
#     print("Monday")
# elif day == 1:
#     print("Tuesday")
# elif day == 2:
#     print("Wednesday")
# elif day == 3:
#     print("Thursday")
# elif day == 4:
#     print("Friday")
# elif day == 5:
#     print("Saturday")
# elif day == 6:
#     print("Sunday")
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
#
#
#
#
# window.mainloop()
#
#
#
#
#
