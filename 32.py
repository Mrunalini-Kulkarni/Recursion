# Print all leaf nodes of a Binary Search Tree using recursion

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def print_leaf_nodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.key)
        return
    
    if root.left:
        print_leaf_nodes(root.left)
    if root.right:
        print_leaf_nodes(root.right)

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

print("Leaf nodes of the Binary Search Tree:")
print_leaf_nodes(root)
