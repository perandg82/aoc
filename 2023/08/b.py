#!/usr/bin/env python3

import time
import re
import threading

class mapper(threading.Thread):
    def __init__(self, d, instr, id, dindex, name):
        threading.Thread.__init__(self)
        self.d = d
        self.instr = instr
        self.id = id
        self.e = threading.Event()
        self.dindex = dindex
        self.sum = 0
        self.next = ""
        self.ffwd = 0
        self.name = name
        print("Inited with id {}".format(self.id))

    def is_running(self):
        return self.e.is_set()

    def step(self):
        self.e.set()

    def run(self):
        ii = 0
        self.next = self.d[self.id][0:3]
        while True:
            while True:
                self.e.wait()
                try:
                    char = self.instr[ii]
                except IndexError as err:
                    #print("Need to wrap, ii is {}".format(ii))
                    ii = 0
                    char = self.instr[ii]
                m = pattern.search(self.d[self.id])
                if m == None:
                    print("Something went awry!")
                    return
                #print("{}: {}".format(char, self.d[self.id][:-1]))
                if self.next != m.groups()[0]:
                    print("Mismatch! {} <> {}".format(self.next, m.groups()[0]))
                    return
                self.next = ""
                if char == "L":
                    self.next = m.groups()[1]
                elif char == "R":
                    self.next = m.groups()[2]
                else:
                    print("Something went to shit, ii is {}, len groups is {}".format(ii, len(m.groups())))
                    return
                self.id = self.dindex.index(self.next)
                ii += 1
                self.sum += 1
                if self.next[2] == "Z":
                    if self.ffwd != 0 and self.sum < self.ffwd:
                        pass
                    else:
                        self.ffwd = 0
                        print("{} got match on step {}! {}".format(self.name, self.sum, self.next))
                        self.e.clear()



pattern = re.compile("(\w*) = \((\w*), (\w*)\)")

f = open("inputa.txt", "r")
#f = open("testinput.txt", "r")
d = f.readlines()
f.close()

instr = d.pop(0)[:-1]
d.pop(0)


dindex = []
for elem in d:
    if len(elem) == 0:
        continue
    dindex.append(elem.split()[0])

procs = []

sum = 0
for l in dindex:
    if l[2] == "A":
        procs.append(mapper(d, instr, dindex.index(l), dindex, sum))
        sum += 1

for p in procs:
    p.start()
sum = 0
sums = []
for p in procs:
    p.step()
for p in procs:
    while p.is_running():
        time.sleep(0.01)
    sums.append(p.sum)
target = max(sums)
i = 0
while i < len(procs):
    while True:
        p = procs[i]
        print("Now looking for {} from {} (got {})".format(target, i, p.sum))
        p.ffwd = target
        if p.sum == target:
            i += 1
            break
        elif p.sum > target:
            i = 0
            target = p.sum
            break
        else:
            p.step()
            while p.is_running():
                time.sleep(0.01)

print(sum)
