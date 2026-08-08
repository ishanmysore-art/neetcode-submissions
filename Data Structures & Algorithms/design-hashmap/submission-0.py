class MyHashMap:

    def __init__(self):
        self.hashMap = [[]]

    def put(self, key: int, value: int) -> None:
        exists = False
        for i in self.hashMap:
            if i != [] and i[0] == key:
                i[1] = value
                exists = True
        if exists == False:
            self.hashMap.append([key, value])
            
    def get(self, key: int) -> int:
        for i in self.hashMap:
            if i != [] and i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in self.hashMap:
            if i != [] and i[0] == key:
                self.hashMap.remove(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)