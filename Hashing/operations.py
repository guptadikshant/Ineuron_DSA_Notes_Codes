class HashTable:

    def __init__(self):
        self.MAX_VALUE = 10
        # intialization of array with None values
        self.arr = [None] * self.MAX_VALUE

    def hashFunction(self,key):
        """
        It gives unique key number from the given key
        It based on division-modulo hash function
        """
        summation = 0
        m =10
        for char in key:
            summation += ord(char)

        return summation % self.MAX_VALUE


    def __setitem__(self, key, value):
        hash_key = self.hashFunction(key)
        self.arr[hash_key] = value


    def __getitem__(self, key):

        hash_key = self.hashFunction(key)
        return self.arr[hash_key]


    def print_hashtable(self):
        return self.arr


if __name__ == "__main__":
    # hash_obj = HashTable()
    # # print(hash_obj.arr)

    # # Add values into hash map
    # hash_obj.addItem("demo value1", 1231)
    # hash_obj.addItem("demo value2", 1232)
    # hash_obj.addItem("demo value3", 1233)
    # hash_obj.addItem("demo value4", 1234)
    # hash_obj.addItem("demo value5", 1235)

    # # print the hash map
    # print(hash_obj.print_hashtable())

    # # get the value corresponding to the given key
    # print(hash_obj.getItem("demo value1"))

    hash_obj1 = HashTable()
    hash_obj1["new value"] = 5467

    print(hash_obj1["new value"])

