# -*- coding: utf-8 -*-

################################ Stack (LIFO) implemented with linked lists.

class SNode:
    def __init__(self, elem, next= None):
        self.elem = elem
        self.next = next


class Stack:
    """ Head stores the first node. The size atribute counts the number of 
    elements of the stack. It updates every time an element is added (push) 
    or removed (pop). """
    
    def __init__(self):
        self._head = None
        self._size = 0
  
    def __len__(self):
        # Stack size.
        return self._size
  
    def isEmpty(self):
        # True if the stack is empty.
        # Another possibility: return len(self) == 0
        return self._head == None
    
    def __str__(self):
        # Returns a string with the elements of the stack.
        
        nodeIt = self._head
        result = ''
        
        while nodeIt:
            result += ',' + str(nodeIt.elem)
            nodeIt = nodeIt.next
    
        # I remove the first comma from the string.
        if len(result) > 0:   
            result = result[1:]
    
        return result    
  
    def push(self, e):
        # Receive an element e, create a node and place it before head.
        
        # I create a new node.
        newNode = SNode(e)
        # newNode points to head.
        newNode.next = self._head
        # newNode is the new head.
        self._head = newNode
        # Increased stack size.
        self._size = self._size + 1
  
    def pop(self):
        # Returns the element stored in the head node.
    
        result = None
        
        if self.isEmpty():
          print('Error: Empty stack!')
          
        else:  
            # I store the value of head before removing it.
            result = self._head.elem
            # The new head is...
            self._head = self._head.next
            # Decreased stack size.
            self._size -= 1
            
        return result
      
    def top(self):
        # Returns the top of the stack.
        
        result = None
        
        if self.isEmpty():
            print('Error: Empty stack!')
        else:  
            result = self._head.elem
            
        return result
  


################################################################### Tests

import random

s=Stack()
print("Stack:{}, Stack lenght = {}".format(str(s),len(s)))

for i in range(5):
    x = random.randint(0,100)
    s.push(random.randint(0,100))
    print("After push({}): {}, len: {}".format(x,str(s),len(s)))
    
for i in range(5):
    s.pop()
    print("After pop: {}, len: {}".format(str(s),len(s)))