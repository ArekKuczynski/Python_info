import os



def tuple():
    import data.tuple as tuple
    t = tuple.Tuple_Class() #obiekt klasy test
    
    os.system('cls')

    while True == True:
        print("*-. Pick one .-*",end="\n\n") 
        print("1. About ( t.tuple_one() )")
        print("2. Tuples in loops ( t.tuple_two() )")
        print("3. Go back",end="\n\n")
        
        try:
            decision = input("Respond: ")
            if  decision == "1":
                os.system('cls')
                t.tuple_one()
                os.system('cls')
            if  decision == "2":
                os.system('cls')
                t.tuple_two()
                os.system('cls')
            elif  decision == "3":
                os.system('cls')
                main()
                break
            else:
                raise Exception
        except:
            os.system('cls')
            print("Error try again.")
  
def list():
    import data.list as list
    l = list.List_Class() #obiekt klasy test
    
    os.system('cls')
    
    while True == True:
        print("*-. Pick one .-*",end="\n\n") 
        print("1. About")
        print("2. Go back",end="\n\n")
        
        try:
            decision = input("Respond: ")
            if  decision == "1":
                os.system('cls')
                l.list_one()
                os.system('cls')
            elif  decision == "2":
                os.system('cls')
                main()
                break
            else:
                raise Exception
        except:
            os.system('cls')
            print("Error try again.")
                        
def main():
    print("*-. What do you want to know today? .-*",end="\n\n") 
    print("1. Tupels")
    print("2. Lists")
    print("9. Exit",end="\n\n")
    
    while True == True:
        try:
            decision = input("Respond: ")
            if  decision == "1":
                tuple()
                break
            if  decision == "2":
                list()
                break
            elif  decision == "9":
                break
            else:
                raise Exception
        except:
            print("Error try again.")

main()

