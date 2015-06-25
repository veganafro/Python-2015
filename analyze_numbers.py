#Check out this program. It confirms if a number is odd, prime, or abundant.

def odd(x):
    case = True
    if (int(x) % 2) == 0:
        case = False
        print("%s is not odd" % (x))
    else:
        print("%s is odd" % (x))
    return case

def prime(x):
    divisors = 0
    case = True
    for factors in range(2, x):
        notprime = x % factors
        if notprime == 0:
            case = False
            divisors += 1
            break
    if divisors >= 1:
        print("%s is not prime" % (x))
    else:
        print("%s is prime" % (x))
    return case

def abundant(x):
    divisors = 0
    case = False
    for factors in range(2, x):
        if (x % factors) == 0:
            divisors = divisors + factors
    if divisors > x:
        case = True
        print("%s is abundant" % (x))
    else:
        print("%s is not abundant" % (x))
    return case

usernumber = int(input("What number would you like to test? "))

odd(usernumber)
prime(usernumber)
abundant(usernumber)
