#!/usr/bin/env python3

import random

def isPrime(p):
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    i = 3
    maxi = p**0.5 + 1
    while i <= maxi:
        if p % i == 0:
            return False
        i += 2

    return True


def setPrime():
    p = random.getrandbits(16)
    q = random.getrandbits(16)
    while isPrime(p) == False:
        p = random.getrandbits(16)
    while isPrime(q) == False:
        q = random.getrandbits(16)
    
    return p * q


def modulo(a, b, n):
    return (a ** b) % n