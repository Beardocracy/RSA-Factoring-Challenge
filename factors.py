#!/usr/bin/python3

import sys

with open(sys.argv[1], 'r') as f:
    numbers = [int(num) for num in f.read().split()]
    length = len(numbers)
    for i in range(0, length):
            num = numbers[i]
            if num % 2 == 0:
                print("{}={}*{}".format(num, 2, num // 2))
            else:
                for divisors in range(3, num // 2, 2):
                    if num % divisors == 0:
                        print("{}={}*{}".format(num, divisors, num // divisors))
                        break
