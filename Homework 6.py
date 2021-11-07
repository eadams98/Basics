# Excercise 5.33

def getInt(small=0, large=0):
    number = 0
    while not small <= number <= large:
        try:
            number = int(raw_input('Enter a number from ' + str(small) + ' to ' + str(large) + ': '))

            if not small <= number <= large:
                print 'Yo numba must be from ' + str(small) + ' to ' + str(large)
        except ValueError:
            print 'That is not a valid integer.'
        except EOFError:
            print 'Why did you do that?'
            print 'We will choose for you.'
            number = 7

# Excercise 5.34

def sliding(word, num = 3):

    if not isinstance(word, str):
        raise ValueError('')

    if not isinstance(num, int):
        raise ValueError('only integers work')

    if not num <= len(word):
        raise ValueError('num to long')
    

    for idx,x in enumerate(range(len(word)-(num-1))):
        y = ' '
        print (idx*y)+word[idx:idx+num]

# Excercise 5.35 (5.26)
#Redo Exercise 5.26 with strict error checking. Not only should you ensure
#that the base is legitimately in range, but also that the given string given is a legitimate
#literal for that base

def toDecimal(convert, base=10):
    
    if not isinstance(base, int):
        raise NameError('use an integer')

    if not isinstance(convert, str):
        raise NameError('try entering as a string')

    if not 2 <= base <= 36:
        print 'try entering a base from 2 - 36'

    
