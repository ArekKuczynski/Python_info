import os

class Collections_Class():
    def __init__(self,main_obj):
        
        self.main = main_obj
        
        self.pick_panel()
    
    def pick_panel(self):
        os.system('cls')
        
        while True:
            print("*-. Pick one .-*",end="\n\n") 
            print("1. OrderedDict")
            print("2. DefaultDict")
            print("3. ChainMap")
            print("4. NamedTuple")
            print("5. Deque")
            print("0. Go back",end="\n\n")
            
            try:
                decision = input("Respond: ")
                if  decision == "1":
                    os.system('cls')
                    self.OrderedDict()
                    os.system('cls')
                elif  decision == "2":
                    os.system('cls')
                    self.DefaultDict()
                    os.system('cls')
                elif  decision == "3":
                    os.system('cls')
                    self.ChainMap()
                    os.system('cls')
                elif  decision == "4":
                    os.system('cls')
                    self.NamedTuple()
                    os.system('cls')
                elif  decision == "5":
                    os.system('cls')
                    self.Deque()
                    os.system('cls')
                elif  decision == "0":
                    os.system('cls')
                    self.main()
                    break
                else:
                    raise Exception
            except:
                os.system('cls')
                print("Error try again.")
                
    def OrderedDict(self):
        from collections import OrderedDict 
    
        print("This is a Dict:\n") 
        d = {} 
        d['a'] = 1
        d['b'] = 2
        d['c'] = 3
        d['d'] = 4
            
        for key, value in d.items(): 
            print(key, value) 
            
        print("\nThis is an Ordered Dict:\n") 
        od = OrderedDict() 
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4
            
        for key, value in od.items(): 
            print(key, value)
            
        #===============
        exit = input()
        os.system("cls")
        #===============
        
        od = OrderedDict() 
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4
            
        print('Before Deleting')
        for key, value in od.items(): 
            print(key, value) 
            
        # deleting element
        od.pop('a')
        
        # Re-inserting the same
        od['a'] = 1
        
        print('\nAfter re-inserting')
        for key, value in od.items(): 
            print(key, value)
        
        exit = input()
        
    def DefaultDict(self):
        from collections import defaultdict 

        # Tworzenie defaultdict z int jako domyślną fabryką
        d = defaultdict(int)

        # Dodawanie kilku kluczy i wartości
        d["a"] = 1
        d["b"] = 2
        d["c"] = 3

        # Wyświetlanie zawartości defaultdict
        print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3})

        # Próba uzyskania dostępu do nieistniejącego klucza
        print(d["d"]) # 0

        # Zauważ, że defaultdict automatycznie dodał klucz "d" z domyślną wartością 0
        print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3, 'd': 0})
        
        exit = input()
    
    def ChainMap(self):
        from collections import ChainMap 
     
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        d3 = {'e': 5, 'f': 6}
        
        # Defining the chainmap 
        c = ChainMap(d1, d2, d3) 
            
        print(c)
        # Accessing Values using key name
        print(c['a'])
        
        # Accessing values using values()
        # method
        print(c.values())
        
        # Accessing keys using keys()
        # method
        print(c.keys())
        
        
        #===============
        exit = input()
        os.system("cls")
        #===============
        
        
        # initializing dictionaries 
        dic1 = { 'a' : 1, 'b' : 2 } 
        dic2 = { 'b' : 3, 'c' : 4 } 
        dic3 = { 'f' : 5 } 
            
        # initializing ChainMap 
        chain = ChainMap(dic1, dic2) 
            
        # printing chainMap 
        print ("All the ChainMap contents are : ") 
        print (chain) 
            
        # using new_child() to add new dictionary 
        chain1 = chain.new_child(dic3) 
            
        # printing chainMap
        print ("Displaying new ChainMap : ") 
        print (chain1)
        
        exit = input()
        
    def NamedTuple(self):
        from collections import namedtuple
    
        # Declaring namedtuple() 
        Student = namedtuple('Student',['name','age','DOB']) 
            
        # Adding values 
        S = Student('Nandini','19','2541997') 
            
        # Access using index 
        print ("The Student age using index is : ",end ="") 
        print (S[1]) 
            
        # Access using name  
        print ("The Student name using keyname is : ",end ="") 
        print (S.name)  
        
        
        #===============
        exit = input()
        os.system("cls")
        #===============
        
        
        # Declaring namedtuple() 
        Student = namedtuple('Student',['name','age','DOB']) 
            
        # Adding values 
        S = Student('Nandini','19','2541997') 
            
        # initializing iterable  
        li = ['Manjeet', '19', '411997' ] 
            
        # initializing dict 
        di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
            
        # using _make() to return namedtuple() 
        print ("The namedtuple instance using iterable is  : ") 
        print (Student._make(li)) 
            
        # using _asdict() to return an OrderedDict() 
        print ("The OrderedDict instance using namedtuple is  : ") 
        print (S._asdict())   
        
        exit = input()     
    
    def Deque(self):
        from collections import deque
        
        # Declaring deque
        de = deque([1,2,3]) 
        print ("The deque example") 
        print(de)
        
        # using append() to insert element at right end  
        # inserts 4 at the end of deque 
        de.append(4) 
            
        # printing modified deque 
        print ("The deque after appending at right is : ") 
        print (de) 
            
        # using appendleft() to insert element at left end  
        # inserts 6 at the beginning of deque 
        de.appendleft(6) 
            
        # printing modified deque 
        print ("The deque after appending at left is : ") 
        print (de)
        
        # using pop() to delete element from right end  
        # deletes 4 from the right end of deque 
        de.pop() 
            
        # printing modified deque 
        print ("The deque after deleting from right is : ") 
        print (de) 
            
        # using popleft() to delete element from left end  
        # deletes 6 from the left end of deque 
        de.popleft() 
            
        # printing modified deque 
        print ("The deque after deleting from left is : ") 
        print (de)
        
        exit = input()