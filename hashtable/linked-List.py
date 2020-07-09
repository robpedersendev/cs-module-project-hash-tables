# REPR is used for debugging, it return everything for a precise reading
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({repr(self.value)})'


class LinkedList:
    # Instantiate the Singly Linked list class
    def __init__(self):
        self.head = None

    # Create an insert method that adds a node as the head. This is a "Stack" SLL
    def insert(self, node):
        node.next = self.head
        self.head = node

    # Delete
    def delete(self, value):
        current_node = self.head

        # If you are deleting the head of the list
        if current_node.value == value:
            self.head = self.head.next
            return current_node

        # Move to the next node
        prev_node = current_node
        current_node = current_node.next

        # While current_node is not None repeat loop
        while current_node is not None:
            # If the value is the same
            if current_node.value == value:
                # Delete it by bypassing it
                prev_node.next = current_node.next
                # return the current_node
                return current_node
            # Otherwise
            else:
                # Move on to the next node
                prev_node = prev_node.next
                current_node = current_node.next
        # Return None
        return None

    # Lookup a value
    def lookup(self, value):
        # set current_node to the head
        current_node = self.head
        # Loop through linked list
        while current_node is not None:
            # If the nodes value is needed value
            if current_node.value == value:
                # Return the nodes value
                return current_node
            # Else move on to the next node
            current_node = current_node.next
        # Return none
        return None
