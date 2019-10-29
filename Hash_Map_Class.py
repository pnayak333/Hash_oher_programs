class Hash_Tabel:
    def __init__(self):
        self.size = 10
        self.Hash_Map = [None] * self.size
        #self.Hash_Map = [[] for _ in range(0,self.size)]
        #self.Hash_Map = [None] * self.size

        print(self.Hash_Map)
    def get_Hash(self,key):
        Key_Number = 0
        for char in str(key):
            Key_Number = Key_Number + ord(char)
        return Key_Number % self.size

    def add(self,key,value):
        key_hash = self.get_Hash(key)
        key_value = [key,value]
        if self.Hash_Map[key_hash] is None:
            self.Hash_Map[key_hash] = list([key_value])
            return  True
        else:
            for k in self.Hash_Map[key_hash]:
                if k[0] == key:
                    k[1] = value
                    return True
            self.Hash_Map[key_hash].append([key_value])
            #return True
    def get_Hash_Index(self,key):
        key_hash = self.get_Hash(key)
        if self.Hash_Map[key_hash] is not None:
            for inner_key in self.Hash_Map[key_hash]:
                if inner_key[0] == key:
                    return inner_key[1]
            #return False

    def delete_Key(self,key):
        hash_key = self.get_Hash(key)
        if self.Hash_Map[hash_key] is None:
            return False
       #if self.Hash_Map[hash_key] is not None:


        for inner_key in range(0,len(self.Hash_Map[hash_key])):
            if self.Hash_Map[hash_key][inner_key][0] == key:
                    self.Hash_Map[hash_key].pop(inner_key)
                    return True

    def display(self):
        print("-------------Values-------")
        for item in self.Hash_Map:
            if item is not None:
                print(str(item))


obj = Hash_Tabel()
obj.add("Prashanth","111")
obj.add("Vasanthkumar","112")
obj.add("Sibi","113")
obj.add("Anthonay","114")
obj.add("aaa","111")
obj.add("bbb","112")

obj.add("Mukundans","11511")
obj.add("Mukundans","116")
obj.add("Mukundans","116444")
obj.add("Vasanthkumar","112222")
obj.display()
print('-------------------------After Deletion---------------------------')
obj.delete_Key("Sibi")
obj.display()