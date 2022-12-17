############################## NODE ###########################################
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

############################## DOUBLYLINKEDLIST ################################
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # add an item to the first position of the linked list
    def addFirst(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
    
    # add an item to the last position on the linked list
    def addLast(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    # add an item to the indicated position on the list
    def add(self, index, data):
        new_node = Node(data)

        if index < 0 or index > self.length:
            raise Exception('Chosen index {index} is invalid!')
        else:
            if index == 0:
                self.addFirst(data)
            elif index == self.length:
                self.addLast(data)
            else:
                temp = self.head
                for i in range(index-1):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp
                self.length+=1
                
    # removes the first item from the list
    def removeFirst(self):

        if self.head != None:
            self.length-=1
            if self.head is self.tail:
                data = self.head.data
                self.head = self.tail = None
            else:
                data = self.head.data
                self.head = self.head.next
                self.head.prev = None
            return data

        else:
            raise Exception('Doubly linked list is empty!')
     
    # removes the last item from the list 
    def removeLast(self):
        if self.head != None:
            self.length-=1
            if self.head is self.tail:
                data = self.head.data
                self.head = self.tail = None
            else:
                data = self.tail.data
                self.tail = self.tail.prev
                self.tail.next = None
            return data

        else:
            raise Exception('Doubly linked list is empty!')
    
    # removes an item from the indicated index in the list
    def remove(self, index):
        if index < 0 or index >= self.length:
            if self.head is None:
                raise Exception('Doubly linked list is empty')
            else:
                raise Exception(f'The index {index} entered is invalid!')
        else:

            if index == 0:
                self.removeFirst()
            elif index == self.length-1:
                self.removeLast()
            else:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                prev_node = temp.prev
                prev_node.next = temp.next
                temp.next.prev = prev_node
                self.length-=1
    
    # returns the first item on the list
    def getFirst(self):
        if self.head != None:
            return self.head.data
        else:
            raise Exception('Doubly Linked List is empty')

    # returns the last element in the linked list
    def getLast(self):
        if self.tail != None:
            return self.tail.data
        else:
            raise Exception('Doubly Linked List is empty')

    # prints the element in the doubly linked list
    def printlist(self):
        if self.head is None:
            raise Exception('Doubly Linked List is empty')
        curr_node = self.head
        while curr_node !=None:
            print(curr_node.data, end=",")
            curr_node = curr_node.next

    # returns the size of the list
    def size(self):
        return self.length
   
    # replaces the elment at the specified index in the list with the specified element.
    def set(self, index, element):
        if index < 0 or index >= self.length:
            if self.head is None:
                raise Exception('Doubly linked list is empty')
            else:
                raise Exception(f'The index {index} entered is invalid!')
        else:
            if index == 0:
                self.head.data = element
            elif index == self.length-1:
                self.tail.data = element
            else:

                temp = self.head

                # traverse up to the position
                for i in range(0, index):
                    temp = temp.next

                temp.data = element

    # returns the element at the specified position in the list.
    def get(self,index):
        if (index > self.length -1) or (index < 0):
            if self.head is None:
                raise Exception('Doubly linked list is empty')
            else:
                raise Exception(f'index {index} out of range')
        else:

            if index == 0:
                return self.head.data

            elif index == self.length -1:
                 return self.tail.data

            else:
                temp = self.head

                # traverse the list
                for i in range(0, index):
                    temp = temp.next

                return temp.data
            
            
    # removes all the items from the list       
    def clear(self):
        if self.head is None:
            raise Exception('List is already empty')
        else:
            self.length = 0
            while self.head!= None:
                curr=self.head
                self.head = self.head.next
                curr = None
                
# Below are some extra methods that will help in the cache implementation


    # this method checks whether a given element exist in the linked list
    def find(self, element):
        curr = self.head;
        if self.head == None:
         # empty list
           return False
        while curr != None:
            if curr.data == element:
                return True
            curr = curr.next
        return False
    
     
    # returns the index/position of an element in the list
    def get_index(self, element):
        if self.head:
            curr=self.head
            index=0
            while curr != None:
                if curr.data == element:
                    return index
                curr = curr.next
                index += 1
            raise Exception('element cannot be found in the list')
        else:
            raise Exception('Doubly linked list is empty!')
            
    # returns a list containing all the elements in the list.
    def get_data(self):
        data = []
        node = self.head
        while node:
            data.append(node.data)
            node = node.next

        return data



