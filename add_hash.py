#!/usr/bin/env python

def add_hash(array):
    return sum(array) & 0x0ff

if __name__ == '__main__':
    print add_hash([23,42,56,67,89,100,56,3,98,234,22222,234,-345,2435,33])
