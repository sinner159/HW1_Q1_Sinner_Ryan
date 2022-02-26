from node import Node

class LinkedList():
    
    def __init__(self):
        self.tail = ListNode()
        self.head = ListNode(None, self.tail)

    def empty(self):
        return self.tail.node == None
    
    def prepend(self, node: Node):

        if self.empty():
            self.tail.node = node
        else:
            list_node = ListNode(node,self.head.next)
            self.head.next = list_node
    
    def append(self, node):
        
        if self.empty():
            self.tail.node = node
            self.head.next = self.tail
        else:
            list_node = ListNode(node)
            self.tail.next = list_node
            self.tail = list_node

    def pop(self):
        if self.empty():
            raise Exception("List is empty")

        if self.head.next == self.tail:
            node = self.tail.node
            self.tail.node = None   
            return node
        
        temp = self.head.next
        self.head.next = temp.next
        node = temp.node
        del temp
        return node


class ListNode():

    def __init__(self, node= None, next = None):
        self.node = node
        self.next = next
    