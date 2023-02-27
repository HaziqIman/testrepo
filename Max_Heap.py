class Max_Heap:
    def __init__(self, arr=[], method = 'heapify'):
        self.swap_counter = 0
        self.heap = [] # initilazing heap with no elements

        if method == 'heapify':
            self.heapify(arr)
        else:
            if arr is not None:
                for value in arr:
                    self.enqueue(value)
    
    ## heapify method uses a top-down approach, starting from the bottom nodes to reshape tree into a heap
    def heapify(self, arr):
        if arr is not None:
            self.heap = arr
            for i in range(len(self.heap)//2, -1, -1):
                    self.top_down(self.heap, i)

    ### enqueue method to insert new element into the heap
    def enqueue(self, value):
        self.heap.append(value) # add the new element at the end of the heap list
        self.bottom_up (self.heap, len(self.heap)-1) # adjust the position of the newly added element

    def dequeue(self):
        if len(self.heap)!=0:         # swapping the root value with the last value.
            self.swap(self.heap, len(self.heap)-1, 0)
            
            # storing the dequeued value in the root variable
            root = self.heap.pop()

            #Calling the top_down function to ensure that the heap is still in order 
            self.top_down(self.heap, 0)   
        else:
            root="Heap is empty"
        return root

    def bottom_up(self, heap, index):
        # find the parent of the element
        parent_index = (index -1 ) // 2
        
        #if we are already at the root node, the  all done, can return 
        if parent_index < 0:
            return
        
        # if the current node is greater than the parent node, swap them
        if heap[index] > heap[parent_index]:
            ##swap these elements
            self.swap(heap, index, parent_index)
            self.bottom_up(heap, parent_index)

    def top_down(self, heap, index):
        child_index = 2 * index + 1
        # If we are at the end of the heap, return nothing
        if child_index >= len(heap):
            return

        # Of the two children find the larger one
        if child_index + 1 < len(heap) and heap[child_index] < heap[child_index + 1]:
            child_index += 1

        # If the child node is smaller than the current node, swap them
        if heap[child_index] > heap[index]:
            self.swap(heap, child_index, index)
            self.top_down(heap, child_index)

    ## swaps two elemets in a list
    def swap(self, L,i,j):
        self.swap_counter += 1
        L[i], L[j] = L[j], L[i]

################
a = [1,2,3,4,5]
myheap = Max_Heap(a,'heapify')
print('swaps done = ',myheap.swap_counter)
print(myheap.heap)
myheap.enqueue(6)
print(myheap.heap)
for i in range(len(a)):
    print("Root dequeued:",myheap.dequeue())
###############

##heapSort ####
def heapsort(arr):
    barr =[]
    myheap = Max_Heap(arr,'heapify')
    for i in range(len(arr)):
        barr.append(myheap.dequeue()) 
    return barr

print(heapsort([5,9,2,18,7]))