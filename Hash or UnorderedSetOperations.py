"""mplement a class MySet that supports the following operations:

insert(int x): Insert the element x into the set. If x is already present, the set remains unchanged.
erase(int x): Remove the element x from the set if it exists. If x is not present, the set remains unchanged.
size(): Return the number of distinct elements present in the set. If the set is empty, return 0.
find(int x): Return 1 if the element x is present in the set; otherwise, return -1."""

class MySet:
    
    # Insert an element into the set.
    def insert(self, s, x):
        s.add(x)
        

    # Remove an element from the set if it exists.
    def erase(self, s, x):
        s.discard(x)

    # Return the number of distinct elements in the set.
    def size(self, s):
        return len(s)

    # Return 1 if the element exists; otherwise, return -1.
    def find(self, s, x):
        if x in s:
            return 1
        else:
            return -1