#-*- coding: utf-8 -*-
def heapsort(lst):
    ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''

    # in pseudo-code, heapify only called once, so inline it here
    for start in range((len(lst)-2)/2, -1, -1):
        siftdown(lst, start, len(lst)-1)

    print 'antes 2loop', lst
    for end in range(len(lst)-1, 0, -1):
        print '2loop', lst, end, lst[end]

        lst[end], lst[0] = lst[0], lst[end]

        print '2troca', lst
        siftdown(lst, 0, end - 1)
    return lst

def siftdown(lst, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break
        print lst

if __name__ == "__main__":
    print heapsort([1,7,5,8,4,9])