class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while (temp is not None):
            print(str(temp.data)+" ", end='')
            temp = temp.next
            
        print()
            
    def reverse(self):
        curr = self.head
        prev = None
        nxt = None
        
        while (curr is not None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        self.head = prev
        
    def reverseList(self):
        self.reverseListUtil(self.head)
        
    def reverseListUtil(self, node):
        if (node.next is None):
            self.head = node
            return
        
        self.reverseListUtil(node.next)
        temp = node.next
        temp.next = node
        node.next = None
        
    def nthNodeFromLast(self, n):
        p1 = self.head
        p2 = self.head
        
        for x in range(n):
            p2 = p2.next
            if p2 is None:
                return None
                
        while (p2 is not None):
            p2 = p2.next
            p1 = p1.next
            
        return p1
    
    def middleNode(self):
        p1 = self.head
        p2 = self.head
        
        while ((p2.next is not None) and (p2 is not None)):
            p1 = p1.next
            p2 = p2.next.next
            
        return p1
        
    def makeLoop(self):
        p = self.head
        
        while (p.next is not None):
            p = p.next
            
        p.next = self.head.next.next
        print ("Introduced loop in the list")
        
    def detectAndRemoveLoop(self):
        slow = self.head
        fast = self.head
        
        while ((slow is not None) and (fast is not None) and (fast.next is not None)):
            slow = slow.next
            fast = fast.next.next
            
            if (slow == fast):
                print ("List has a loop")
                self.removeLoop(fast)
                return True
                
        print ("List has no loop")
        return False
        
    def removeLoop(self, fast):
        slow = self.head
        
        while (slow.next != fast.next):
            slow = slow.next
            fast = fast.next
            
        fast.next = None
        
def sumLists(list1, list2):
    
    resultList = LinkedList();
    carry = 0
    sum = 0
    
    while (list1.head is not None or list2.head is not None):
        sum = 0
        if (list1.head is not None):
            sum = sum + list1.head.data
            list1.head = list1.head.next
            
        if (list2.head is not None):
            sum = sum + list2.head.data
            list2.head = list2.head.next
            
        sum = sum + carry   
        carry = int (sum/10)       
        resultList.push(sum%10)
        
        
    if (carry != 0):
        resultList.push(carry)
        
    return resultList
        
list = LinkedList()
list.push(5)
list.push(4)
list.push(3)
list.push(2)
list.push(1)

list.printList()
list.reverse()
list.printList()
list.reverseList()
list.printList()

nthNode = list.nthNodeFromLast(3)
print ("Last nth node data: " + str(nthNode.data))

midNode = list.middleNode()
print ("Middle node of the list " + str(midNode.data))

list.detectAndRemoveLoop()
list.makeLoop()
list.detectAndRemoveLoop()
list.detectAndRemoveLoop()

list1 = LinkedList()
list1.push(4)
list1.push(5)
list1.push(6)

list2 = LinkedList()
list2.push(3)
list2.push(4)
list2.push(5)
list2.push(6)

list3 = sumLists(list1, list2)
list3.printList()
