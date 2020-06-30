"""
使用字典来实现一个简易的graph算法
BFS使用辅助队列, DFS使用辅助栈, 时间复杂度O(n^2+e), e为边的个数, 可以给每个节点一个visited状态, 这样就不用每次检测是否在traveled中, 时间复杂度可以简化为O(n+e)
"""
from queue import Queue


def bfsTravel(graph, source):
    q = Queue()
    q.put(source)
    traveled = []
    while q.qsize() > 0:
        cur = q.get()
        if cur not in traveled:
            traveled.append(cur)
        for nxt in graph[cur]:
            if nxt not in traveled:
                q.put(nxt)
    return traveled


def dfsTravel(graph, source):
    traveled = []
    stack = [source]
    while stack:
        cur = stack.pop()
        if cur not in traveled:
            traveled.append(cur)
        for nxt in graph[cur]:
            if nxt not in traveled:
                stack.append(nxt)
    return traveled


if __name__ == "__main__":
    graph = {}
    graph['a'] = ['b', 'c']
    graph['b'] = ['d', 'e']
    graph['c'] = ['f']
    graph['d'] = ['h']
    graph['e'] = []
    graph['f'] = ['g']
    graph['g'] = ['c']
    graph['h'] = ['e']

    print(bfsTravel(graph, "a"))
    print(dfsTravel(graph, "a"))
