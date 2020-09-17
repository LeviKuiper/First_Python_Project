
a = int(input("which exercises do you want to run?: "))

if a == 1:
    # 2.1
    a = "all"
    b = "work"
    c = "and"
    d = "no"
    e = "play"
    f = "makes"
    g = "Jack"
    h = "a"
    i = "dull"
    j = "boy"
    print(a, b, c, d, e, f, g, h, i, j)

    # 2.2
    print(6 * (1-2))

    # 2.4
    bruce = 6
    print(bruce + 4)

    # 2.5
    print("please enter the correct values")

    P = float(input("Principal Amount: "))
    r = float(input("nominal interest rate: "))
    n = float(input("compounding interval: "))
    t = float(input("holding years: "))

    A = P*(1+(r/n))**(n*t)
    print(A)

    # 2.6
    print(5 % 2)
    print(9 % 4)
    print(15 % 12)
    print(12 % 15)
    print(6 % 6)
    print(0 % 7)

    # 2.7
    print((51+14)//24)
    print((51+14) % 24)

    # 2.8
    a = int(input("what time is it in hours: "))
    b = int(input("How many hours until the alarm: "))
    c = (a+b) % 24
    print("The time you will wake up is: ", c)

else:
    decider = input("What is your mode of transportation? ")

    if decider == "walk":
        km_travel = int(input("How many km do you want to travel? "))
        speed_walk = int(input("How fast do you walk in km/u? "))
        hours_travelled = km_travel // speed_walk
        minutes_travelled = 60 * ((km_travel % speed_walk)/speed_walk)
        print("You will travel for ", hours_travelled, "hours and ", minutes_travelled, "minutes")

    if decider == "bike":
        km_travel = int(input("How many km do you want to travel? "))
        speed_bike = int(input("How fast do you bike in km/u? "))
        hours_travelled = km_travel // speed_bike
        minutes_travelled = 60 * ((km_travel % speed_bike)/speed_bike)
        print("You will travel for ", hours_travelled, "hours and ", minutes_travelled, "minutes")

    if decider == "car":
        km_travel = int(input("How many km do you want to travel? "))
        speed_car = int(input("How fast do you ride in km/u? "))
        hours_travelled = km_travel // speed_car
        minutes_travelled = 60 * ((km_travel % speed_car)/speed_car)
        print("You will travel for ", hours_travelled, "hours and ", minutes_travelled, "minutes")

