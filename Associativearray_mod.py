import string,random

class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве value поступают строки!
        input_string=str(key)
        index=sum(ord(input_string[i])**(i+1) for i in range(len(input_string)))%self.size
        return index

    def is_key(self, key):
         # возвращает True если ключ имеется,
         # иначе False
        key=str(key)
        flag=False
        for i in range(len(self.slots)):
            if self.slots[i]==key:
                flag=True
                return flag
            else:
                i+=1
        if flag==False:
            return flag

    def put(self, key, value):
        # гарантированно записываем 
        # значение value по ключу key

        if None in self.slots and value!=None:
            index=self.hash_fun(key)
            while self.slots[index]!=None:
                if index<self.size-1:
                    index+=1
                else:
                    index=0
            self.slots[index]=str(key)
            self.values[index]=value
        else: 
            pass
         

    def get(self, key):
        # возвращает value для key, 
        # или None если ключ не найден
        key=str(key)
        if self.is_key(key)==True:
            for index in range(len(self.slots)):
                if self.slots[index]==key:
                   # data.append(self.slots[index])
                    data=self.values[index]
                index+=1
            return data
        else:
            return None


    






