#!/usr/bin/env python3

def selection_sort(a):
    a = a[:]
    for i in range(len(a) - 1):
        m_index = i
        for j in range(i, len(a)):
            if a[j] < a[m_index]:
                m_index = j
        a[i], a[m_index] = a[m_index], a[i]

    return a

if __name__ == '__main__':
    assert(selection_sort([]) == [])
    assert(selection_sort([1]) == [1])
    assert(selection_sort([3, 2, 1]) == [1, 2, 3])
    import random
    a = [random.randrange(100) for i in range(100)]
    assert(selection_sort(a) == sorted(a))
