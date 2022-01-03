# -*- coding: utf-8 -*-

import queue

########################################################## Binary tree.


class Node:
    def __init__(self, elem, left = None, right = None, parent = None):
        self.elem = elem
        self.left = left
        self.right = right
        self.parent = parent
   
class BinaryTree():
    """ left = left child. right = right child. parent = parent node. The 
    size atribute counts the number of elements of the binary tree. It 
    updates every time an element is added or removed. """
    
    def __init__(self):
        self._root = None
   
    def size(self):
        # Binary tree size.
        
        return self._size(self._root)

    def _size(self, node):
        # Auxiliar recursive function which returns the size of a subtree.
        
        if not node: 
            return 0
        
        return 1 + self._size(node.left) + self._size(node.right)

    def height(self):
        # Binary tree height.
    
        return self._height(self._root)
    
    def _height(self, node):
        # Auxiliar recursive function which returns the height of a subtree.
        
        if not node:
            return -1

        return 1 + max(self._height(node.left), self._height(node.right))

    
    def depth(self,node):
        # Binary tree depth.

        if not node:
            return 0

        if not node.parent: 
            # Another possibility: node == self._root.
            return 0
        
        return 1 + self.depth(node.parent)

    def preorder(self):
        # Binary tree preorder path: (root, left, right).
        
        self._preorder(self._root)
        
    def _preorder(self, node):
        # Auxiliar recursive function which returns the preorder path of 
        # a subtree.

        if node:
            print(node.elem)
            self._preorder(node.left)
            self._preorder(node.right)

        
    def postorder(self):
        # Binary tree postorder path: (left, right, root).
        self._postorder(self._root)
        
    def _postorder(self, node):
        # Auxiliar recursive function which returns the postorder path of 
        # a subtree.
    
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem)
        
    def inorder(self):
        # Binary tree inorder path: (left, root, right).
        
        self._inorder(self._root)

    def _inorder(self,node):
        # Auxiliar recursive function which returns the inorder path of 
        # a subtree.
        
        if node:
            self._inorder(node.left)
            print(node.elem)
            self._inorder(node.right)
        
    def levelorder(self):
        # Binary tree levelorder path: prints nodes from left to right.

        if not self._root:
            print('Empty tree!')
        else:
            
            q = queue.Queue() # q = Queue()
            q.put(self._root) # q.enqueue(self._root)
            
            while not q.empty(): # while not self.isEmpty:
                current = q.get() # q.dequeue()
                print(current.elem)
                if current.left: # if the node has left child.
                    q.put(current.left) # q.enqueue(current.left)
                if current.right: # if the node has right child.
                    q.put(current.right) # q.enqueue(current.right)
                    
