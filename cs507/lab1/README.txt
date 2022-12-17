*************************************************
* Application of Linked list to Simulate Cache
* CS507
* 12-15-2022
* Stanley Akor
**************************************************

OVERVIEW:
	
 A cache is a computer auxiliary memory that supports fast retrieval of data/information. This program implements a doubly linked list and utilizes its intrinsic properties to implement a cache.

INCLUDED FILES:
 doublylinkedlist.py - implements the doublylinked list and its member functions
 cache.py - main script, containing the cache routine
 cacheclient.py - client script
 README.txt - this file

BUILDING AND RUNNING:

 From the folder containing all the files above and the input textfile, run the cacheclient script, option 1 for one-level cache and 2 two-level cache. Additionally, choose the cache size(s) in any of the options picked. An example on how to successfully compile the file is shown below.
 
 For one-level cache, do;
 $ python cacheclient 1 <cache size> <input textfile name>

 For two-level cache, do;
 $ python cacheclient 2 <1st-level cache size> <2nd-level cache size> <input textfile name>

 Upon successful compilation of the script, the console output will report the cache information ( i.e hit, miss, hit ratio, etc.).

PROGRAM DESIGN:
 
 This task utilizes the DoublyLinkedList (DLL) as an underlying container for the cache. A DLL is a modification of a singly linked list (SLL) such that navigation is possible from the forward and backward directions. Some of the advantages of DLL are: it allows for iteration from both directions, is easily reversed, can be used to implement other data structures like stacks and hash-tables, size can shrink or grow dynamically, etc.
  
 The DLL and cache scripts consist of the following classes: Node, DoublyLinkedList, and Cache (one-level and Two-Level). The Node class has three data members, the Object, next and previous references. The DoublyLinkedList class would maintain appropriate references to the data stored in the list and will provide several methods (for example, in this project, we implemented methods such as; add, remove, addFirst, addLast, etc.). The Cache class uses the DoublyLinkedList as its primary container and utilize some of its methods. 

 To check if an item is in the cache, it will implement a search method by dynamically looping over the items in the list; if this item is found, it will first delete the item and then implement the addFirst method to put the item at the top of the list. However, if the item is not found, it will first check if the items in the cache are less than the maximum limit. If so, it will implement the addFirst method to put the item at the top. Otherwise, it will first remove the last item before adding the new item to the first position on the list.

 TESTING:

 The robustness of the cache would greatly rely on the robustness of the DLL since it's the primary container. All the methods implemented in the DLL were tested under various input conditions. Relevant exceptions were raised in the cases where the inputs were invalid. The cache was tested with the small.txt file, and the results matched the Professor's own. I also tried the cache on the Encyclopedia.txt file and noticed the global reference count is 1347450 instead of 1347451 as shown in result1k2k/result1k5k. After reporting this issue to the TA, he mentioned that the reference is sometimes off by one due to the machine and python version. Other than that, our results are the same.

 DISCUSSION:

  Initially, I had a problem with the code running for too long. I noticed that some of my methods could have been more efficient. By getting rid of some repetitions and fully harnessing the versatility of the DLL, I saw the program run in a shorter time for larger inputs. Overall, I have learned to think about problems independently and find ways to make things work.










