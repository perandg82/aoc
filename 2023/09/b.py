#!/usr/bin/env python3

import re
def find_val(d):
    print("Finding val for {}".format(d))
    index = 0
    while True:
        new_line = []
        line = d[index]
        #print("About to start iter {}, d len is {}, line len is {}".format(index, len(d), len(line)))
        index+=1
        for i in range(len(line)-1):
            new_line.append(line[i+1]-line[i])
        if new_line.count(0) == len(new_line):
            d.append(new_line)
            #print("Appended new line")
            print("Done!")
            #print(d)
            break
        else:
            d.append(new_line)
            #print("Appended new line")
            #print(new_line)

    for i in range(len(d)-1, -1, -1):
        if i == len(d)-1:
            d[i].insert(0, 0)
        else:
            d[i].insert(0, d[i][0] - d[i+1][0])
    for line in d:
        print(line)
    return d[0][0]

pattern = re.compile("^\D*(\d)")

f = open("inputa.txt", "r")
#f = open("testinput.txt", "r")
d = f.readlines()
f.close()

#print(find_val([[0,3,6,9,12,15]]))
#print(find_val([[1,3,6,10,15,21]]))
#print(find_val([[10,13,16,21,30,45]]))

score = []
for line in d:
    d_int = []
    for w in line.split(" "):
        d_int.append(int(w))
    score.append(find_val([d_int]))
print("Len is {} and sum is {}".format(len(score), sum(score)))

print(find_val([[0,1,1,0]]))
