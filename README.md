# PrimeNumberSieve

This is a prime number sieve that is based off of the Sieve of Eratosthenes.

Unlike the Sieve of Eratosthenes, not every number is checked when making the sieve, therefore making the process more efficient.

numbers are split up into groups of six:
the first number is a multiple of 6 and is not prime
the second number is a potential prime number
the third number is even and so it is not a prime
the fourth number is a multiple of 3 and is not a prime
the fifth number is even and is not a prime
the sixth number is a potential prime number

therefore all potential primes are 2, 3, and {i*6-1, i*6+1} for all integers i >= 1
also all potential primes are either primes or are a product of two potential primes

algorithm:
create a bolean array of length n and set each element to true
add 2 and 3 to the list of primes
set i = 1 and iterate
for each potential prime, i*6-1 and i*6+1, 
  if the value of the boolean array at that position is true, 
    then add it to the list of the primes
    set j = i and iterate
    for each potential prime j*6-1 and j*6+1
      set the value of the boolean array at the position of the product of the two potential primes to be false
      

analysis:

This seems to be the same time complexity of The Sieve of Eratosthenes, but more slightly more efficient. I have also found that it takes up less memory.



