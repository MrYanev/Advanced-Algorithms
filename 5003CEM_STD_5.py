class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
            
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode

    def Insert(self, val_before,newdata):
        if val_before is None:
            print("No node to insert after")
            return
        else:
            NewNode = Node(newdata) #Creating a new node and storing the data in it
            NewNode.nextval = val_before.nextval    #Updates val_before to be the following element after the new one
            val_before.nextval = NewNode    #The new elemet becomes the element after val_before     

        

list = SLinkedList()
list.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

list.AtEnd("Sun")

list.Insert(list.headval.nextval ,"Wed")

list.listprint()