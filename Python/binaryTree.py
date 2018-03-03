import math
import sys
#import pyodbc
import datetime

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        #print('data=', data)
        if self.root == None:
            #print('    self.root == None')
            self.root = Node(data)
        elif root == None:
            #print('    root == None')
            root = Node(data)
        else:
            if data <= root.data:
                #print('    data <= root.data')
                root.left = self.insert(root.left, data)                
            elif data > root.data:
                #print('    data > root.data')
                root.right = self.insert(root.right, data)
        return root

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
        
    def findNode(self, node, val):
        if node is None:
            return False
        elif val == node.data:
            return True
        elif val < node.data:
            return self.findNode(node.left, val)
        else:
            return self.findNode(node.right, val)        
        
# Define a main() function 
def main():
    tree = Tree()

    tree.insert(tree.root, 8)
    tree.insert(tree.root, 3)
    tree.insert(tree.root, 10)
    tree.insert(tree.root, 1)
    tree.insert(tree.root, 6)
    tree.insert(tree.root, 4)
    tree.insert(tree.root, 7)
    tree.insert(tree.root, 14)
    tree.insert(tree.root, 13)
    tree.inorder(tree.root)
    
    findVal = tree.findNode(tree.root, 5)
    print('5', findVal)
    
    findVal = tree.findNode(tree.root, 6)
    print('6', findVal)
        
    
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
