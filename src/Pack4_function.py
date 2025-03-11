# Project: Prog_Projet2048
# Title: Pack4_function
# Author: Kilian Testard
# Version: 0.4 11.03.2025


# function to pack any set of values in any direction
def pack4(a, b, c, d, score):
    # base value for counting the fusions
    nb_fusion = 0

    # pack the values in one direction
    if c == 0:
        c, d = d, 0
        if c != 0:
            nb_fusion += 1
    if b == 0:
        b, c, d = c, d, 0
        if b != 0:
            nb_fusion += 1
    if a == 0:
        a, b, c, d = b, c, d, 0
        if a != 0:
            nb_fusion += 1

    # pack two identical values together, add the fusion to the score
    if a == b and a != 0:
        a = 2 * a
        b = c
        c = d
        d = 0
        nb_fusion += 1
        score += a
    if b == c and b != 0:
        b = 2 * b
        c = d
        d = 0
        nb_fusion += 1
        score += b
    if c == d and c != 0:
        c = 2 * c
        d = 0
        nb_fusion += 1
        score += c

    # return the new values
    return [a, b, c, d,nb_fusion, score]

# print the results and count the total amount of fusions that occurred
# print(pack4(16,16,2,2)[:4], "Nombre de fusions effectuées : ", pack4(16,16,2,2)[4])