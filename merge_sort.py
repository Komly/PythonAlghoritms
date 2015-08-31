#!/usr/bin/env python3

def merge_sort(a):
    if not a:
        return a
    if len(a) == 1:
        return a
    mid = len(a) // 2

    a, b = merge_sort(a[mid:]), merge_sort(a[:mid])

    ai, bi = 0, 0
    merged = []
    while ai < len(a) and bi < len(b):
        if a[ai] < b[bi]:
            merged.append(a[ai])
            ai += 1
        else:
            merged.append(b[bi])
            bi += 1
    if ai < len(a):
        merged.extend(a[ai:])
    if bi < len(b):
        merged.extend(b[bi:])
    return merged

if __name__ == '__main__':
    assert(merge_sort([]) == [])
    assert(merge_sort([1]) == [1])
    assert(merge_sort([3, 2, 1]) == [1, 2, 3])
    import random
    a = [random.randrange(100) for i in range(100)]
    assert(merge_sort(a) == sorted(a))
