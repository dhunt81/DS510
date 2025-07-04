from Node import *

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")
    
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
    
        raise Exception("Node with data '%s' not found" % target_node_data)    
    
    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")
    
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
    
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
    
        raise Exception("Node with data '%s' not found" % target_node_data)

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)