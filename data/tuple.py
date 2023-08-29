class Tuple_Class:
    def __init__(self):
        self.tuple_1 = (1,'h',3,4,5,3)
    
    def tuple_one(self):
        
        
        print("tuple_1 = (1,'h',3,4,5,3)",end="\n\n")
        print("print(tuple_1) >>> ",end="")
        print(self.tuple_1,end="\n\n")
        
        print("print(tuple_1[1]) >>> ",end="")
        print(self.tuple_1[1],end="\n\n")
        
        print("print(tuple_1[1:4]) >>> ",end="")
        print(self.tuple_1[1:4],end="\n\n")
        
        print("print(len(tuple_1)) >>> ",end="")
        print(len(self.tuple_1),end="\n\n")
        
        print("print(tuple_1.count(3)) >>> ",end="")
        print(self.tuple_1.count(3),end="\n\n")
        
        print("tuple_1[0] = 5 >>> ",end="")
        print("Error",end="\n\n")
        
        exit = input()
    
    def tuple_two(self):
        
        print("Look in the code.",end="\n\n")
        
        tuple_1 = (1,"bannana",3,4,'t',3,9.24)
        
        print("Loop one:")
        
        for i in tuple_1:
            print(i)
        
        print("")
        print("Loop two:")
        
        for i in range(0,len(tuple_1)):
            print(tuple_1[i])
            
        print("")
        print("Loop three:")
        
        i = len(tuple_1) - 1
        while i >= 0:
            print(tuple_1[i])
            i-=1
        
        exit = input()