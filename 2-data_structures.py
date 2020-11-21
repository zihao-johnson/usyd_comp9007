''' concepts:

A. Abstract Data Type (ADT) : is theoretical concepts of data structure from user's view
   1. index-based list: i -- index, e -- element.
        a. size()
        b. isEmpty()
        c. get(i)
        d. set(i,e)
        e. add(i,e)
        f. remove(i)   
   2. positional list: p -- potion, e -- element.
        a. size()
        b. isEmpty()
        c. first()
        d. last()
        e. before(p)
        f. after(p)
        g. insertBefore(p,e)
        h. insertAfter(p,e)
        i. remove(p)
B. Data Structure : concrete representation from implementer's view
   1. Array-based Lists --> see "array class"
        python has not arrary data type without libraries imported, it has only four built-in data type (list, tuple, set and dictionaries),
        from my understanding, python list is an array-based built-in data structure with much richer operations.
        python does not have any as pointers.
        class array is implemented by list with some of its built-in functions
   2. concrete data structure for positional list ADT:
    a. Singly Linked List --> see "linked_list class"
    b. Doubly Linked List --> see "linked_list class"   (same class but argu if_Doubly_linked indicates whether it is singly or doubly linked list)


'''


# ----------B.1 array class----------
# I decide to practise it even useless lol...
class array:
    def __init__(self,list_data):
        self.data = list_data
    def size(self):
        return len(self.data)
    def get(self,i):
        if i > self.size() - 1 or i < 0:
            print("index out of range")
        else:return self.data[i]
    def set(self,i,e):
        if i > self.size() - 1 or i < 0:
            print("index out of range")
        else:self.data[i] = e
    def add(self,i,e): # python has insert(i,e) built-in function...
        # but maunally implement will be...:
        if i > self.size() - 1 or i < 0:
            print("index out of range")
        else:
            list_temper = self.data[i:]
            self.data[i] = e
            for j,e in enumerate(list_temper):
                if i+1+j < self.size():
                    self.data[i+1+j] = e
                else: self.data.append(e)
            # time comlexity equals to theoretically shiftting elements to the left of element i down.  
    def remove(i):
        # python conveniently supports functions to remove from specific index of list:
        #   1. del list[i]
        #   2. list.pop(i)
        # but manually implement will be ...:
        if i > self.size() - 1 or i < 0:
            print("index out of range")
        else:
            for j,e in enumerate(self.data):
                if j >=i:
                    if j<self.size-1:
                        self.data[j] = self.data[j+1]
                    else:
                        del self.data[j]
    def isEmpty(self, absolutely = True):
        '''
            seems there is no any built-in function to check if a list contains values, if a list contains two empty list, check statement using if does not work (see test part t1)
        '''
        if absolutely == True: # list contains nothing, even empty lists
            if not self.data:
                return True
            else: return False
        if absolutely == False:
            return self.check_list_empty(self.data)
    
    def check_list_empty(self,data):
        # recursively checking...
        if type(data)!=type(["list_element_1","list_element_1"]):
            return False
        else:
            if not data:
                flag = True
            else:
                flags = [self.check_list_empty(e) for e in data]
                if flags.count(True) == len(data):
                    flag = True
                else : flag = False
            return flag

                
# ----------B.2.a singly linked list class----------
class LL_node():
    # Linked list element definition 
    def __init__(self, pre_node=None, next_node=None, if_head = False, if_Doubly_linked = False, data = None):
        # pointers is two element list if singly linked, else three elements list
        self.next_node = next_node
        self.if_Doubly_linked = if_Doubly_linked
        if if_head==False:
            self.data = data
            if self.if_Doubly_linked == True:
                self.previous_node = pre_node

class linked_list():
    def __init__(self, nodes, if_Doubly_linked = False):
        # nodes is a list start with header node,
        # initially will linked all nodes in order.
        self.header = nodes[0]
        self.nodes = nodes
        self.if_Doubly_linked = if_Doubly_linked
        self.size = 1  # size include header node
        for i in range(0,len(nodes)-1):
            nodes[i].next_node = nodes[i+1]
            self.size += 1
        if if_Doubly_linked == True:
            for i in range(1,len(nodes)):
                nodes[i].pre_node = nodes[i-1]

    def get_size(self):
        return self.size - 1

    def ifEmpty(self):
        if self.size ==1:
            return True
        else: return False
    
    def first(self):
        return self.header.next_node
    
    def last(self):  
        last = self.header
        for i in range(0,self.size):
            if last.next_node == None:
                return last
            last = last.next_node
    
    def after(self,p):
        return self.nodes[self.nodes.index(p)].next_node
    
    def before(self,p):
        if self.if_Doubly_linked == False:
            last = self.header
            for i in range(0,self.size):
                if last.next_node==p:
                    return last
                last = last.next_node
        else:
            return self.nodes[self.nodes.index(p)].pre_node
    
    def insertAfter(self,p,e):
        e.next_node = self.nodes[self.nodes.index(p)].next_node
        self.nodes[self.nodes.index(p)].next_node = e
        if if_Doubly_linked == True:
            e.pre_node = self.nodes[self.nodes.index(p)].next_node.pre_node
            self.nodes[self.nodes.index(p)].next_node.pre_node = e
        self.size += 1
    
    def insertBefore(self,p,e):
        last = self.header
        for i in range(0,self.size):
            if last.next_node==p:
                e.next_node = last.next_node
                last.next_node = e
                break
            last = last.next_node
        if self.if_Doubly_linked == True:
            e.pre_node = self.nodes[self.nodes.index(p)].pre_node
            self.nodes[self.nodes.index(p)].pre_node = e
        self.size += 1

    def remove(self,p):
        if if_Doubly_linked == False:
            start = header
            for i in range(0,self.size):
                if start.next_node == p:
                    start.next_node = p.next_node
                    p.next_node = None
        else:
            p.pre_node.next_node = p.next_node
            p.next_node.pre_node = p.pre_node
            p.next_node = None
            p.pre_node = None
        self.size -= 1
        


# test...:

# ------------ t1
'''
list_test_1 = []
if not list_test_1:
    print("list_test_1 empty")
list_test_2 = [[],[]]
if not list_test_2:
    print("list_test_2 empty")
'''
# ------------ t2

list1_header = LL_node(if_head=True)
list1_node1 = LL_node(if_head = False,data = 1)
list1_node2 = LL_node(data = 2) 
list1_node3 = LL_node(data = 3)
list1_node4 = LL_node(data = 4)

list1 = linked_list(nodes = [list1_header,list1_node1,list1_node2,list1_node3])
list1.insertBefore(list1_node1,list1_node4)
print(list1.get_size())
print(list1.first().data)
print(list1.last().data)