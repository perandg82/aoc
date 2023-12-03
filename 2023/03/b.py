#!/usr/bin/env python3

import re

def find_indexes(line):
    i = 0
    nums = []
    while i < len(line):
        try:
            match = line[i:].index("*")
            nums.append(match)
            i+=match+1
        except ValueError:
            break
    return nums

def find_nr_numbers(pattern):
    i = 0
    nums = 0
    t = [pattern[0].isdigit(), pattern[1].isdigit(), pattern[2].isdigit()]
    if t.count(True) == 0:
        return 0
    elif t == [True, False, True]:
        print("{} returning 2".format(t))
        return 2
    print("{} returning 1".format(t))
    return 1

#f = open("testinput.txt", "r")
f = open("inputa.txt", "r")
d = f.readlines()
f.close()
sum = 0
t = "."*len(d[0])
d.insert(0,t)
d.append(t)

for line in d[1:-1]:
    index = d.index(line)
    last_index = len(line)-1
    nums = find_indexes(line)
    for num in nums:
        nr_nrs = 0
        nr_nrs += find_nr_numbers(d[index-1][num-1:num+2])
        nr_nrs += find_nr_numbers(d[index][num-1:num+2])
        nr_nrs += find_nr_numbers(d[index+1][num-1:num+2])
        if nr_nrs == 2:
            print("Found a possible match:")
            print(d[index-1][num-4:num+5])
            print(d[index][num-4:num+5])
            print(d[index+1][num-4:num+5])


print(sum)
