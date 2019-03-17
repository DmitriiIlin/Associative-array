import Associativearray_mod,unittest,random,string

def string_generator(size=8):
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def data_generator(a=1,b=10000):
    number=random.randint(a,b)
    return number

class Hash_table_Tests(unittest.TestCase):

    def test_hash_fun(self):
        #Проверка метода генерации хеша, hash_fun 
        size=19
        input_string=string_generator()
        sum_1=sum(ord(input_string[i])**(i+1) for i in range(len(input_string)))% size
        hash_for_test=Associativearray_mod.NativeDictionary(size)
        self.assertEqual(sum_1,hash_for_test.hash_fun(input_string))



if __name__='__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()
