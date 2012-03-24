#-*- coding: utf-8 -*-
def merge_and_count(a, b):
    assert a == sorted(a) and b == sorted(b)
    c = []
    count = 0
    i, j = 0, 0
    while i < len(a) and j < len(b):
        c.append(min(b[j], a[i]))
        if b[j] < a[i]:
            count += len(a) - i # number of elements remaining in `a`
            j+=1
        else:
            i+=1
        # now we reached the end of one the lists
    c += a[i:] + b[j:] # append the remainder of the list to C
    return count, c

def sort_and_count(L):
    if len(L) == 1: return 0, L
    n = len(L) // 2
    a, b = L[:n], L[n:]
    ra, a = sort_and_count(a)
    rb, b = sort_and_count(b)
    r, L = merge_and_count(a, b)
    return ra+rb+r, L

def count_inversions_brute_force(permutation):
    """Count number of inversions in the permutation in O(N**2)."""
    return sum(pi > permutation[j]
    for i, pi in enumerate(permutation)
    for j in xrange(i+1, len(permutation)))

if __name__ == "__main__":
    l = list()
    with open("static\IntegerArray.txt", "r") as f:
        for numero in f:
            l.append(int(numero))

        print count_inversions_brute_force(l) #2407905288
