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


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.count = 0
        # An Array of linked lists
        self.data = [LinkedList()] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        Could only find information on FNV1a
        """
        # Placed the seed value within the function
        seed = 0
        FNV_prime = 578421533
        offset_basis = 5548812254

        fnv1_hash = offset_basis + seed
        for char in key:
            fnv1_hash = fnv1_hash * FNV_prime
            fnv1_hash = fnv1_hash ^ ord(char)
        return fnv1_hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Assign node to the value of hash_index method
        node = self.hash_index(key)
        # Grab the head of the head of the linked List, cause the LinkedList() is created with a head
        current_node = self.data[node].head

        # While there is a current_node
        while current_node:
            # If the the current nodes key is the key were looking for
            if current_node.key == key:
                # Set the current nodes value to the value
                current_node.value = value
            # Otherwise move along to the next node
            current_node = current_node.next

        new_node = HashTableEntry(key, value)
        # Insert a new node into the data object (the stack SLL)
        self.data[node].insert(new_node)
        # Add to the data objects total weight
        self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Use the PUT method to trick the linked list to remove the entry with the specific key
        self.put(key, None)
        # Decrement the data objects total weight
        self.count -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Assign node to the value of hash_index method
        node = self.hash_index(key)
        # Grab the head of the head of the linked List, cause the LinkedList() is created with a head
        current_node = self.data[node].head

        # While there is a current_node
        while current_node:
            # If the the current nodes key is the key were looking for
            if current_node.key == key:
                # Return the current nodes value
                return current_node.value
            # Otherwise move along to the next node
            current_node = current_node.next


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
