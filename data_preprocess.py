#!/usr/bin/env python

import csv

with open('levelwise_enrollment.csv', 'r') as csvinput:
    header = next(csvinput).strip() + ",Gender"
    writer = csv.writer(csvoutput, delimiter = ',')
    print header
    for row in csvinput:
        field = row.strip().split(",")
        levelGender= field[1].split(" ")
        field[1] = levelGender[0]
        if levelGender[1] == "Girls":
            field.append("F")
        else:
            field.append("M")
        print ','.join(field)

