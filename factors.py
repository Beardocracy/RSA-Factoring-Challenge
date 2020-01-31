#!/usr/bin/python3

import sys

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

with open(sys.argv[1], 'r') as f:
    numbers = [int(num) for num in f.read().split()]
    
    for num in numbers:
        flag = 0
        print("{}=".format(num), end='')
        for prime in primes:
            if num % prime == 0:
                print("{}*{}".format(prime, num // prime))
                flag = 1
                break
        if flag == 0:
            for divisors in range(29, num // 2, 2):
                if num % divisors == 0:
                    print("{}*{}".format(divisors, num // divisors))
                    break
    
    '''
    line = f.readlines()
    for element in line:
        element = element.strip('\n') 
    print(line)
    '''
