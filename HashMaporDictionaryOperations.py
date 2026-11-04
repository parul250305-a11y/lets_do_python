''' Que --->
Implement a class MyMap that supports the following operations:

insert(int x, int y): Add an entry with key x and value y to the map.
get(int x): Return the value of key x if it is present in the map, otherwise return -1.
size(): Return the number of entries currently in the map.
remove(int x): If key x exists in the map, remove it; otherwise, the map remains unchanged.'''

class MyMap:
    def insert(self, mp, x, y):
        mp[x] = y 

    def get(self, mp, x):
        return mp.get(x,-1)
     

    def size(self, mp):
        return len(mp)
        

    def remove(self, mp, x):
        if x in mp:
            del mp[x]