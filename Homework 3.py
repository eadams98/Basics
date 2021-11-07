words = 'slice'

level = []
for x in words:
    level.append(x)
    print ''.join(level)

import math

numbers = [1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    print x
    e = math.factorial(x)
    print e
    ee = float(1.0/math.factorial(x))
    print ee

baseConversion = raw_input('please enter a number to be converted:')
baseToConvertTo = raw_input('Please enter number of base from 1-10 that you want used:')
print int(baseConversion, int(baseToConvertTo))

y = len(baseConversion)
converted = 0
for x in baseConversion:
    y = y-1
    z=0
    print int(x)*(int(baseToConvertTo)**y)
    z = int(x)*(int(baseToConvertTo)**y)
    print x
    converted= converted+z
print 'mathmatical conversion:', converted

original = ['A', 'B', 'C', 'D', 'E', 'F']
for entry in original:
    print entry
    print 'after print entry:',original
    original.remove(entry)
    print 'after removal:', original
    original.append(entry)
    print 'after append:', original

"essential what's happening is that the order of the items in the list is constantly being altered, while the increment of the index is constant and as a consequence letters are being skipped"
