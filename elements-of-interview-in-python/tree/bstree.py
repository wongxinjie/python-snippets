class BSTNode:

    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def search_bst(tree, key):
    if tree is None or tree.data == key:
        return tree

    if key < tree.data:
        search_bst(tree.left, key)
    else:
        search_bst(tree.right, key)


def is_binary_tree_bst1(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False

    return (is_binary_tree_bst1(tree.left, low_range, tree.data) and
            is_binary_tree_bst1(tree.right, tree.data, high_range))


prev = None


def is_bst(tree):
    global prev

    if not tree:
        return True

    if prev is not None and tree.data < prev.data:
        return False

    prev = tree
    return is_bst(tree.right)


root = BSTNode(3)
root.left = BSTNode(2)
root.right = BSTNode(1)

print(is_bst(root))
