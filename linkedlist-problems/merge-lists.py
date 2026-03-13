# merge two sorted singly-linked lists
# example: 5->10->15->40->None and 2->3->20->None
# output:  2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40 -> None

from classes import LinkedList, Node


# def mergeLists(list1, list2):




list1 = LinkedList()
list1.append(5)
list1.append(10)
list1.append(15)
list1.append(40)


list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(20)


print(f"{list1.display()}")
print(f"{list2.display()}")