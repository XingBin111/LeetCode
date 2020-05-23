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


nums = [1, 2, 3]
track = []
backtrack(nums, track)