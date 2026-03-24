#given a binary tree, convert it to a doubly linked list keeping the same order.
#(using in-order traversal, and a global prev variable


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
class Tree:
    def __init__(self):
        self.root = None
        self.nodes = 0
        self.prev = None #(used in conversion function)

    def insert(self, data):
        new_node = Node(data)

        if self.root is None: #check if tree has a root
            self.root = new_node
        
        else:
            current = self.root

            while True:
                if data > current.data:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
                elif data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    break
        self.nodes += 1

    
    #print binary tree values in-order
    def inorder(self, node):
        if node is None:
            return
        
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)


    # IN PROGRESS!! Got discouraged, taking a break
    # convert binary tree to doubly linked list
    # def toDll(self, node):

    #     #either there's a single node in the tree
    #     #or a recursive call reached the bottom of the tree
    #     if node is None:
    #         return node
        
    #     head = self.toDll(node.left)
        
    #     #if prev is 0, root is first node
    #     global prev

    #     if prev is None:
    #         head = node
    #     else:
    #         node.left = self.prev
    #         self.prev.right = node

        
        
    #     self.toDll(node.left)

        


values = [10, 6, 14, 3, 8, 12, 18]

tree = Tree()
for i in values:
    tree.insert(i)

tree.inorder(tree.root)