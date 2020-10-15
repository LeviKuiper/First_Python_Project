import math
import string


def remove_punctuation(phrase):
    phrase_wo_punct = ""
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_wo_punct += letter
    return phrase_wo_punct


def calculate_distance(polar1, polar2):
    (r1, phi1) = polar1
    (r2, phi2) = polar2
    distance = ((r1**2) + (r2**2) - 2 * r1 * r2 * math.cos(phi2-phi1))**0.5
    return distance


# Calculate distance between two points based on polar coordinates

(x, y) = remove_punctuation(input("What are the polar coordinates of a? ")).split()
(z, w) = remove_punctuation(input("What are the polar coordinates of b? ")).split()

a = (int(x), int(y))
b = (int(z), int(w))

distance = calculate_distance(a, b)

print("The distance between a and b is equal to: ", distance)

