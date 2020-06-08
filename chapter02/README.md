## 最大二叉堆(最小二叉堆)

最大二叉堆(也称优先级队列), 二叉堆其实就是完全二叉树, 但保存在数组中, 把数组的索引当作指针
最大二叉堆性质: 父节点 >= 左右节点
插入和删除的时间复杂度为O(logN)

**最大二叉堆中的数组不一定是有序的, 但root节点一定是最大的.**


## 双端链表实现LRU缓存

LRU缓存: 最近使用的数据放在最前面.

要求:
1. 设置最大缓存容量
2. put方法: 存入(key, val), 时间效率为O(1), 并将(key, val)存在缓存的首位
3. get方法: 获取(key, val), 时间效率为O(1), 并将(key, val)存在缓存的首位

设计: 使用哈希链表, 即双向链表和哈希表(字典)的结合.
1. 哈希表存: (key, ListNode), 并实现put和get
2. 双向链表: (key, ListNode), 实现addFirst和remove_last接口

在哈希表中查找和删除key的效率为O(1), 将查找到的key所对应的ListNode在双向量表中插入或删除效率为O(1), 这样就能实现LRU缓存


## 平衡二叉树
BST遍历非常巧妙和优雅, 要经常回顾.
二叉树的递归套路:
    
    TreeNode* BST(TreeNode root, int target) {
        if (root.val == target)
            // 找到目标，做点什么
        if (root.val < target) 
            root->right = BST(root.right, target);
        if (root.val > target)
            root->left = BST(root.left, target);
    }
    
1. 只需要关注当前节点, 其余交给递归框架
2. 如果当前节点会对下面的子节点有整体影响, 可以通过辅助函数增长参数列表, 借助参数传递信息.

## 反转链表
反转链表做法非常优雅和巧妙, 再次体现了递归的思想:

> 只需要关注当前节点, 其余交给递归框架