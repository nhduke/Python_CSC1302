"""
Python Exam: Binary Search Trees
--------------------------------

Time limit: ~1 hour
Rules:
- Do NOT import any extra libraries (only built-ins are allowed).
- Work only with the code in this file.
- Only modify the parts marked with TODO comments.

Goal:
We work with a Binary Search Tree (BST).

A BST is a binary tree where for every node:
    - all values in the left subtree are < node.value
    - all values in the right subtree are > node.value

You must implement three methods inside the BinarySearchTree class:

    1) insert(self, value)         [4 pts]
    2) contains(self, value)       [3 pts]
    3) to_list_inorder(self)       [3 pts]

An auto-grader in a separate file will test your code.
Total: 10 points
"""


# ---------------------------------------------------------------------
# BINARY SEARCH TREE IMPLEMENTATION (SKELETON)
# ---------------------------------------------------------------------

class Node:
    """A node in the binary search tree."""
    def __init__(self, value):
        self.value = value
        self.left = None   # Node or None
        self.right = None  # Node or None


class BinarySearchTree:
    """Simple Binary Search Tree storing integers."""
    def __init__(self):
        self.root = None

    # -------------------------------------------------------------
    # Q1: insert(self, value)  [4 pts]
    # -------------------------------------------------------------
    def insert(self, value):
        """
        Insert a new value into the BST.

        Requirements:
        - If the tree is empty, the new value becomes the root.
        - Otherwise, compare the value with the current node:
            * If value < node.value: go to the left subtree.
            * If value > node.value: go to the right subtree.
        - Insert the value in the correct place following BST rules.
        - You can ignore duplicate values (i.e., do not insert if equal).

        This method should NOT return anything (return None).
        """
      
        # TODO: Implement this method.
        if self.root is None:
                self.root = Node(value)
                return None
        else:
            current = self.root
            while value != current.value:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
        return None    


    # -------------------------------------------------------------
    # Q2: contains(self, value)  [3 pts]
    # -------------------------------------------------------------
    def contains(self, value):
        """
        Return True if the BST contains 'value', otherwise False.

        Requirements:
        - Start from the root and search down the tree using BST logic:
            * If value == node.value: found -> return True
            * If value < node.value: search in left subtree
            * If value > node.value: search in right subtree
        - If you reach a None node, the value is not in the tree.
        """
        # TODO: Implement this method.
        if self.root:
            current = self.root
            while current:
                if value == current.value:
                    return True
                if value < current.value:
                    current = current.left
                else:
                    current = current.right
        return False

    # -------------------------------------------------------------
    # Q3: to_list_inorder(self)  [3 pts]
    # -------------------------------------------------------------
    def to_list_inorder(self):
        """
        Return a list of all values of the BST in *ascending* order.

        Requirements:
        - Use an in-order traversal:
              left subtree -> node -> right subtree
        - Collect the values in a Python list and return it.
        - You may implement this using a helper function (recursion) or
          using an explicit stack. Both are allowed.

        Example:
            If the tree contains values [7, 3, 9, 1, 5],
            to_list_inorder() might return [1, 3, 5, 7, 9]
        """
        # TODO: Implement this method.
        result = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            result.append(node.value)
            inorder(node.right)

        inorder(self.root)
        return result
# ---------------------------------------------------------------------
# DO NOT MODIFY BELOW THIS LINE
# ---------------------------------------------------------------------

if __name__ == "__main__":
    # Import and run the auto-grader from a separate file
    from bst_grader import run_autograder

    run_autograder(BinarySearchTree)
