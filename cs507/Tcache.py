################################ NODE ##########################################
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        

################################### DOUBLYLINKEDLIST #############################        
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
        
    def size(self):
        return self.length
    
    def addFirst(self,element):
        curr_node = Node(element)
        curr_node.next = self.head
        curr_node.prev = None
        
        self.length+=1
   
        if self.head != None:
            self.head.prev = curr_node
        self.head = curr_node        
    
        
    def printlist(self):
        if self.head is None:
            raise Exception('List is empty')
            
        curr_node = self.head
        while curr_node !=None:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
            
    def addLast(self, element):
        curr_node = Node(element)
        if self.head is None:
            self.head = Node(element)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = curr_node
            curr_node.prev = temp
        self.length+=1
                     
    def getFirst(self):
        if self.head is None:
            raise Exception('List is empty')
        return self.head.data
    
    def getLast(self):
        if self.head is None:
            raise Exception('List is empty') 
            
        cur_node = self.head 

        while cur_node.next != None:
            cur_node = cur_node.next
            
        return cur_node.data

    
    def removeFirst(self):
        if self.head is None:
            raise Exception('List is empty')
        if self.head.next is None:
            self.head = None
        self.head = self.head.next
        self.head.prev = None
        self.length-=1
        
    
    def removeLast(self):
       
        if self.head == None:
            raise Exception('List is empty')  
        if self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.prev.next = None
            n.prev = None
        self.length-=1
        
            
            
    def clear(self):
        self.length=0
        if self.head == None:
            raise Exception('List is already empty')
            
        while self.head!=None:
            n = self.head
            self.head= self.head.next
            n = None
            
            
    def add(self, index, element):
        
        self.length+=1
        node = Node(element)

        if self.head is None:
            self.head = node
            return
    
        if index == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
  
        n = self.head
        n_p = 0
        while n and index > n_p:
            n_p += 1
            n = n.next
        # Insert the new node
        if n is None:
            prev_node.next = node
            node.prev = prev_node
            
        
            
    def set(self, index, element): 
   
        if self.head == None: 
            raise Exception('List is empty')
            
        self.length+=1    

        temp = self.head 

        # traverse up to the position 
        for i in range(0, index): 
            temp = temp.next
            if temp is None: 
                break

        # position found, element is updated
        if temp is not None: 
            temp.data = element

        else: 
            raise Exception('index does not exist in the list')            
   
    def remove(self,index):  
        if self.head is None:
            raise Exception('cannot delete from an empty list')
        
        self.length-=1
        # delete first item on the list
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
            
        # Store the current node in a temp variable.
        current = self.head
        # Store the previous node in a temp variable.
        previous = None
        # Store the current position.
        current_pos = 0

        # Iterate over the list.
        while current_pos < index and current.next is not None:
            # Update the previous node.
            previous = current
            # Update the current node.
            current = current.next
            # Increment the position.
            current_pos += 1

        # If the list is empty or position is greater than the list size.
        if current is None:
             raise Exception('index does not exist in list')

        # Remove the node by updating the links.
        if previous is None:
            head = current.next
        else:
            previous.next = current.next
                  
            
    def get(self,index):
        if self.head==None:
            raise Exception('List is empty')
        temp = self.head   
        # traverse the list    
        for i in range(0, index): 
            temp = temp.next
            if temp is None: 
                break
                
        if temp is not None: 
            return temp.data
        
        else: 
            raise Exception('index does not exist in the list')

    def get_data(self):
        data = []
        node = self.head
        while node:
            data.append(node.data)

            node = node.next

        return data 

    
    def get_index(self,element):
        data = self.get_data()
        
        index = None
        
        if element in data:
            index = list(data).index(element)
            
        return index 


################################### CACHE ###################################################################    
   
class   OneLevel_Cache:
    
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
                self.cache.remove(self.cache_limit-1)
                     
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
                self.cache1.remove(self.cache1_limit-1)
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
                self.cache1.remove(self.cache1_limit-1)


                self.cache1.addFirst(arg)


            if self.cache2.size()< self.cache2_limit: 

                 self.cache2.addFirst(arg)

            else:      
                            # maintain the size of the cache
                self.cache2.remove(self.cache2_limit-1)


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

               

            
                    
                   
                    
            
            
                    



                            
                            
                        
                        
        
        
        
        
        
        
        
            
           
  
