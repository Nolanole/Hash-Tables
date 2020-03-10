# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        linked_pair = LinkedPair(key, value)
        #if something is stored at the index
        if self.storage[index]:
            #set current node to first node in the bucket
            curr_lp = self.storage[index]
            
            #if the key matches
            if curr_lp.key == key:
                #overwrite the value for that key
                curr_lp.value = value

            else: #if key didnt match
                #iterate through the chain of nodes in this bucket
                while curr_lp.next:
                    #update current node to the next node
                    curr_lp = curr_lp.next
                    if curr_lp.key == key:
                        curr_lp.value = value
                        return
                #if the end of the chain is reached and no matching key is found, add the node to the end of the chain
                curr_lp.next = linked_pair

        #if the bucket at this index was empty, add the node to the bucket
        else:
            self.storage[index] = linked_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        #If something is stored at the index
        if self.storage[index]: 
            #set the first item to curr_lp var
            curr_lp = self.storage[index]
            #if key at first item matches the key we want to remove: 
            if curr_lp.key == key: 
                #remove the node by re-assigning the first node in the storage at that index as the next node in the chain and return
                self.storage[index] = curr_lp.next
                return
            #if the first node key doesnt match, iterate through the rest of the bucket checking for matching key:
            #if next node is None, break the loop and print 'key not found'
            while curr_lp.next: 
                #if next node key matches
                if curr_lp.next.key == key:
                    #change the next node to the node after the next node (thereby removing the matching key node from the chain)
                    curr_lp.next = curr_lp.next.next
                    return
                #if next node key doesnt match
                else:
                    #move on to next node in the chain
                    curr_lp = curr_lp.next
        print('Warning- key not found')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        #if something is stored at the index bucket:
        if self.storage[index]:
            curr_lp = self.storage[index] #assign current node
            #iterate thru the chain searching for matching key
            while curr_lp:
                #if matching key found, return the value
                if curr_lp.key == key: 
                    return curr_lp.value
                else:
                    curr_lp = curr_lp.next
        #if matching key not found:
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        #double the capacity and set up the new storage of Nones
        self.capacity *= 2
        self.storage = [None] * self.capacity
        
        #iterate thru the buckets from previous
        for item in old_storage:
            #start with first node
            curr_lp = item
            while curr_lp:
                #add the node to the new storage
                self.insert(curr_lp.key, curr_lp.value)
                #move on to the next node in the chain
                curr_lp = curr_lp.next              


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")