class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    # Function to swap Nodes x and y in linked list by
    # changing links
    def swap(self, x, y):
 
        # Nothing to do if x and y are same
        if x == y:
            return
 
        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
        print(f'\nprevX:{prevX.data}, currX:{currX.data}')
        
        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
            
        print(f'\nprevY:{prevY.data}, currY:{currY.data}')
        
        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else:  # make y the new head
            self.head = currY
 
        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else:  # make x the new head
            self.head = currX
 
        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
                
    
    def get(self, index):
        cur = self.head
        idx = 0
        while cur:
            if idx==index:
                return cur.data
            idx+=1
            cur = cur.next
    
    def length(self):
        cur = self.head
        count = 0
        while cur:
            count+=1
            cur = cur.next
        return count
            
    def push(self, data):
        # Function to insert a new node at the BEGINNING
        '''Complexity Analysis:
            Time Complexity: O(1), We have a pointer to the head and we can 
                directly attach a node and change the pointer. So the Time complexity 
                of inserting a node at the head position is O(1) as it does a constant 
                amount of work.
            Auxiliary Space: O(1)'''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def remove_at(self, index):
        cur = self.head
        idx = 0
        while cur.next and (idx<index):
            prev = cur
            cur = cur.next
            index+=1
        if index==0:
            self.head = self.head.next
        else:
            prev.next = cur.next
        
        
    def append(self, data):
        # Function to insert a new node at the END
        new_node = Node(data)
        cur = self.head
        if cur == None:
            self.head = new_node
        else:    
            while cur.next!=None:
                cur = cur.next
            cur.next = new_node
    
    def insert_after(self, prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def display(self):
        cur_node = self.head
        while cur_node: # self.head is True
            print(cur_node.data, end="->")
            cur_node=cur_node.next
            
    def search(self, data):
        # This Function checks whether the value
        # x present in the linked list
        '''Time Complexity: O(N), Where N is the number of nodes in the LinkedList
        Auxiliary Space: O(1)'''
        cur_node = self.head
        while cur_node:
            if data == cur_node.data:
                print(f"\nYes, {data} exists")
                return None
            else:
                cur_node = cur_node.next
        print(f"\nNo, {data} doesn't exists")
        return None

            
        