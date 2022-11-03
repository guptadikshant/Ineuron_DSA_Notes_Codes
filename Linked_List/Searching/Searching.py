class Node:

    def __init__(self, data):
        self.data = data
        self.nextPtr = None

class LinkedList:

    def __init__(self):
        self.head = None

    ## insert the new node at the end of the linked list
    def insertAtEnd(self, new_data):
        ## create a new node for the new data
        new_node = Node(new_data)

        ## check whether linked list is empty or different
        if self.head is None:
            self.head = new_node
            return
        
        ## insert the data at the end
        temp = self.head
        while temp.nextPtr:
            temp = temp.nextPtr
    
        temp.nextPtr = new_node

    def searchNode(self,newData):

        temp = self.head
        while temp:
            if temp.data == newData:
                return True
            temp = temp.nextPtr
        return False

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ", end=" ")
            temp = temp.nextPtr


if __name__ == '__main__':
    llist = LinkedList()

    llist.insertAtEnd(10)
    llist.insertAtEnd(20)
    llist.insertAtEnd(30)
    llist.insertAtEnd(40)
    llist.insertAtEnd(50)
    print("Insertion of nodes at the end of the Linked List:")
    llist.printLinkedList()
    print()

    # Searching inside the Linked List
    givenNode = 75
    search_of_node = llist.searchNode(givenNode)
    print(f"Given node {givenNode} present inside Linked List : {search_of_node}")
