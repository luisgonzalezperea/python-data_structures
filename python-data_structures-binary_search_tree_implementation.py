# -*- coding: utf-8 -*-

from binarytree import BinaryTree
from binarytree import Node

###################################################### Binary search tree.

class BSTNode(Node):
    
    def __init__(self, key, elem, left = None, right = None, parent = None):
        
        # key lets us count the position of the tree.
        self.key=key
        
        super(BSTNode,self).__init__(elem, left, right, parent)

    def __eq__(self,other):
        
        return (other != None and self.key == other.key  and 
                self.left == other.left and self.right == other.right)

class BinarySearchTree(BinaryTree):
    
    def __eq__(self,other):
        # Function equal.
        return other != None and self._root == other._root
  
    def search(self, key):
        # Returns true if the node exists.
        
        return self._searchNode(self._root, key)

    def _searchNode(self, node, key):
        # Auxiliar recursive function.
        
        if not node:
            return False

        if node.key==key:
            return True

        if key < node.key:
            return self._searchNode(node.left, key)

        if key > node.key:
            return self._searchNode(node.right, key)

    def find(self,key):
        # Returns the node if the node exists.
        
        return self._find(self._root, key)

    def _find(self, node, key):
        # Auxiliar recursive function.
        
        if not node:
            return None

        if node.key == key:
            return node

        if key < node.key:
            return self._find(node.left, key)
        
        if key > node.key:
            return self._find(node.right, key)
        
    def insert(self, key, elem):
        # Inser a new node with the key and the element that passes 
        # by parameter
        
        # If the tree is empty, the new node is the root.
        if not self._root:
            self._root = BSTNode(key, elem)
            
        else:
            self._insertNode(self._root, key, elem)

    def _insertNode(self, node, key, elem):
        # Auxiliar recursive function.
        
        # If the node already exists.
        if node.key == key:
            print('Error')
         
        else:
            if key < node.key:

                if not node.left:
                    newNode = BSTNode(key, elem)
                    newNode.parent = node
                    node.left = newNode
                else:
                    self._insertNode(node.left, key, elem)

            else: #key > node.key
    
                if not node.right:
                    newNode=BSTNode(key, elem)
                    newNode.parent = node
                    node.right = newNode
                else:
                    self._insertNode(node.right, key, elem)

    def _numChildren(self, node):
        # Returns the number of sons that the node has.
        
        if not node or (not node.left and not node.right):
            return 0
        
        if node.left and node.right:
            return 2
        
        # If you do not meet the above conditions, it is because node 
        # only has one child.
        return 1

    def remove(self,key):
        # Removes a node.
        
        # If the node does not exist, returns None
        node = self.find(key)
        if not self.find(key):
            print('Error')
            return None
        
        node = self._removeNode(node)
  
    def _removeNode(self, node):    
        # Auxiliar recursive function. The possibilities:
        # 1) The node to delete is a leaf.
        # 2) The node to delete has only one subtree.
        # 3) The node to delete has two subtrees.
        
        #1) 
        if self._numChildren(node) == 0:
            
            if not node.parent: #if node = self._root:
                self._root = None 
            else:
                if node == node.parent.left: 
                    node.parent.left = None
                elif node == node.parent.right: 
                    node.parent.right = None  
                    
                node.parent = None
                return None
            
        #2)
        elif self._numChildren(node) == 1:

            grandP = node.parent
            
            if node.left:
                grandC = node.left   
            elif node.right:
                grandC = node.right
                
            if not grandP:
                self._root = grandC
            
            elif node == grandP.left:
                grandP.left = grandC
            elif node == grandP.right: 
                grandP.right=grandC
            
            grandC.parent=grandP            
            return grandC
        
        #3)
        else:

            successor = node.right
            while successor.left != None:
                successor = successor.left
                        
            node.key = successor.key
            node.elem = successor.elem

            return self._removeNode(successor)
        
    def draw(self, extend=True):
        # Draws the tree.
        if self._root:
            self._draw('', self._root, False, extend)
        else:
            print('Empty tree.')
        print('\n\n')
        
    def _draw(self, prefix, node, isLeft ,extend):
        # Auxiliar recursive function.
        
        if node !=None:
            self._draw(prefix + "     ", node.right, False, extend)
            
            #Puedes reemplazar elem por key.
            if extend:
                print(prefix + ("|-- ") + 'key:'+str(node.key) +'\telem:('+ str(node.elem)+')')
            else:
                print(prefix + ("|-- ") + str(node.key))
                
            self._draw(prefix + "     ", node.left, True, extend)
            
    def fe_size(self, key):
        # returns the balance factor in size of the tree.
        # fe = |size(node.left)-size(node.right)|
        
        node = self.find(key)
        return self._fe_size(node)

    def _fe_size(self, node):
        # returns the balance factor in size of a subtree.
        
        if not node:
            return 0
        else:
            return abs(self._size(node.left)-self._size(node.right))
        
    def fe_height(self, key):
        # returns the balance factor of the tree.
        # fe = |height(node.left)-height(node.right)|
        
        node = self.find(key)
        return self._fe_height(node)

    def _fe_height(self, node):
        # returns the balance factor of a subtree.
        
        if not node:
            return 0
        else:
            return abs(self._height(node.left)-self._height(node.right))

    def isSizeBalanced(self):
        # Returns true if the tree is size balanced.    
        
        return self._isSizeBalanced(self._root)

    def _isSizeBalanced(self,node):
        # Auxiliar recursive function.
        
        if not node:
            return True
        if self._fe_size(node) > 1:
            return False
        return (self._isSizeBalanced(node.left) and 
                self._isSizeBalanced(node.right))
        
    def isHeightBalanced(self):
        # Returns true if the tree is height balanced.  
        
        return self._isHeightBalanced(self._root)

    def _isHeightBalanced(self,node):
        # Auxiliar recursive function."
        
        if not node:
            return True
        if self._fe_height(node) > 1:
            return False
        return (self._isSizeHeight(node.left) and 
                self._isHeightBalanced(node.right))
        
########################################################## Tests

if __name__=="__main__":
    
	tree=BinarySearchTree()

	for x in [18,11,23,5,15,20,24,9,15,22,21,6,8,7]:
	    tree.insert(x,x)
	print()

	tree.draw()
	print('tamaño:',tree.size())
	print('altura:',tree.height())

	# Removing the root.
	tree.remove(18)
	tree.draw(False)

	# Removing a leaf.
	tree.remove(7)
	tree.draw(False)

	# Removing a leaf which does not exists.
	tree.remove(8)
	tree.draw(False)

    # Removing node that only has left child.
	tree.remove(5)
	tree.draw(False)

	# Removing node that only has right child.
	tree.remove(9)
	tree.draw(False)

	# Removing node that has both children.
	tree.remove(11)
	tree.draw()