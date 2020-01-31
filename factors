#!/usr/bin/python3

import sys

with open(sys.argv[1], 'r') as f:
    for num in f.read().split():
        num = int(num)
        if num % 2 == 0:
            print("{}={}*{}".format(num, 2, num // 2))
        else: 
            for divisors in range(3, num // 2, 2):
                if num % divisors == 0:
                    print("{}={}*{}".format(num, divisors, num // divisors))
                    break
