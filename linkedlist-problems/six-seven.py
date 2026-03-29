import time

#A stupid 67 program idk :P

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

node1 = Node(6)
node2 = Node(7)

node1.next = node2
node2.next = node1

curr = node1
while curr is not None and curr.next is not None:
  print(curr.data)
  curr = curr.next
  time.sleep(0.5)
