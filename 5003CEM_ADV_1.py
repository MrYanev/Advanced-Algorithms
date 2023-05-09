""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 5. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 5 (available in Week 5).

    There will be some ***introductory challenges*** in Week 4, with solutions released in Week 5.
    It is STRONGLY RECOMMENDED you attempt these!

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the Week 5 lab sheet guidance). 
"""

#from curses.ascii import TAB
import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    """ ADVANCED TASK 1 CODE STARTS HERE"""

    def removeNode(self, target):
        parent = None
        if self.root is None:   #If no tree
            return None
        elif self.root.data == target:  #If the root is the target
            if self.root.left is None and self.root.right is None:  #If both left and right branches are None
                self.root = None    #Assign None to the root
            elif self.root.left and self.root.right is None:    #If the right branch is None
                self.root = self.root.left  #Assign left branch to the root
            elif self.root.left is None and self.root.right:    #If the left brant is None
                self.root = self.root.right #Assign right branch to the root
            elif self.root.left and self.root.right:    #If both are present
                removeParent = self.root #Initiate removeParent and assign the root to it
                removeNode = self.root.right    #Initiate removeNode and assign right root to it
                while removeNode.left:  #While there is nodes to the left
                    removeParent = removeNode   #Remove the value
                    removeNode = removeNode.left    #Change the possition

                self.root.data = removeNode.data    
                if removeNode.right:    #This section is to determine whether to be on the left or the right branch
                    if removeParent.data > removeNode.data: #If the parent data is greater to the Node data
                        removeParent.left = removeNode.right    #Node goes to the right
                    elif removeParent.data < removeNode:    #If the parent data is less than the Node data
                        removeParent.right = removeNode.right   #Node goes to the right
                else:
                    if removeNode.data < removeParent.data: #If the Node data is less than the parent data 
                        removeParent.left = None    #Remove parent left
                    else:   
                        removeParent.right = None   #Remoce parent right
        parent = None   #Initiate parent and assign to None 
        node = self.root    #Initiate node and assign the root to it

        while node and node.data != target: #While loop to run until there are nodes different than the target node
            parent = node   #Node assigned to parent
            if target < node.data:  #If target value is less than node value
                node = node.left    #Goes to the left
            elif target > node.data:    #If target value is greater than node value
                node = node.right   #Goes to the right
        
        if node is None or node.data != target: #If there is no nodes or node data is not eaqual to targer
            return False

        elif node.left is None and node.right is None:  #If there aren't left and right nodes
            if target < parent.data:    #If target value is less than the parent value
                parent.left = None  #Parent left to be removed
            else:   #If the target value is greater than the parent value
                parent.right = None #Parent right to be removed
            return True

        elif node.left and node.right is None:  #If there is left node but no right node
            if target < parent.data:    #If parent data is greater than target value 
              parent.left = node.left   #Assing node value to left parent
            else:   #If parent data is less than the target 
                parent.right = node.left    #Right parent to take left node value
            return True

        elif node.left is None and node.right:  #If there is only right node
            if target < parent.data:    #If target value is less than the parent value
              parent.left = node.right #Left parent to take left node value
            else:   #If target value is greater than the parent value
                parent.right = node.right   #Right parent to right node value
            return True

        else:   #Last case if there are both left and right node
            removeParent = node #Initiating removeParent and assigning the node value to it
            removeNode = node.right #Initiating removeNode and assigning right node value to it
            while removeNode.left:  #While there are node on the right side
                removeParent = removeNode   
                removeNode = removeNode.left

            node.data = removeNode.data 
            if removeNode.right:    #If there is a node to the right to be removed
                if removeParent.data > removeNode.data: 
                    removeParent.left = removeNode.right
                elif removeParent.data < removeNode:
                    removeParent.right = removeNode.right
            else:
                if removeNode.data < removeParent.data:
                    removeParent.left = None
                else:
                    removeParent.right = None   
 

#example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)

bst.display(bst.root)





