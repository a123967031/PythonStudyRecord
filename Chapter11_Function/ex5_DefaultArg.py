#!/usr/bin/env python

def tax(price, persents=0.01):
    tax = price * persents
    return tax

print tax(1000)
