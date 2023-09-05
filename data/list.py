import os

class List_Class:
    def __init__(self,main_obj):
        self.list_1 = ["apple",1,'b',6,3,4,9,]
        self.main = main_obj

        self.pick_panel()
        
    def pick_panel(self):
        os.system('cls')
        
        while True:
            print("*-. Pick one .-*",end="\n\n") 
            print("1. About")
            print("0. Go back",end="\n\n")
            
            try:
                decision = input("Respond: ")
                if  decision == "1":
                    os.system('cls')
                    self.list_one()
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