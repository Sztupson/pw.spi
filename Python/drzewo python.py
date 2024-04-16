# tree = [1,2,3,4,5,6,7]

# def get_left_child(index):
#     return 2 * index + 1
# def get_right_child(index):
#     return 2 * index + 2
# def get_parent(index):
#     return (index - 1) // 2

# index = 0 # korzeń drzewa 
# left_child_index = get_left_child(index)
# right_child_index = get_right_child(index)

# print(f"Wartość korzenia: {tree[index]}")
# print(f"Lewe dziecko korzenia: {tree[left_child_index]}")
# print(f"Prawe dziecko korzenia: {tree[right_child_index]}")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_preorder(node):
    if node:
        print(node.value)
        dfs_preorder(node.left)
        dfs_preorder(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Przeszukiwanie w glasb (DFS) - pre order: ")
dfs_preorder(root)