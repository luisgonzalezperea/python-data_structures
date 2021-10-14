# -*- coding: utf-8 -*-

########################### Queue (FIFO) implemented with simple linked lists.

class SNode:
    def __init__(self, elem, next= None):
        self.elem = elem
        self.next = next
        
class Queue:
    """ Head stores the first node. Tail stores the last node. The size 
    atribute counts the number of elements of the stack. It updates every 
    time an element is added (enqueue) or removed (dequeue). """
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        # Queue size.
        return self._size
    
    def isEmpty(self):
        # True if the queue is empty.
        # Another possibility: return len(self) == 0
        return self._head == None
       
    def __str__(self):
        # Returns a string with the elements of the queue.
        
        nodeIt = self._head
        result = ''
        
        while nodeIt:
            result += ',' + str(nodeIt.elem)
            nodeIt = nodeIt.next
    
        # I remove the first comma from the string.
        if len(result) > 0:   
            result = result[1:]
    
        return result     
    
    def enqueue(self,e):
        # Receive an element e, create a node and enqueue It.
        
        # I create a new node.
        newNode = SNode(e)

        # If there was no elements, queue has a new head.
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail.next = newNode

        self._tail=newNode
        self._size += 1

    def dequeue(self):
        # Returns the element stored in the head node.
        
        result = None
        
        if self.isEmpty():
            print('Error: Queue is empty!')
        else:
            # We save the value of the first element, to return It later.
            result=self._head.elem
            
            self._head=self._head.next
            if self.isEmpty():
                self._tail = None
            self._size -= 1
        
        return result 

    def front(self):
        # Returns the first element of the queue.
        
        result = None
        
        if self.isEmpty():
            print('Error: Queue is empty!')
        else:
            # We save the value of the first element.
            result = self._head.elem
        return result    

    def tail(self):
        # Returns the last element of the queue.
        
        result = None
        
        if self.isEmpty():
            print('Error: Queue is empty!')
        else:
            # We save the value of the last element.
            result = self._tail.elem
          
        return result 
  

################################################################### Tests

import random

s = Queue()
print("Queue: {}, lenght: {}".format(str(s),len(s)))

for i in range(5):
    x = random.randint(0,100)
    s.enqueue(x)
    print("After enqueue({}): {}, len: {}".format(x,str(s),len(s)))


print()
print("front:", s.front()) 
print("tail:", s.tail()) 
print()


print()
while not s.isEmpty():
    print("front of  {}: {}".format(str(s),s.dequeue())) 
    print("after pop: {}, len: {}".format(s,len(s)))
    print()