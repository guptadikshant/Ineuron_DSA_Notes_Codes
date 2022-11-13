class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def preOrder(root):

    if root:
        print(f"{root.data} ",end='')
        preOrder(root.left)
        preOrder(root.right)


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    print(f"Preorder Traversal is : ")
    preOrder(root)
    