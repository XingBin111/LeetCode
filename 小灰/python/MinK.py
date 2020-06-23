from chapter02.python.BinaryHeap import MaxPQ


# 返回nums中第k个最小的元素, 效率为O(nlogk), 使用in-place heap可以把空间效率降为O(1)
def min_k(nums, k):
    heap = MaxPQ(nums[:k])
    for i in range(k, len(nums)):
        if nums[i] < heap.pq[1]:
            heap.del_max()
            heap.insert(nums[i])
    return heap.del_max()


if __name__ == "__main__":
    nums = [7, 5, 15, 3, 17, 2, 20, 24, 1, 9, 12, 8]
    k = 6
    print(min_k(nums, k))


