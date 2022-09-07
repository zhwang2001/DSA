#data structure implementation

class queue:
    default_length = 10
    
    def __init__(self, k):
        self.data = [None]*queue.default_length
        self.first = 0
        self.size = 0
        self.item = k

    def isempty(self):
        if len(self.size) == 0:
            return True
        return False

    def isfull(self):
        if len(self.data) == 0.75*queue.default_length:
            return True
        return False
        
    def front(self):
        """index front and change"""
        (self.first + 1) % len(self.data)
        self.data[self.first] = None
        return self.data

    def rear(self):
        """index rear and add"""
        rear = (self.first + self.size) % len(self.data)
        self.data[rear] = self.item
        return self.date


    def enqueue(self):
        """if size of array is full then double size
            every enqueue increase front by 1
            increase size by 1
        """

        if self.isfull():
            self.resize("up")
        self.front()
        self.size += 1

    def dequeue(self):
       """ add an item to the end of queue
        if empty resize to 1/4 the original size
        else increase :size by 1"""
       if self.isempty():
            self.resize("down")
       self.rear()
       self.size -= 1

    def resize(self, scale = str): 
        old_array = self.data
        if scale == 'up':
            self.data = [None] * 2
            walk = self.front # we use walk to index the first item in old_array, if we didn't use walk we might index None
            for item in range(self.size):
                old_array[item] = self.data[walk]
            self.front = 0 #(new array front set at 0)
        else:
            self.data = [None] * 0.25
        
#singly linked list implementation
class Node:
     def __init__(self, data):
          self.data = data
          self.next = next
class singlylinkedList:
     def __init__(self):
          """
          #has a head and a tail pointer
          #Node stores data and memory address of next node
          #traverse linked list
          #insert and delete anywhere in list
          #get head and tail
          """
          self.tail = None
          self.head = None
          self.size = 0

     def front(self):
          return self.head

     def rear(self):
          return self.tail

     def getindex(self, ind):
          indexed_result = self.traverse(ind, False).data
      
     def insertindex(self, data, ind):
          self.size += 1
          newnode = Node(data)
          if self.isempty():
              self.head, self.tail = newnode
          prevnode = self.traverse(ind - 1, False)
          newnode = newnode
          curnode = self.traverse(ind, False)

          prevnode.next = newnode#previous node connects to newnode
          newnode.next = curnode#newnode connects to oldnode
        

     def setindex(self, data, ind):
          if self.isempty():
              print('linked list has no nodes')    
          self.traverse(ind , False).data = data #change the internode's data with new data at index


     def delindex(self, ind: int):
          self.size -= 1
          if self.isempty():
              print('Linked List is empty')
          if ind == 0:
              self.head = self.head.next
          elif ind == self.__len__():
              self.tail = self.traverse(ind - 1, False)

          self.pointer = self.traverse(ind -1, False)#up until but not including the index, returns node at index
          self.nextindex = self.traverse(ind).next
          self.pointer.next = self.nextindex


     def prepend(self, data):#equivalent to enqueue
          self.size += 1
          newnode = Node(data)
          if self.__len__() == 1:
              self.head, self.tail = newnode
          oldhead = self.head
          self.head = newnode #taking properties from newnode
          self.head.next = oldhead
              

     def append(self, data):#add to rear
          self.size += 1
          newnode = Node(data)
          if self.__len__() == 1:
              self.head, self.tail = newnode
           
          oldtail = self.tail#implement an old tail
          oldtail.next = newnode #the next item in the old tail is newnode
          self.tail = newnode #the tail is now the new node 
          
     def __len__(self):
          return self.size
      
     def isempty(self):
          if self.size == 0 or self.head == None:
              return True
          return False


      
     def traverse(self, ind, display: True):
          """
          display  = show entire linked list
          """
          self.display = display
          if self.isempty():
              print("linked list has no nodes")
          internode = self.head
          if self.display == True:
              while self.head != None:
                  print(internode.data, '->', end = ' ')
          for i in range(ind + 1):
              internode = internode.next 
          print(f'{internode.data} at index{ind}')
          return internode



