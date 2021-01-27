# Linked list operations in Python


# Create a node
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node



    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node
        
    #Inserting node at specific position
    def insertInbtw(self,data,p):
        new_node=Node(data) 
        c=1
        temp_node=self.head
        while(c!=p):
            pre_node=temp_node
            temp_node=temp_node.next
            c=c+1
        pre_node.next=new_node
        new_node.next=temp_node

    # Deleting a node
    def deleteNode(self, position):

        if self.head == None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp_node = temp_node.next
            if temp_node is None:
                break

        # If the key is not present
        if temp_node is None:
            return

        if temp_node.next is None:
            return

        next = temp_node.next.next
        temp_node.next = None
        temp_node.next = next
#--------------------------------------------------------------------------------------------------------------------end of abdul
    def printList(self):
        temp_node = self.head
        while (temp_node):
            print(str(temp_node.item) + "--> ", end="")
            temp_node = temp_node.next
​
​
if __name__ == '__main__':
​
​
​
​
    llist = LinkedList()
    status=True
    while(status):
        print("\nChoose from the options by entering index:\n1.Insert at beginning\n2.Insert at end\n3.delete a node\n4.Traverse\n5.exit")
        print("---------------------------------------------------------------------------------------")
        ind=int(input("enter the index :"))
        if ind==1:
            data=input("enter data:")
            llist.insertAtBeginning(data)
        elif ind==2:
            data=input("enter data:")
            llist.insertAtEnd(data)
        elif ind==3:
            data=input("enter data:")
            p=int(input("enter postion:"))
            llist.insertInbtw(data,p)
        elif ind==4:
            data=int(input("enter position:"))
            llist.deleteNode(data)
        elif ind==5:
            llist.printList()
        elif ind==6:
            status=False
