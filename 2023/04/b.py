#!/usr/bin/env python3

import re

index_re = re.compile("Card\s+(\d*):")

#f = open("testinput.txt", "r")
f = open("inputa.txt", "r")
d = f.readlines()
f.close()

sums = [1]*len(d)

for line in d:
    try:
        index = int(index_re.search(line).groups()[0])-1
    except Exception as e:
        print("Caught {}, invalid line: {}".format(e, line))
        continue

    winning, mine = line.split(":")[1].split("|")
    results = 0
    for num in mine.split():
        results += winning.count(" {} ".format(num))

    print()
    print(line[:-1])
    print("Got {} results".format(results))
    for r in range(results):
        try:
            sums[index+1+r] += sums[index]
            print("{}: {}".format(index+1+r, sums[index+1+r]))
        except IndexError:
            print("Got exception on index {}, max is {}".format(index+1+r, len(d)))
            break

print(sum(sums))
