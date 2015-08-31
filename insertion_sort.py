#!/usr/bin/env python3

def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

    return a

if __name__ == '__main__':
    assert(insertion_sort([]) == [])
    assert(insertion_sort([1]) == [1])
    assert(insertion_sort([3, 2, 1]) == [1, 2, 3])
    import random
    a = [random.randrange(100) for i in range(100)]
    assert(insertion_sort(a) == sorted(a))
