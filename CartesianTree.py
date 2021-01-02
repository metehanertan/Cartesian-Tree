# Melisa DÖNMEZ - 150116030
# Metehan ERTAN - 150117051

# Object to keep the properties of the tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.index = 0
        self.inherited = None
        self.left_smallest = None
        self.right_smallest = None


# create cartesian tree
def create_tree(tree):
    if len(tree) == 0:
        return None
    Min = min(tree)
    i = tree.index(Min)
    root = Node(Min)
    root.left = create_tree(tree[: i])
    root.right = create_tree(tree[i + 1:])
    return root


# print tree(to see whether tree created correctly
def print_tree(node, level):
    if node is not None:
        print(' ' * 4 * level + '->', node.val, node.inherited)
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)


# Traverse the tree object and find each node's index by comparing with the input array
def find_index(node, arr):
    k = 0
    if node is not None:
        while k < arr.__len__():
            if node.val == arr[k]:
                node.index = k + 1
            k = k + 1
        find_index(node.left, arr)
        find_index(node.right, arr)


def find_smallest(node, l_r):
    if node is not None:
        inher = node.inherited
        # find left smallest
        if l_r == "left":
            if node.left is not None:
                node.left.inherited = inher  # node.inhereted to inheredted variable of its left child
                find_smallest(node.left, l_r)
            if node.right is not None:
                node.right.inherited = node.index  # node.index to inhereted var,able of its right child
                find_smallest(node.right, l_r)
        # find right smallest
        elif l_r == "right":
            if node.left is not None:
                node.left.inherited = node.index
                find_smallest(node.left, l_r)
            if node.right is not None:
                node.right.inherited = inher
                find_smallest(node.right, l_r)


def create_smallest(node, arr, l_r):
    if node is not None:
        if node.inherited is not None:  # if node.inhereted != null
            if l_r == "left":
                node.left_smallest = arr[
                    node.inherited - 1]  # node.inhereted-1 denotes the index of the node's nearest smaller neighbor on the left
            elif l_r == "right":
                node.right_smallest = arr[
                    node.inherited - 1]  # node.inhereted-1 denotes the index of the node's nearest smaller neighbor on the rigth
        else:
            if l_r == "left":
                node.left_smallest = "-"  # It does not have smaller neighbor on the left
            elif l_r == "right":
                node.right_smallest = "-"  # It does not have smaller neighbor on the right
        create_smallest(node.left, arr, l_r)
        create_smallest(node.right, arr, l_r)


# Tree inorder traversal
def inorder_traversal(root, l_r):
    res = []
    if root:
        res = inorder_traversal(root.left, l_r)
        if l_r == "left":
            res.append(root.left_smallest)
        elif l_r == "right":
            res.append(root.right_smallest)
        res = res + inorder_traversal(root.right, l_r)
    return res


# read input txt file
with open("input.txt") as f:
    for line in f:
        int_list = [int(x) for x in line.strip().split(",")]

tree = create_tree(int_list)
find_index(tree, int_list)

left_smallest = []
right_smallest = []
# left smallest
find_smallest(tree, "left")
create_smallest(tree, int_list, "left")
left_smallest = inorder_traversal(tree, "left")
print("nearest left smaller values:", left_smallest)
# right smallest
find_smallest(tree, "right")
create_smallest(tree, int_list, "right")
right_smallest = inorder_traversal(tree, "right")
print("nearest right smaller values:", right_smallest)
