class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def treeHeight(node):
    if not node:
        return -1  # empty tree has height -1, single node = height 0
    if node.left or node.right:
        return 1 + (treeHeight(node.left) if treeHeight(node.left) > treeHeight(node.right) else treeHeight(node.right))
    else:
        return 0

def countLeaves(node):
    if not node: #empty tree has 0 leaves
        return 0
    if not node.left and not node.right: #reached the leaves
        return 1 
    return countLeaves(node.left) + countLeaves(node.right)

def isBinary(node, left = float('-inf'), right = float('inf')): #set default (initial) value of left and right is negative infinity and infinity
    if not node: #empty tree is binary
        return True
    if not (left < node.value < right): 
        return False
    return (isBinary(node.left, left, node.value) and
            isBinary(node.right, node.value, right))  #check left and right child

def isBalance(node):
    def check(node): #return tuple (height, isBalance())
        if not node: #empty Tree
            return -1, True
        
        if  (not node.left) or (not node.right): #reached leaf
            return 0, True
        
        leftHeight, leftBalance = check(node.left)
        rightHeight, rightBalance = check(node.right)
        
        #balanced tree -> both of its child is balanced, difference in height of the childs must less than 1
        if leftBalance and rightBalance and (abs(leftHeight - rightHeight) <= 1):
            balanced = True
        else:
            balanced = False 
        return treeHeight(node), balanced
    
    height, balanced = check(node)
    return balanced


def tree_info(node):
    height = treeHeight(node)
    leaves = countLeaves(node)
    binary = isBinary(node)
    balanced = isBalance(node)

    print(f"Height of the tree: {height}")
    print(f"Number of leaf nodes: {leaves}")
    print(f"Is a Binary Search Tree: {'Yes' if binary else 'No'}")
    print(f"Is Balanced: {'Yes' if balanced else 'No'}")


# # Example binary tree 
# #        1
# #       / \
# #      2   3
# #     / \ 
# #    4   5
# #       /
# #      6

# left111 = TreeNode(6)
# right11 = TreeNode(5,left111)
# left11 = TreeNode(4)
# right1 = TreeNode(3)
# left1 = TreeNode(2, left11, right11)
# root = TreeNode(1,left1, right1)

# tree_info(root)