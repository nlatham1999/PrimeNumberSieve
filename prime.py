#Nick Latham
#10/10/2020
#Alternate way of finding prime numbers using a more efficient version of the sieve of eratosthenes

import time
import matplotlib.pyplot as plt

#alteranate way of finding prime numbers
def primeSieve(n):
    sieve = [True] * n
    primes = [2, 3]
    i = 1
    while(True):
        for p in [i*6 - 1, i*6 + 1]:
            if(p > n):
                return primes
            if(sieve[p]):
                primes.append(p)
                if(p * p <= n):
                    newP1 = 0
                    j = i
                    while(newP1 < n):
                        # for x in [j * 6 - 1, j * 6 + 1]:
                        #     newP1 = x * p
                        #     if(newP1 < n):
                        #         sieve[newP1] = False
                        x = j * 6 - 1
                        newP1 = x * p
                        if(newP1 < n):
                            sieve[newP1] = False
                            x = j * 6 + 1
                            newP1 = x * p
                            if(newP1 < n):
                                sieve[newP1] = False
                        j += 1
        i += 1
    return primes

#adapted this algorithm from: https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def SieveOfEratosthenes(n): 
    primes = []
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True] * (n+1)
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    for p in range(n + 1): 
        if prime[p]: 
            primes.append(p)
    return primes


def graphTimes():
    testCases = [2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216]
    times1 = []
    times2 = []
    for x in testCases:
        sieve = 0
        eratosthenes = 0
        print("testing ", x)
        for _ in range(10):
            start = time.time()
            s1 = primeSieve(x)
            t1 = time.time() - start
            sieve += t1
            print(t1)
            start = time.time()
            s2 = SieveOfEratosthenes(x)
            t2 = time.time() - start
            eratosthenes += t2
            print(t2)
        times1.append(sieve/10)
        times2.append(eratosthenes/10)
    
        plt.plot(times1)
        plt.plot(times2)
        plt.legend(['Alternate Way', 'Eratosthenes Sieve'], loc=4)
        plt.show()

def compareResults():
    s1 = primeSieve(1000)
    s2 = SieveOfEratosthenes(1000)
    i = 0
    while(i < len(s1) and i < len(s2)):
        print(s1[i], " ", s2[i])
        i += 1
    print(len(s1))

def simpleTimeTest():
    for _ in range(10):
        start = time.time()
        s1 = primeSieve(10000000)
        t1 = time.time() - start
        print(t1)
        start = time.time()
        s2 = SieveOfEratosthenes(10000000)
        t2 = time.time() - start
        print(t2)

# graphTimes()
# compareResults()
simpleTimeTest()

