# -*- coding: utf-8 -*-

###################################################### Double linked lists.

class DNode:
  def __init__(self, elem,next = None, prev = None ):
    self.elem = elem
    self.next = next
    self.prev = prev
    
class DList:
    """ Head stores the first node. Tail stores the last node. The size 
    atribute counts the number of elements of the linked list. It updates 
    every time an element is added or removed. """
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        # Stack size.
        return self._size
    
    def isEmpty(self):
        # True if the stack is empty.
        # Another possibility: return len(self) == 0
        return self._head == None

    def __str__(self):
        # Returns a string with the elements of the linked list.
        
        nodeIt = self._head
        result = '['
        
        while nodeIt:
            if type(nodeIt.elem) == int:
                result += str(nodeIt.elem) + ", "
            else:
                result += "'" + str(nodeIt.elem) + "', "
            nodeIt = nodeIt.next
        
        if len(result) >1:
            result = result[:-2]

        result += ']'
        return result

    def addFirst(self, e):
        # Adds a element at the first position

        # I create a new node.
        newNode = DNode(e)

        # I update the references of nodes.
        if self.isEmpty():
            self._tail = newNode
        else:
            newNode.next = self._head
            self._head.prev = newNode

        self._head = newNode
        # Increased linked list size.
        self._size += 1


    def addLast(self, e):
        # Adds a element at the last position and returns It.
        
        # I create a new node.
        newNode = DNode(e)

        # I update the references of nodes.
        if self.isEmpty():
            self._head = newNode
        else:

            newNode.prev = self._tail
            self._tail.next = newNode

        self._tail = newNode
        # Increased linked list size.
        self._size += 1

    def removeFirst(self):
        # Removes a element at the first position.
        
        result = None
        if self.isEmpty():
            print('Error: linked list is empty!')
        else:
            # I save the elements before removing It.
            result = self._head.elem
            
            # I update the references of nodes.
            
            self._head = self._head.next
            if not self._head:
                self._tail = None
            else:
                self._head.prev = None

            # Decreased linked list size.
            self._size -= 1

        return result

    def removeLast(self):
        # Removes a element at the last position and returns It.

        result = None
        if self.isEmpty():
            print('Error: linked list is empty!')

        else:
            # I save the elements before removing It.       
            result = self._tail.elem

            # I update the references of nodes.
            self._tail = self._tail.prev
               
            if not self._tail:
                self._head = None
            else:
                self._tail.next = None

            # Decreased linked list size.
            self._size -= 1

        return result
 
    def getAt(self, index):
        # Returns the element of index position. If index is not valid, It
        # returns None
        
        result = None
        
        # I check the range of elements.
        if index not in range(0, len(self)): 
            print(index,'Error: out of index')    
        else:
             
            # I update the references of nodes.
            nodeIt = self._head
            i = 0
            while nodeIt and i < index:
                nodeIt = nodeIt.next
                i += 1
                
            # The element was found.    
            result = nodeIt.elem

        return result


    def index(self, e):
        # Returns the first index of element. If e is not in the list
        # It returns -1.
           
        nodeIt = self._head
        index = 0     
        while nodeIt:
            if nodeIt.elem == e:
                return index
            nodeIt = nodeIt.next
            index += 1
            
        return -1

    def insertAt(self,index,e):
        # Add a element at the index position.
       
        # I check the range of elements.
        if index not in range(0, len(self) + 1): 
            print('Error: out of index')
    
        # addFirst adds nodes at the first position.
        elif index == 0:
            self.addFirst(e)
            
        # addLast adds nodes at the last position.
        elif index == len(self):
            self.addLast(e)
        
         # I update the references of nodes.
        else:
            nodeIt = self._head
            for i in range(index):
                nodeIt = nodeIt.next
            previous = nodeIt.prev
            # I create a new node.
            newNode = DNode(e)
            newNode.next = nodeIt
            newNode.prev = previous
            previous.next = newNode
            nodeIt.prev = newNode
            
            # Increased linked list size.
            self._size += 1

    def removeAt(self, index):
        # Removes a element at the index position and returns It.
        
        result = None
        
        # I check the range of elements.
        if index not in range(0, len(self) + 1): 
            print('Error: out of index')

        # removeFirst removes nodes at the first position.
        elif index == 0:
            result = self.removeFirst()
        
        # removeLast removes nodes at the last position.            
        elif index == len(self) -1:
            result = self.removeLast()
            
        # I update the references of nodes.
        else:
            nodeIt = self._head
            for i in range(index):
                nodeIt = nodeIt.next
            # I save the elements before removing It.      
            result = nodeIt.elem
            prevNode = nodeIt.prev
            nextNode = nodeIt.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            
            # Decreased linked list size.
            self._size -= 1

        return result

################################################################### Tests
if __name__=='__main__':
    import random
    l = DList()
    for i in range(5):
        l.addLast(random.randint(-5, 5))

    print('Content of l:', l)
    print('len(l):', len(l))
    print()

    while not l.isEmpty():
        print('after removeFirst()={}, l={}, len={}'.format(l.removeFirst(), l, len(l)))

    for i in range(3):
        x = random.randint(-5, 5)
        l.addFirst(x)
        print('after addFirst({}), l={}, len={}'.format(x, l, len(l)))

    print('Content of l:', l)
    print('len(l):', len(l))
    print()

    while not l.isEmpty():
        print('after removeLast()={}, l={}, len={}'.format(l.removeLast(), l, len(l)))
    
    print('---------------------')
    
    for i in range(3):
        x = random.randint(-5, 5)
        l.addFirst(x)
        l.addLast(x)

    print('Content of l:', l)
    print('len(l):', len(l))
    print()

    for i in range(len(l)):
        print(' getAt({})={}'.format(i, l.getAt(i)))
    print()

    for i in range(3):
        x=random.randint(-5,5)
        print(' index({})={}'.format(x, l.index(x)))
    print()

    print('Content of l:', l)
    print('len(l):', len(l))
    print()

    x = 414
    l.insertAt(0,x)
    print(' insertAt(0,{}), l={}, len={}'.format(x, l, len(l)))
    l.insertAt(len(l),x)
    print(' insertAt(len(l),{}), l={}, len={}'.format(x, l, len(l)))
    l.insertAt(len(l)//2,x)
    print(' insertAt(len(l)//2,{}), l={}, len={}'.format(x, l, len(l)))
    print()
    print()


    print(' removeAt(0)={}, l={}, len={}'.format(l.removeAt(0),l, len(l)))
    print(' removeAt(len(l)-1)={}, l={}, len={}'.format(l.removeAt(len(l)-1), l, len(l)))
    print(' removeAt(len(l)//2+1)={}, l={}, len={}'.format(l.removeAt(len(l)//2+1), l, len(l)))