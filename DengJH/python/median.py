"""
给定两个有序的向量S1和S2, 如何找出它们归并后所得的有序向量S的中位数

方法1: 暴力法, 将S1和S2归并为有序向量S, 然后直接取中位数, 时间效率为O(n1+n2)
方法2: 方法1没有充分利用两个子向量已经有序,
"""