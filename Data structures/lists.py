l1 = [1,2,3,4,5]
l2 = [6,10,7,8,9,10]
l3 = [l1,l2]
list_A = list(range(5))

l1.append(6)        #Add an item to the end of the list
l1.extend([7,8,9])  #Extend the list by appending all the items from the iterable
l1.insert(0,0)      #Insert an item at a given position.
l1.remove(5)        #Remove the first item from the list whose value is equal to x.
l1.pop(2)           #Remove the item at the given position in the list
l1.pop()            #removes and returns the last item in the list
l1.clear()          #Remove all items from the list


l2.index(8)         #Return index in the list of the first item whose value is equal to x.
l2.count(10)        #Return the number of times x appears in the list.
l2.sort()           #Sort the items of the list in place 
l2.reverse()        #Reverse the elements of the list in place.

# =========== Using Lists as Queues ============= #
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()      # "Eric" The first to arrive now leaves
queue.popleft()      # "John" The second to arrive now leaves

# ============== List Comprehensions ============= #
squares = [x**2 for x in range(10)]
#squares = list(map(lambda x: x**2, range(10)))

l = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]