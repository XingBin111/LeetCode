# BinSearch细节总结

BinSearch要非常小心搜索区间:
1. right = len(nums) 确定了搜索区间为[left, right), **于是也确定了while left < right(停止搜索是left=right)**
2. right = len(nums) - 1 确定了搜索区间为[left, right], **于是也确定了while left <= right(停止搜索时left=right+1)**


搜索区间决定了left和right和mid的关系:
1. 搜索区间为[left, right), 那么left和right的更新为: left = mid + 1, right = mid;
2. 搜索区间为[left, right), 那么left和right的更新为: left = mid + 1, right = mid - 1;


返回左侧边界和返回右侧边界决定了, 当nums[mid] == target的时候, 如何更新left和right:
1. 返回左侧边界: right = mid(搜索区间为[left, right))或right = mid - 1(搜索区间为[left, right]), 其实就是让搜索区间移动到target的左侧.
2. 返回右侧边界: left = mid + 1(因为两种搜索区间都包含了left, 所以都+1即可), 其实就是让搜索区间移动到target的右侧.

除了实现细节, 还要主要nums=[]和返回时的后处理.
