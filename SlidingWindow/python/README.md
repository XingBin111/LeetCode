# 滑动窗口总结

使用左右指针来构造滑动窗口, 代码模板为:

    left = 0
    right = 0
    window = {}
    
    while right < len(s):
        c1 = s[right]
        window[c1] = window.get(c1, 0) + 1  # 更新window
        
        while valid:                        # 验证[left, right]区间的字符串是否满足问题的要求, 如果满足则慢指针右移.
            c2 = s[left]
            window[c2] -= 1             
            left += 1                       
           
        right += 1
       