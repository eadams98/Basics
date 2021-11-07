from decimal import *
from random import sample, randint


def greeting():
    print 'This interest calculator will ask you to select an interest rate, followed by a principal value. It will then calculate and displa the principal value. It will then calulate and display the principal, interest rate, and balance after one year. you will then be invited to execute the process again or terminate. \n'


def getRate(random):

    choices = [chr(k+ord('A')) for k in range(len(random))]
    

    incorrectLetter = True
    correctLetter = False
    while incorrectLetter:

            print 'Please select an interest rate:'

            for x in range(len(random)):
                print choices[x] + ') ' + str(random[x]) + '%'

            userRateText = 'Enter ' + str(choices[0]) + '-' + str(choices[len(random) - 1]) + ': '
            userRate = raw_input(userRateText)
            print 

            choices = choices[0:len(random)]
            
            for idx,x in enumerate(choices):
                if x == userRate:
                    correctLetter = True
                    userRate = idx
                    
                    

            if correctLetter == False:
                print 'That is not a valid selection. \n'
            else:
                incorrectLetter = False

    try:
        userRate = float(random[userRate])/100
        
    except IndexError:
        pass

    return userRate
                 

def getPrincipal(limit = '1000000'):

    inproperGreeting = True
    
    while inproperGreeting:

        
                                    
        try:
            
            principalSTR = raw_input('Enter principle: ')
        
            try:
                if principalSTR[0] == '$':
                    principalSTR = principalSTR[1:len(principalSTR)]
            except IndexError:
                pass

            principal = float(principalSTR)
            
            if principal <= 0:
                print 'You must enter a positive amount.'
                print
            elif principal >= int(limit):
                print 'The principal must be less than $1 million.'
                print
            elif principal > 0 and principal < 1000000 and principalSTR.find('.') == -1:
                inproperGreeting = False
                principal = '%d.%s' % (principal, '00')
                break
            else:
                x = principalSTR.find('.')
                if x != -1:
                    principalNewSTR = principalSTR[principalSTR.find('.')+1: len(principalSTR)]
                    if len(principalNewSTR) == 2:
                        inproperGreeting = False
                    elif len(principalNewSTR) == 1:
                        inproperGreeting = False
                    else:
                        print 'The principal must be specified in dollars and cents.'
                        print
    

        except ValueError:
            print 'Please enter a number'
            print
    print
    
    return principal
    

    
def computerBalance(principal, rate):
    return principal + (principal * rate)
    

def calculation(value = 0):
    value = balance

    print 'intial Principal \t Interest Rate \t End of Year Balance'
    print '=' * 58
    print '$%.2f \t\t\t %.2f \t\t $%.2f ' % (principal, rate, value)
    print  

greeting()
need = True
while need:
    
    options = sorted(sample(range(1,20), randint(2,6)))
    
    rate = getRate(options)
    
    principalSTR = getPrincipal()
    principal = float(principalSTR)
    balance = computerBalance(principal, rate)
    calculation()

    inconclusive = True

    while inconclusive:
        try:
            answer = raw_input('another Computation [y/n]? ')
            print

            if answer[0] == 'Y' or answer[0] == 'y':
                inconclusive = False
                pass
            elif answer[0] == 'N' or answer[0] == 'n':
                need = False
                inconclusive = False
                print 'Exiting comupation. Thank you.'
            elif answer == '':
                pass
            else:
                pass

        except IndexError:
            pass

#ord (function: ord('Y') returns number which letter,symbol, upper, lower, etc. occurs
#chr (function: chr(72) returns the corresponding letter, symbol, upper, lower, etc. 
