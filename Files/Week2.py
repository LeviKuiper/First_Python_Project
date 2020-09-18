def time_arrive(x, y, z):
    hours_total = x / y
    total_minutes_travelled = hours_total * 60 + z
    hours_travelled = total_minutes_travelled // 60
    minutes_travelled = total_minutes_travelled % 60
    print("You will arrive in ", int(hours_travelled), "hours and ", int(minutes_travelled), "minutes")


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

    print("bye")
    exit()

if a == 2:
    km_travel = int(input("How many km do you want to travel? "))
    decider = input("What is your mode of transportation? ")

    if decider == "walk":
        speed = int(input("How fast do you walk in km/u? "))
        if speed >= 30:
            print("Look at you, Usain Bolt.")

    if decider == "bike":
        speed = int(input("How fast do you bike in km/u? "))
        if speed >= 40:
            print("Wow you must be so fast")
        if speed <= 5:
            print("You sure you don't want to walk?")

    if decider == "car":
        speed = int(input("How fast do you ride in km/u? "))
        if speed >= 160:
            print("Don't go breaking no traffic regulations now. ")
        if speed <= 20:
            print("Save the environment, take a bike.")

    minutes_prepare = int(input("How long does it take to get prepared to leave in minutes? "))
    minutes_arrival = int(input("How long does it take to find parking? "))
    time_arrive(km_travel, speed, minutes_prepare)

else:
    print("Bye")
    exit()
