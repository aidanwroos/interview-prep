#sort and merge two singly linked lists
#time O(nlogn) recursive, space O(1) in place with some pointer rewiring :P

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  

class LinkedList:


  def __init__(self):
    self.head = None
    self.nodes = 0


  def append(self, data):
    new_node = Node(data) #instantiate new node
    new_node.next = None

    if self.head is None: #case: list empty
      self.head = new_node
      
    else: #case: list has elements already
      current = self.head
      while current.next is not None: #walk to end of list
        current = current.next
      current.next = new_node         #attach newnode to end
    self.nodes += 1


  def printList(self, head):
    current = head #start of beginning of list

    while current is not None:
      print(current.data, end=" -> ")

      if current.next is None:
        print("None")
      current = current.next


  def split(self, head):
    #find the middle
    slow = head
    fast = head.next

    #fast isn't none, and next element isn't none
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    mid = slow.next

    #breaks list in half
    slow.next = None

    #left, right halves list
    return head, mid


  #recursively sort each half of list until base case
  def sort(self, head):

    #head of sublist is none (list has 0), or next element is none (list has 1)
    if head is None or head.next is None:
      return head

    #split sublist into left, right
    l, r = self.split(head)
    left = self.sort(l)
    right = self.sort(r)

    return self.merge(left, right)


  #merge left and right sorted lists into 1
  def merge(self, left, right):

    #whichever is empty first
    if left is None:
      return right
    if right is None:
      return left

    #compare the heads of the sublists to see which one is greater than the other
    #whichever is smaller points to the greater one
    if left.data < right.data:
      left.next = self.merge(left.next, right)
      return left
    else:
      right.next = self.merge(left, right.next)
      return right


ll = LinkedList()
array = [8,2,4,1,7,6,4]
for i in array:
  ll.append(i)

print("Original: ", end="")
ll.printList(ll.head)
ll.head = ll.sort(ll.head)
print("Sorted: ", end="")
ll.printList(ll.head)
