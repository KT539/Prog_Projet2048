# Project: Prog_Projet2048
# Title: Pack4_function
# Author: Kilian Testard
# Version: 0.2 04.02.2025

# function to pack any set of values in any direction
def pack4(a, b, c, d):
    fusion = 0
    if c == 0:
        c, d = d, 0
        if c != 0:
            fusion += 1
    if b == 0:
        b, c, d = c, d, 0
        if b != 0:
            fusion += 1
    if a == 0:
        a, b, c, d = b, c, d, 0
        if a != 0:
            fusion += 1
    if a == b and a != 0:
        a = 2 * a
        b = c
        c = d
        d = 0
        fusion += 1
    if b == c and b != 0:
        b = 2 * b
        c = d
        d = 0
        fusion += 1
    if c == d and c != 0:
        c = 2 * c
        d = 0
        fusion += 1
    return [a, b, c, d,fusion]

# print the results and counts the amount of fusions that occurred
# print(pack4(16,16,2,2)[:4], "Nombre de fusions effectuées : ", pack4(16,16,2,2)[4])

# COMMENTAIRES A AJOUTER