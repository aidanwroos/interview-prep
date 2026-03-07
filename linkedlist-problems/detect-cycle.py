# Detect cycle in a singly linked list
# returns true if a node points to a previously visited node instead of pointing to None (NULL)
# 1->2->3->4
#   |      |
#   -------
# ex: node w/ value 4 points to previously visited node w/ value 2
#     meaning there is a cycle, so function should return true
#     (note: the values of the nodes themselves do not have any influence on the outcome)

from classes import LinkedList, Node

# TEST 1: List having no cycle occurance
def noCycle():
    ll = LinkedList()
    for i in range(1, 5):
        ll.append(i)
    return ll
    # 1 -> 2 -> 3 -> 4 -> None

# TEST 2: List where its last node cycles back to the head
def cycleToHead():
    ll = LinkedList()
    for i in range(1, 5):
        ll.append(i)
    # get tail
    tail = ll.head
    while tail.next:
        tail = tail.next
    #point tail back to head
    tail.next = ll.head
    return ll

# TEST 3: List where the last node cycles back to the middle node of the list
def cycleToMiddle():
    ll = LinkedList()
    for i in range(1, 5):
        ll.append(i)

    list_len = ll.get_length()
    middle_index = list_len // 2
    
    #get tail and middle node
    tail = ll.head
    middle = None
    current = ll.head
    i = 0
    while current:
        if i == middle_index:
            middle = current
        tail = current
        current = current.next
        i += 1

    # point tail back to the middle
    tail.next = middle
    return ll



# Function to detect a cycle in the above 3 lists
# Floyd's Cycle Finding algorithm
# I chose Floyd's over a hashset approach because:
# 1. O(1) space vs O(n) space — Floyd's only uses two pointers,
#    while a hashset stores a reference to every visited node
# 2. Both approaches are O(n) time, so Floyd's is strictly more
#    space efficient with no tradeoff
# A hashset would store node references (not values), so duplicate
# values wouldn't cause false positives — but the space cost makes
# Floyd's the better choice

def detectCycle(ll):
    
    slowptr = ll.head
    fastptr = ll.head

    # while slow and fast ptrs and next fastptr isn't None
    while slowptr and fastptr and fastptr.next:

        slowptr = slowptr.next       # increment by 1
        fastptr = fastptr.next.next  # increment by 2

        if slowptr == fastptr:       # if both ptrs land on same node
            return True
    
    return False # no cycle found



# TEST RESULTS

ll1 = noCycle()
print(f"{ll1.display_safe(20)}")
print(f"{detectCycle(ll1)}\n")

ll2 = cycleToHead()
print(f"{ll2.display_safe(20)}")
print(f"{detectCycle(ll2)}\n")

ll3 = cycleToMiddle()
print(f"{ll3.display_safe(20)}")
print(f"{detectCycle(ll3)}\n")


