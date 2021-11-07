import os

data = open(os.path.expanduser('~/Desktop/dup.in.py'))

pos = 0
found = False

for dups in range(6):
    line = data.readline()
    pieces = line.split()
    #pieces = [int(i) for i in pieces]
    for dups in pieces:
        while pos < len(dups) and found == False:
            if dups == dups[pos]:
                found = True
                print 'found dup at index', dups[pos]
            else:
                pos = pos + 1
    


def sqrtA(n):
    guess = 1.0
    while guess != n/guess:
        guess = (guess + n/guess) / 2.0
        print 'current guess is', guess

    return guess
