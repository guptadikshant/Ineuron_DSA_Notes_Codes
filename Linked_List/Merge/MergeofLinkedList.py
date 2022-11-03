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


    def printLinkedList(self):
        temp = self.head
        while temp:
            print(str(temp.data)+" ", end=" ")
            temp = temp.nextPtr



def mergeLists(head1, head2):

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.nextPtr = mergeLists(head1.nextPtr, head2)

    else:
        temp = head2
        temp.nextPtr = mergeLists(head1, head2.nextPtr)

    return temp

if __name__ == '__main__':
    llist1= LinkedList()
    llist2 = LinkedList()

    llist1.insertAtEnd(2)
    llist1.insertAtEnd(4)
    llist1.insertAtEnd(6)
    llist1.insertAtEnd(8)
    llist1.insertAtEnd(10)
    print("First Linked List : ")
    llist1.printLinkedList()
    
    llist2.insertAtEnd(1)
    llist2.insertAtEnd(3)
    llist2.insertAtEnd(5)
    llist2.insertAtEnd(7)
    llist2.insertAtEnd(9)
    print("\nSecond Linked List :")
    llist2.printLinkedList()

    llist3 = LinkedList()
    llist3.head = mergeLists(llist1.head, llist2.head)
    print("\nMerge Linked List :")
    llist3.printLinkedList()
    