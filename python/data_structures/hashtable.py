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
        # has the key and set the key and value pair in the table
        hash_index = self.hash(key)
        # get index of hashing function

        bucket = self.buckets[hash_index]

        if bucket is None:

            self.buckets[hash_index] = LinkedList()
        # if no linked list in bucket then make one and put into bucket

        #TODO: handle updates
        self.buckets[hash_index].insert((key, value))
    # insert the key value pair at the index of the bucket in hash


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
        if not self.get(key):
            return bool(self.get(key))


    def keys(self):
# returns a collection of keys
        key_list = set()
# setting the key_list to be populated later
        for bucket in self.buckets:
            if bucket is not None:
# checking if bucket exists
# if it doesn't exist set the current to the head of LL
                current = bucket.head
                while current:
                    pair = current.value
                    current_key = pair[0]
                    key_list.add(current_key)
                    current = current.next
# loop through the current bucket heads and check values and assign key to 0 index of the pair
# add the current key to the key list and move onto the next current
        return key_list







