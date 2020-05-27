回溯问题实际上就是解决一个决策树遍历的过程，下面是伪代码

    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return
        
        for 选择 in 选择列表:
            做选择
            backtrack(路径, 选择列表)
            撤销选择

其实就是在循环里面做递归。经典问题就是全排列问题：

    # 在循环中递归
    def backtrack(nums, track):
        if len(track) == len(nums):
            print(track)
            return
        for e in nums:
            if e in track:
                continue
            track.append(e)
            backtrack(nums, track)
            track.pop()