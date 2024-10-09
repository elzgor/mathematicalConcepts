# Checks whether a number x is prime
def isPrime(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
    return True

# Checks for any prime divisors between 2 and x
def smallDiv(x):
    for i in range(2,x):
        if (x % i == 0) and (isPrime(i)):
            return i
    return x

# Prime factor decomposition of x
def primeFactDecomp(x):
    allPF = []
    while smallDiv(x) != x:
        allPF.append(smallDiv(x))
        x = int(x/smallDiv(x))
    allPF.append(x)
    return allPF

# Largest positive integer (below N) only divisible by both p and q
# E.G. M(2,11,100) = 88 since 2(^3) * 11 = 88 and 88 < 100
def M(p,q,N):
    for n in range(N,0,-1):
        if (set(primeFactDecomp(n)) == {p,q}):
            return n
    return 0

# Sum of all distinct M(p,q,N)
def S(N):
    sum = 0
    apun = [item for item in [i if isPrime(i) else None for i in range(2,N+1)] if item is not None]
    print("APUN::: ", apun)
    for i in range(0,len(apun)):
        for j in range(i+1,len(apun)):
            sum += M(apun[i],apun[j],N)
            print(apun[i],apun[j],N, "---", sum)
    return(sum)

whichS = input("Which number would you like to give as the limit? ")
print("ANSWER: ", S(int(whichS)))
