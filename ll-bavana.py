 def printList(self):
        temp_node = self.head
        while (temp_node):
            print(str(temp_node.item) + "--> ", end="")
            temp_node = temp_node.next

if __name__ == '__main__':


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
            data=int(input("enter position:"))
            llist.deleteNode(data)
        elif ind==4:
            llist.printList()
        elif ind==5:
            status=False

