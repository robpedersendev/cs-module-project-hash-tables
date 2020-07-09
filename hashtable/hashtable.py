from linked_list import LinkedList
import sys
sys.path.append('../hashtable/linked-list')


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
        inx = self.hash_index(key)
        # If there is nothing in the linked list
        if self.data[inx] == None:
            # Create a new one with an empty key and value
            self.data[inx] = HashTableEntry(key, value)
            # Increase the size of the Linked list, used to get number of items in LL
            self.count += 1
            # If there is something in the linked list
        else:
            # Set node equal to the index value within the data (the buildout version of the LL)
            node = self.data[inx]
            # If the value entered equals the value of the key of the node
            if node.key == key:
                # Then then value of the node is equal to the value of the value of the node
                node.value = value
                # If the entered input doesnt equal any node
            else:
                # Loop through list while there is a value in .next and the value in .key is not the input
                while node.next is not None and node.key != key:
                    # Point to the next node
                    node = node.next
                # Once loop is done, create a new next value with the input
                node.next = HashTableEntry(key, value)
                # increase the count
                self.count += 1

        if self.get_load_factor() > 0.7:
            self.resize(2 * self.capacity)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


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
