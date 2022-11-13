class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def postOrder(root):

    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(f"{root.data} ",end='')


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(f"Postorder Traversal is : ")
    postOrder(root)