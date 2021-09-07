import numpy as np


class ListNode:
    def __init__(self, v=0, nxt=None):
        self.val = v
        self.next = nxt


def partition(intvs, left, right):
    pivot = intvs[left]
    while left < right:
        while left < right and intvs[right] >= pivot:
            right -= 1
        intvs[left], intvs[right] = intvs[right], intvs[left]

        while left < right and intvs[left] <= pivot:
            left += 1
        intvs[left], intvs[right] = intvs[right], intvs[left]
    return left


def quick_sort(intvs, left, right):
    if left < right:
        mid = partition(intvs, left, right)
        quick_sort(intvs, left, mid - 1)
        quick_sort(intvs, mid + 1, right)


if __name__ == "__main__":
    intvs = [6, 3, 8, 2, 5, 9, 4, 5, 1, 7]

    quick_sort(intvs, 0, len(intvs)-1)
    print(intvs)
