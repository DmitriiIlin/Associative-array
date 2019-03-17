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
        if None in self.slots:
            index=self.hash_fun(key)
            while self.slots[index]!=None:
                if index<self.size-1:
                    index+=1
                else:
                    index=0
        self.slots[index]=str(key)
        self.values[index]=value

    def get(self, key):
        # возвращает value для key, 
        # или None если ключ не найден
        data=[]
        key=str(key)
        if self.is_key(key)==True:
            for index in range(len(self.slots)):
                if self.slots[index]==key:
                    data.append(self.slots[index])
                    data.append(self.values[index])
                index+=1
            return data
        else:
            return None

a=NativeDictionary(23)
size=8
st_massive=[]
number_massive=[]
chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
for i in range(23):
    st=''.join(random.choice(chars) for j in range(size))
    st_massive.append(str(st))
    a.put(st,random.randint(1,1000))
print(a.slots)
print(a.values)
for i in range(len(a.slots)):
    print(a.get(a.slots[i]))


