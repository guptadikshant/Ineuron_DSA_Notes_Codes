class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def inOrder(root):

    if root:
        inOrder(root.left)
        print(f"{root.data} ",end=" ")
        inOrder(root.right)


if __name__ == "__main__":
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(f"Inorder Traversal is : ")
    inOrder(root)