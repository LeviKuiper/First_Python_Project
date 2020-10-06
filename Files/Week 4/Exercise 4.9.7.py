
def sum_to_n(number):
    a = 0
    for i in range(number):
        a += number
        number = number - 1
    return a


n = 10
nsum = sum_to_n(n)
print(nsum)

