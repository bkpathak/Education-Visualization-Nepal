#!/usr/bin/env python

import csv

with open('levelwise_enrollment.csv', 'r') as csvinput:
    header = next(csvinput).strip() + ",Gender"
    print header
    count = 0
    for row in csvinput:
        count += 1
        field = row.strip().split(",")
        levelGender= field[1].split(" ")
        if count % 12 == 0 or count % 12 == 11:
            field[1] = " ".join(levelGender[0:-1]) + " level"
        else:
            field[1] = " ".join(levelGender[0:-1])
        if levelGender[-1] == "Girls":
            field.append("F")
        else:
            field.append("M")
        print ','.join(field)
