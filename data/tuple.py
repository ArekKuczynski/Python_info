import os

class Tuple_Class:
    def __init__(self,main_obj):
        self.tuple_1 = (1,'h',3,4,5,3)
        self.main = main_obj

        self.pick_panel()
        
    def pick_panel(self):
        os.system('cls')

        while True:
            print("*-. Pick one .-*",end="\n\n") 
            print("1. About ( t.tuple_one() )")
            print("2. Tuples in loops ( t.tuple_two() )")
            print("0. Go back",end="\n\n")
            
            try:
                decision = input("Respond: ")
                if  decision == "1":
                    os.system('cls')
                    self.tuple_one()
                    os.system('cls')
                if  decision == "2":
                    os.system('cls')
                    self.tuple_two()
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