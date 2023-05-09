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
    
    ##Binary Search Iterativa
    def find_i(BinaryTree, target): #Iniciating the function which takes the tree and the target as arguments
        cur_node = BinaryTree.root  #The root is set as a current node
        while cur_node != None: #While loop goes over the tree if there is any
            if cur_node.data == target: ##If the target is in the current node 
                return True
            elif cur_node.data >  target: ##If the target value is less than the current node value move left
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right ##If the target is higher move to the right node
        return False

    ##Binary Search Recursive
    def find_r(BinaryTree, target): #Iniciating the function which takes the tree and the target as arguments
        if BinaryTree.root:
            if BinaryTree._find_r(target, BinaryTree.root): ##This function returns true only if the target has been found in the tree
                return True
            return False
        else:
            return None

    def _find_r(BinaryTree, target, cur_node):
        if target > cur_node.data and cur_node.right: ##If the target value is higher than the current node value and we are on the right node
            return BinaryTree._find_r(target, cur_node.right) ##It returns the current node to the previous function
        elif target < cur_node.data and cur_node.left: ##If the target is less than the node value and it on the left side
            return BinaryTree._find_r(target, cur_node.left) ##Returns the current node to the first function
        if target == cur_node.data: ##This case is for when the target value matches the current node
            return True
