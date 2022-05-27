from data_structures.linked_list import LinkedList
class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        # returns index in collection for that key

        sum_of_chars = 0
        for char in key:
            sum_of_chars += ord(char)

        primed = sum_of_chars * 599

        index = primed % self.size

        return index

    def set(self, key, value):
        # has the key and set the key and value pari in the table
        hash_index = self.hash(key)
        # get index of hashing function

        bucket = self.buckets[hash_index]

        if bucket is None:
            bucket = LinkedList()
            self.buckets[hash_index] = bucket
        # if no linked list in bucket then make one and put into bucket

        #TODO: handle updates
        bucket.append((key, value))

    def get(self, key):
        # returns value associated with key in the table
        index = self.hash(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]

            current = current.next
        return None

    def contains(self, key):
# Arguments: key
# Returns: Boolean, indicating if the key exists in the table already.
        return bool(self.get(key))

    def keys(self):
# returns a collection of keys
        key_list = []
        for key in self.buckets[0]:
            key_list.append(key)

        return key_list







