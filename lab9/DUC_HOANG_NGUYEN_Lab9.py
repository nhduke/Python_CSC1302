class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


#Traverse the tree - Pre order traversal (Root -> Left -> Right)
def traversePreOrder(node: TreeNode):
    #TODO1: implement this function
    # traverse the tree in pre-order and print the value of each node
    if node is None:
        return
    
    print(node.value, end=" ")
    
    traversePreOrder(node.left)
    traversePreOrder(node.right)
    

def trim(node: TreeNode):
    #TODO2: implement this function. Method should decrease the values of every node of the tree by 1
    if node is None:
        return
    node.value -= 1
    
    trim(node.left)
    trim(node.right)


def trim_leaves(node: TreeNode):
    #TODO3: implement this function. Method should decrease the values of every LEAF node by 1
    if node is None:
        return
    
    if (not node.left) and (not node.right):
        node.value -= 1
        return
    
    if node.left:
        trim_leaves(node.left)
    if node.right:
        trim_leaves(node.right)

def mirror(node: TreeNode):
    #TODO4: implement this function. Method should swap the left and right subtrees
    if node is None:
        return
    

    if node.left and node.right:
        node.left, node.right = node.right, node.left
        
    if node.left:
        mirror(node.left)
    if node.right:
        mirror(node.right)    
    
    
        
    
    

    

# ====== Test code - do not modify ======
#Build the sample tree
# Tree1
grand_child1 = TreeNode(4, None, None)
grand_child2 = TreeNode(5, None, None)
child1 = TreeNode(9, grand_child1,  grand_child2)
child2 = TreeNode(8, None, None)
parent1 = TreeNode(3, child1, child2)

# Tree2
grand_child3 = TreeNode(4, None, None)
grand_child4 = TreeNode(5, None, None)
child3 = TreeNode(9, grand_child3, None)
child4 = TreeNode(8, None,  grand_child4)
parent2 = TreeNode(3, child3, child4)


def print_answer(parent):
    print('Original tree:')
    traversePreOrder(parent)

    print('\nAfter trimming entire tree:')
    trim(parent)
    traversePreOrder(parent)


    print('\nAfter trimming only the leaves:')
    trim_leaves(parent)
    traversePreOrder(parent)

    print('\nAfter mirroring the tree:')
    mirror(parent)
    traversePreOrder(parent)


print('===== Tree 1 =====')
print_answer(parent1)
print('\n---\n')
print('===== Tree 2 =====')
print_answer(parent2)