#Doubly Linked list implementation
class Node:
    def __init__(self, data, next, prev):
        #contains an extra pointer (self.pointer)
        #each node now uses 12 bytes
        #use of sentinnels to simplify special boundary conditions
        self.data = data
        self.next = next
        self.prev = prev

class doublylinkedList(Node):
    def __init__(self):
        """
        insertion, deltion, indexing properties O(1)
        at beginning, end = O(1)
        at ith element = O(n)
        """
        self.header = Node(data = None, next = None, prev = None) 
        self.trailer = Node(data = None, next = None, prev = None) 
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
    
    def _isempty(self):
        if self.size == 0:
            return True
        return False
    def __len__(self):
        return self.size

    def _traverse(self, ind, direction:'forward'):
        """
        Traverse up to a certain index or display entire linked list
        """
        if self._isempty():
            print('the linked list is empty')
        header_internode = self.header #internode starts at header
        trailer_internode = self.trailer #internode starts at trailer

        if direction == 'backward': #backwards traversal
            for i in range(self.__len__() - ind + 1): #traversing list backwards
                trailer_internode = trailer_internode.prev
            return trailer_internode
        
        else:
            for i in range(ind + 1): #forwards traversal
                header_internode = header_internode.next
            return header_internode 

    def display(self):
        """
        prints out entire linked list and your position within the list
        """
        print('display has started')
        if self._isempty():
            print('the linked list is empty')
        internode = self.header.next
        n = 0
        while internode.data != self.trailer.data:#while internode != None
            print(f'{internode.data} ->', end = ' ')
            n += 1
            internode = internode.next
        print(f'\nYou are number {n} in line, there are {n - 1} people in front')

    def modify(self, ind, data):
        """
        replaces the data at a certain index with another piece of data
        """
        self._djikstra(ind = ind).data = data
        print(f'modification: {data}, completed at {ind} index')

    def insert(self, data, ind = 0):
        """ 
        #4 connections in total
        ##oldnode.prev = newnode
        ##newnode.prev = previous
        ##newnode.next = oldnode
        ##previous.next = newnode
        """
        self.size += 1
        #instantiation of variables
        oldnode = self._djikstra(ind = ind)
        previousnode = oldnode.prev #oldnode's previous node is also newnode's previous node
        nextnode = oldnode #old becomes next

        #insertion of newnode in place of old node and connecting links
        newnode = Node(data, nextnode, previousnode)
        previousnode.next = newnode
        nextnode.prev = newnode
    
    def delete(self, ind):
        self.size -= 1
        if self._djikstra(ind = ind).data == None:
            raise IndexError('Index is out of range')
        previousnode = self._djikstra(ind = ind).prev
        nextnode = self._djikstra(ind = ind).next
        previousnode.next = nextnode
        nextnode.prev = previousnode
     

    
    def _djikstra(self, ind):
        """
        determines whether or not to traverse the list from rear
        or from front
        """
        if ind <= (self.size // 2) + 1:
            return self._traverse(ind, 'forward')
        elif ind > (self.size // 2) + 1:
            return self._traverse(ind, 'backward')

#ignore
class Tree:
    def __init__(self, val = None):
        if val != None:
            self.val = val
        else:
            self.val = None
            self.left = None
            self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.insert(val)

            elif val > self.val:
                if self.right is None:
                    self.right = Tree(val)

                else:
                    self.right.insert(val)

        else:
            self.val = val

    def printValues(self):
        if self.left:
            self.left.printValues()

        print(self.val)
        if self.right:
            self.right.printValues()

if __name__ == "__main__":

    tree = Tree(20)
    tree.left = Tree(18)
    tree.right = Tree(23)
    tree.insert(19)
    tree.insert(24)
    tree.insert(21)

    tree.printValues()

#Binary tree implmentation
class treeNode:

    def __init__(self, val = None):
        self.val = data
        self.right = None
        self.left = None
        

class binaryTree(treeNode):

    def __init__(self, val):
        """
        #For ordered trees (numbers only), improper implementation, Non recursive Traversal
            index(replace or display) (implement recursively)
        children
        siblings
        _insert new node
            remove node
        merge (2 trees)
        Traversal algorith(hard)
        """
        if val == None:
            self.root, self.tracker = treeNode(val)
        self.val = val 
        self.degree = 0 #degree of tree
        self.depth = 0
        self.deg_list = [] #store as data value

    def children(self):
        #4 conditions, check if left isn't empty, right isn't empty, both are empty, both aren't empty
        if self.right != None and self.left != None:
            print(f"Right Node: {self.right} and Left Node: {self.left}")
        elif self.right != None:
            print(f"Right Node: {self.right}")
        elif self.left != None:
            print(f"Left Node: {self.left}")
        print(f"No children :(")

    def degree(self):
        """conjunction in insert and remove"""
        self.deg_list.append(self.degree)
        self.degree = 0#once called returns self.degree to 0 again
        return max(self.deg_list) #returns the max value of the list which is the degree
        
        
    def root(self):
        """ returns root """
        return self.root
        
    def insert(self, data):
        """
        if data = val then put on right by default
        each recursive loop increases degree by 1
        once self.left = None or self.right = None --> assign either one to data
        """
        newnode = treeNode(val = data)
        #iterate through the whole thing using pointer (starting at root)
        while self.left or self.right != None:
        #greater than or less than current node
            if data < self.val:
                if self.left == None:
                    self.pointer.left = newnode
                    self.pointer.right = None 
                    self.degree += 1
                self._increse_depth()
                print(f"degree of tree is now {self.degree()}")
            elif data > self.val:
                if self.right == None:
                    self.pointer.right = newnode
                    self.poitner.left = None
                    self.degree += 1
                self._increase_depth()
                print(f"degree of tree is now {self.degree()}")

            else:
                raise Exception("values must not match values of parent node") 
        self.pointer = self.root


    def _increase_depth(self, data, display = False):
        """Used as a counter for insert and depth methods"""
        if display == True:
            print(self.depth)
        return self.depth += 1 

    def depth(self, data):#TODO
        #traverse until node
        #use _increase_depth()

    def height(self, display = False):
        self.height = self.degree - self.depth
        print(self.height)
        if display == True:
            return self.height

    def remove(self, data):
        #decrease a metric every time the loop starts #FIXME
        """if the child is found in the parent node then assign right or left as None"""
        #similar to insert
        while self.left or self.right != self.val:
            if data < self.val:
                if self.val in self.left:
                    self.left == None
                elif self.val in self.right:
                    self.right == None
            elif data > self.val
                if self.val in self.left:
                    self.left == None
                elif self.val in self.right:
                    self.right == None
            else:
                raise Exception("values must not match values of parent node")

    def index(self, val, display)#TODO
        #add modify value condition




if __name__ == "__main__":

    #Tree implementation 
    root = tree
    tn = treeNode(32, 45, root)
    
    #Doubly linked list
    dll = doublylinkedList()
    dll.insert(data = 45)
    dll.insert(data = 12, ind = 1)
    dll.insert(data = 14, ind = 2)
    dll.insert(data = 15, ind = 2)
    dll.insert(data = 14, ind = 2)
    dll.insert(data = 14, ind = 2)
    dll.insert(data = 15, ind = 2)
    dll.insert(data = 235, ind = 6)
    dll.insert(data = 'sdfsdf', ind = 6)
    dll.insert(data = 5, ind = 6)
    dll.insert(data = 12, ind = 3)
    dll.insert(data = 14, ind = 6)
    dll.insert(data = 15, ind = 6)
    dll.insert(data = 12, ind = 2)
    dll.insert(data = 15, ind = 6)
    dll.insert(data = 15, ind = 6)
    dll.insert(data = 15, ind = 6)
    dll.insert(data = 15, ind = 6)
    dll.delete(ind = 0)
    dll.delete(ind = 1)
    dll.delete(ind = 2)
    dll.delete(ind = 3) 
    dll.modify(ind = 2, data = 4) #works
    dll.modify(ind = 3, data = 4) #FIXME remove first modify and doesn't work properly anymore
    print(dll.display())

    #Singly linked list          
    sll = singlylinkedList#FIXME

    sll.append(data = 33332)
    sll.append(data = 222)
    sll.append(data = 32)
    sll.append(data = 232)
    sll.append(data = 333)


