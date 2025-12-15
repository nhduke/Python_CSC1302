# ---------------------------------------------------------------------
# DO NOT MODIFY BELOW THIS LINE
# AUTO-GRADER FOR TESTING THE IMPLEMENTATION
# ---------------------------------------------------------------------
# bst_grader.py

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


class RefNode:
    """Internal node type for building reference trees."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _inorder_manual(node, out_list):
    """Internal helper for grading Q1 (works on any node with left/right/value)."""
    if node is None:
        return
    _inorder_manual(node.left, out_list)
    out_list.append(node.value)
    _inorder_manual(node.right, out_list)


def _insert_manual(root, value):
    """Internal helper to build a correct reference BST."""
    if root is None:
        return RefNode(value)
    if value < root.value:
        root.left = _insert_manual(root.left, value)
    elif value > root.value:
        root.right = _insert_manual(root.right, value)
    # ignore duplicates
    return root


def _build_reference_tree(values):
    """Build a reference BST using only internal code."""
    root = None
    for v in values:
        root = _insert_manual(root, v)
    return root


def run_autograder(BST_class):
    """
    Run auto-grader on a given BinarySearchTree class.

    BST_class must:
    - have attribute 'root'
    - implement methods: insert, contains, to_list_inorder
    """
    print("Running auto-grader for BinarySearchTree...\n")

    total_score = 0
    max_score = 10

    values_to_insert = [7, 3, 9, 1, 5, 8, 10]
    expected_inorder = [1, 3, 5, 7, 8, 9, 10]

    # -----------------------------------------
    # Q1: insert (4 pts) — uses student's insert
    # -----------------------------------------
    bst_q1 = BST_class()
    try:
        for v in values_to_insert:
            bst_q1.insert(v)

        inorder_values = []
        _inorder_manual(bst_q1.root, inorder_values)

        if inorder_values == expected_inorder:
            total_score += 4
            print(f"{GREEN}Q1 insert: 4/4{RESET}")
        else:
            if bst_q1.root is not None:
                total_score += 2
                print(f"{RED}Q1 insert: 2/4 (tree built but incorrect structure/order){RESET}")
            else:
                print(f"{RED}Q1 insert: 0/4 (tree is empty after insert){RESET}")
    except Exception as e:
        print(f"{RED}Q1 insert: 0/4 (exception: {e}){RESET}")

    # -----------------------------------------
    # Q2: contains (3 pts) — uses reference tree, only tests contains
    # -----------------------------------------
    bst_q2 = BST_class()
    bst_q2.root = _build_reference_tree(values_to_insert)

    try:
        tests = [
            (7, True),
            (1, True),
            (10, True),
            (6, False),
            (0, False),
        ]
        correct = True
        for value, expected in tests:
            result = bst_q2.contains(value)
            if result != expected:
                correct = False
                break

        if correct:
            total_score += 3
            print(f"{GREEN}Q2 contains: 3/3{RESET}")
        else:
            print(f"{RED}Q2 contains: 0/3 (wrong True/False results){RESET}")
    except Exception as e:
        print(f"{RED}Q2 contains: 0/3 (exception: {e}){RESET}")

    # -----------------------------------------
    # Q3: to_list_inorder (3 pts) — uses reference tree, only tests traversal
    # -----------------------------------------
    bst_q3 = BST_class()
    bst_q3.root = _build_reference_tree(values_to_insert)

    try:
        inorder_list = bst_q3.to_list_inorder()
        if inorder_list == expected_inorder:
            total_score += 3
            print(f"{GREEN}Q3 to_list_inorder: 3/3{RESET}")
        else:
            if isinstance(inorder_list, list):
                total_score += 1
                print(f"{RED}Q3 to_list_inorder: 1/3 (list returned but incorrect order/values){RESET}")
            else:
                print(f"{RED}Q3 to_list_inorder: 0/3 (must return a list){RESET}")
    except Exception as e:
        print(f"{RED}Q3 to_list_inorder: 0/3 (exception: {e}){RESET}")

    print("\nTOTAL SCORE: {}/{}".format(total_score, max_score))


if __name__ == "__main__":
    print("This file is the grader. Run bst_student.py instead.")
