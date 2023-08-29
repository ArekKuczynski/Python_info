class List_Class:
    def __init__(self):
        self.list_1 = ["apple",1,'b',6,3,4,9,]
    
    def list_one(self):
        
        
        print(self.list_1,end="\n\n")
        
        print(self.list_1[4])
        print(self.list_1[4:6])
        print(len(self.list_1))
        
        self.list_1[0] = "ananas"
        print(self.list_1)
        
        exit = input()
    def list_sorted(self):
        pass