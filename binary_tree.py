class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return f"{self.left.val} - {self.val} - {self.right}"


t1 = TreeNode(1)
t2 = TreeNode(3)
t1.left = t2
t3 = TreeNode(4)

t1.right = t3
t2.right = TreeNode(5)
print(t1)