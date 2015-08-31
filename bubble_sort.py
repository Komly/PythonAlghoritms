#!/usr/bin/env python3

def bubble_sort(a):
    a = a[:]
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

if __name__ == '__main__':
    assert(bubble_sort([]) == [])
    assert(bubble_sort([1]) == [1])
    assert(bubble_sort([3, 2, 1]) == [1, 2, 3])
    import random
    a = [random.randrange(100) for i in range(100)]
    assert(bubble_sort(a) == sorted(a))
