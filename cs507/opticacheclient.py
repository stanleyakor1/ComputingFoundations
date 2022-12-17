class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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

    def add(self, index, data):
        new_node = Node(data)

        if index < 0 or index > self.length:
            raise Exception('Chosen index is invalid!')
        else:
            self.length+=1
            if index == 0:
                self.addFirst(data)
            elif index == self.length:
                self.addLast(data)
            else:
                temp = self.head
                for _ in range(index-1):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp

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

    def remove(self, index):
        if index < 0 or index >= self.length:
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

    def getFirst(self):
        if self.head != None:
            return self.head.data
        else:
            raise Exception('Doubly Linked List is empty')

    def getLast(self):
        if self.tail != None:
            return self.tail.data
        else:
            raise Exception('Doubly Linked List is empty')
            
    def printlist(self):
        if self.head is None:
            raise Exception('List is empty')
            
        curr_node = self.head
        while curr_node !=None:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
            

    def get_data(self):
        data = []

        node = self.head

        while node:
            data.append(node.data)

            node = node.next

        return data
    
    def size(self):
        return self.length
    

    def get_index(self, element):
        if self.head:
            current=self.head
            index=0
            while current != None:
                if current.data == element:
                    return index
                current = current.next
                index += 1
            raise AttributeError('element cannot be found in the list')
        else:
            raise Exception('Doubly linked list is empty!')

      
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

    def get(self,index):
        if (index > self.length -1) or (index < 0):
            raise ValueError(f' index out of range')
        elif self.head==None:
            raise Exception('List is empty')
    
        elif index == 0:
            return self.head.data

        elif index == self.length -1:
             return self.tail.data

        else:
            temp = self.head
        # traverse the list
            for i in range(0, index):
                temp = temp.next
                if temp is None:
                    break

            if temp is not None:
                return temp.data


class OneLevel_Cache:
    
    def __init__(self,limit):
            self.cache_hit = 0
            self.cache_miss = 0
            
            self.cache = DoublyLinkedList()   
           
            self.cache_limit= limit
            assert self.cache_limit > 0,f' The chosen cache limit is invalid'
            
    def search(self,arg):

        if arg in self.cache.get_data():
                
            self.cache_hit+=1     
            index=int(self.cache.get_index(arg))
            self.cache.remove(index)
                      
            self.cache.addFirst(arg)
                
  
        else:
                 
            self.cache_miss+=1
                
            if self.cache.size() < self.cache_limit:
                                 
                    
                self.cache.addFirst(arg)
                    
            else:
                   
                    
                     # to remove the last element   
               # self.cache.remove(self.cache_limit-1)
                self.cache.removeLast()
                     
                self.cache.addFirst(arg)
                     
                    
    def Info(self):
        return self.cache_hit,self.cache_miss
    
    def clear(self):
        self.cache.clear()

        # returns the item on the given index
    def get(self,index):
        data = self.cache.get_data()
        assert 0<=index<len(data),f'chosen index {index} is invalid'
        return data[index]

        # add  an item at a specified location in the cache
    def add(self,index,item):
        self.cache.add(index,element)
        
        # removes an item from the specified location
    def remove(self,index):
        sel.cache.remove(index)
        
          # prints the item in the cache      
    def print__cache(self):
            data=self.cache.get_data()
            for values in data:
                print(values,end=', ')

         # return the hit ratio       
    def hit_ratio(self):        
            return self.cache_hit/(self.cache_hit+self.cache_miss)
        
    
class TwoLevel_Cache:
    
    def __init__(self,limit1,limit2):
            self.cache1_hit = 0
            self.cache1_miss = 0
            
            self.cache2_hit = 0
            self.cache2_miss = 0
        
            self.cache1 = DoublyLinkedList()
            self.cache2 = DoublyLinkedList()
           
            self.cache1_limit= limit1
            self.cache2_limit= limit2
            
            assert self.cache1_limit > 0,f' The chosen cache1 limit is invalid'
            assert self.cache2_limit>self.cache1_limit,f'Cache2 limit should be greater than Cache1 limit'
            assert self.cache2_limit>0,f' The chosen size of cache2 is invalid' 
            
            
            
    def search(self,arg):

        if arg in self.cache1.get_data():

            self.cache1_hit+=1
            index=int(self.cache1.get_index(arg))
            self.cache1.remove(index)
            self.cache1.addFirst(arg)



            # what is in cache 1 is also in cache 2
            # bringing item to top of cache 2

            index2=int(self.cache2.get_index(arg))
            self.cache2.remove(index2)
            self.cache2.addFirst(arg) 

        elif (arg not in self.cache1.get_data()) and (arg in self.cache2.get_data()):

                 # cache1 miss
            self.cache1_miss+=1

                # cache2 hit
            self.cache2_hit+=1

            # to put the item at the top, we first remove it and add it first.
            index2=int(self.cache2.get_index(arg))
            self.cache2.remove(index2)
            self.cache2.addFirst(arg)


                        # Adding item to top of cache 1.
                        # Ensuring the size of the cache is not exceeded

            if self.cache1.size()<self.cache1_limit:
                self.cache1.addFirst(arg)

            else:

                # remove last
                self.cache1.removeLast()
                #self.cache1.remove(self.cache1_limit-1)
                            # add new item to first
                self.cache1.addFirst(arg)


        else:

                # when item is not in cache1 and cache2

            self.cache1_miss+=1 
            self.cache2_miss+=1

            if self.cache1.size() < self.cache1_limit:        
                self.cache1.addFirst(arg)

            else:
                            # maintain the size of the cache
                #self.cache1.remove(self.cache1_limit-1)
                self.cache1.removeLast()

                self.cache1.addFirst(arg)


            if self.cache2.size()< self.cache2_limit: 

                 self.cache2.addFirst(arg)

            else:      
                            # maintain the size of the cache
                #self.cache2.remove(self.cache2_limit-1)

                self.cache2.removeLast()
                self.cache2.addFirst(arg)

                            
    def add_Cache1(self, index, element):
        self.cache1.add(index,element)
        
    def add_Cache2(self,index,element):
        self.cache2.add(index,element)
        
    def remove_Cache1(self,index):
        sel.cache1.remove(index)
        
    def remove_Cache2(self,index):
        sel.cache2.remove(index)
                            
    def clear_Cache1(self):
        self.cache1.clear()

    def clear_Cache2(self):
        self.cache2.clear()

        #returns item at given index
    def get_Cache1(self,index):
            data=self.cache1.get_data()
            assert 0<=index<len(data),f'chosen index {index} is invalid'
            return data[index]

    def get_Cache2(self,index):
            data=self.cache2.get_data()
            assert 0<=index<len(data),f'chosen index {index} is invalid'
            return data[index]

    def printcache1(self):
        data=self.cache1.get_data()
        for values in data:
            print(values,end=', ')

    def printcache2(self):
        data=self.cache2.get_data()
        for values in data:
            print(values,end=', ')

    def cache1_hitratio(self):
        return self.cache1_hit/(self.cache1_hit+self.cache1_miss)

    def cache2_hitratio(self):
        return self.cache2_hit/self.cache1_miss

    def global_hitratio(self):
        return(self.cache1_hit+self.cache2_hit)/(self.cache1_hit+self.cache1_miss)
    
    def Info(self):
        return self.cache1_hit,self.cache1_miss,self.cache2_hit,self.cache2_miss

               

            
                    
