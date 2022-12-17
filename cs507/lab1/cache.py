from doublylinkedlist import *

############################## CACHE  ################################
class OneLevel_Cache:

    def __init__(self,limit):
            # result initialization
            self.cache_hit = 0
            self.cache_miss = 0

            # initializing the cache
            self.cache = DoublyLinkedList()

            self.cache_limit= limit
            # ensures the user puts in the correct cache limit
            assert self.cache_limit > 0,f' The chosen cache limit is invalid'

    def search(self,arg):

        if self.cache.find(arg):
            self.cache_hit+=1
            
            # locate the index of the item in the cache
            index=self.cache.get_index(arg)

            # remove the item from that index
            self.cache.remove(index)

            # add the item to the top of the cache
            self.cache.addFirst(arg)


        else:

            self.cache_miss+=1

            if self.cache.size() < self.cache_limit:


                self.cache.addFirst(arg)

            else:

                # maintain the cache limit by removing the last item
                self.cache.removeLast()

                # add the new item to the top of the cache
                self.cache.addFirst(arg)

    def size(self):
        return self.cache.size()

    def Info(self):
        return self.cache_hit,self.cache_miss

    def clear(self):
        self.cache.clear()

        # returns the item on the given index
    def get(self,index):
        return self.cache.get(index)

    # add  an item at a specified location in the cache
    def add(self,index,item):
        self.cache.add(index,element)

    # removes an item from the specified location
    def remove(self,index):
        self.cache.remove(index)

    # prints the item in the cache
    def printcache(self):
        self.cache.printlist()

    # return the hit ratio
    def hit_ratio(self):
            return self.cache_hit/(self.cache_hit+self.cache_miss)

class TwoLevel_Cache:

    def __init__(self,limit1,limit2):
            # initializing the results
            self.cache1_hit = 0
            self.cache1_miss = 0

            self.cache2_hit = 0
            self.cache2_miss = 0

            # create two doubly linked list which will serve as cache 1 & 2
            self.cache1 = DoublyLinkedList()
            self.cache2 = DoublyLinkedList()

            self.cache1_limit= limit1
            self.cache2_limit= limit2

            # we want to ensure that the user puts the right cache sizes
            assert self.cache1_limit > 0,f' The chosen cache1 limit is invalid'
            assert self.cache2_limit>0,f' The chosen size of cache2 is invalid'
            assert self.cache2_limit>self.cache1_limit,f'Cache2 limit should be greater than Cache1 limit'



    def search(self,arg):

        if self.cache1.find(arg):

            self.cache1_hit+=1
            
            # find the index of the item in the list
            index=self.cache1.get_index(arg)

            # removes the item from that index
            self.cache1.remove(index)

            # then add the item to the top
            self.cache1.addFirst(arg)

            # what is in cache 1 is also in cache 2
            # bringing item to top of cache 2

            # find the index of the item in the cache
            index2=self.cache2.get_index(arg)
            # remove the item by its index
            self.cache2.remove(index2)
            # add it to the top
            self.cache2.addFirst(arg)

        elif (self.cache1.find(arg)==False) and (self.cache2.find(arg)==True):
            # item only exist in cache 2

            # cache1 miss
            self.cache1_miss+=1

            # cache2 hit
            self.cache2_hit+=1

            # to put the item at the top, we first remove it and add it first.
            index2=self.cache2.get_index(arg)
            self.cache2.remove(index2)
            self.cache2.addFirst(arg)


            # Adding item to top of cache 1.
            # Ensuring the size of the cache is not exceeded

            if self.cache1.size()<self.cache1_limit:
                self.cache1.addFirst(arg)

            else:

                # remove last
                self.cache1.removeLast()
                
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

                self.cache1.removeLast()

                self.cache1.addFirst(arg)


            if self.cache2.size()< self.cache2_limit:

                 self.cache2.addFirst(arg)

            else:
                # maintain the size of the cache

                self.cache2.removeLast()
                self.cache2.addFirst(arg)

    # adds an item at a specified location to the cache
    def add_Cache1(self, index, element):
        self.cache1.add(index,element)

    def add_Cache2(self,index,element):
        self.cache2.add(index,element)

    # removes an item at a specified location from the cache
    def remove_Cache1(self,index):
        sel.cache1.remove(index)

    def remove_Cache2(self,index):
        sel.cache2.remove(index)

    # remove every item from the cache
    def clear_Cache1(self):
        self.cache1.clear()

    def clear_Cache2(self):
        self.cache2.clear()

    #returns item at given index
    def get_Cache1(self,index):
        return self.cache1.get(index)

    def get_Cache2(self,index):
        return self.cache2.get(index)

    # prints all the items in the cache
    def printcache1(self):
        self.cache1.printlist()

    def printcache2(self):
        self.cache2.printlist()

    # first level cache hit ratio
    def cache1_hitratio(self):
        return self.cache1_hit/(self.cache1_hit+self.cache1_miss)
    
    # second level cache hit ratio
    def cache2_hitratio(self):
        return self.cache2_hit/self.cache1_miss

    # global cache hit ratio
    def global_hitratio(self):
        return(self.cache1_hit+self.cache2_hit)/(self.cache1_hit+self.cache1_miss)

    # tuple of simulation results
    def Info(self):
        return self.cache1_hit,self.cache1_miss,self.cache2_hit,self.cache2_miss

    def size_cache1(self):
        return self.cache1.size()

    def size_cache2(self):
        return self.cache2.size()



