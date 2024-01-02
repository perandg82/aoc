#!/usr/bin/env python3

import re

pattern = re.compile("^\D*(\d)")

f = open("inputa.txt", "r")
d = f.readlines()
f.close()

times = ""
for elem in d[0][:-1].split(" "):
    times += elem

times = [int(times)]
dists = ""
for elem in d[1][:-1].split(" "):
    dists += elem

dists = [int(dists)]

#times = [7,15,30]
#dists = [9,40,200]
#times = [71530]
#dists = [940200]

print(times)
print(dists)

sums = []

for i in range(len(dists)):
    time = times[i]
    sum = 0
    for j in range(time-1, 0, -1):
        speed = j
        distance_traveled = speed * (time-j)
        if distance_traveled > dists[i]:
            #print("  VALID: {}, {} > {}".format(j, distance_traveled, dists[i]))
            sum += 1
        #else:
            #print("INVALID: {}, {} < {}".format(j, distance_traveled, dists[i]))
    sums.append(sum)

print(sums)
sum = 1
for s in sums:
    sum = sum*s
print(sum)
