#!/usr/bin/env python3

def quick_sort(a):
    if not a:
        return []
    pivot = a[0]
    less = quick_sort([x for x in a if x < pivot])
    more = quick_sort([x for x in a if x > pivot])
    equal = [x for x in a if x == pivot]
    return less + equal + more


if __name__ == '__main__':
    assert(quick_sort([]) == [])
    assert(quick_sort([1]) == [1])
    assert(quick_sort([3, 2, 1]) == [1, 2, 3])
    import random
    a = [random.randrange(100) for i in range(100)]
    assert(quick_sort(a) == sorted(a))
