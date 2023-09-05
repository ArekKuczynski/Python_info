import os


class Main():
    def __init__(self):
        self.main()
    
    def main(self):
        print("*-. What do you want to know today? .-*",end="\n\n") 
        print("1. Tupels")
        print("2. Lists")
        print("3. Collections")
        print("4. Generators")
        print("0. Exit",end="\n\n")
        
        while True:
            try:
                decision = input("Respond: ")
                if  decision == "1":
                    self.tuple()
                    break
                elif  decision == "2":
                    self.list()
                    break
                elif  decision == "3":
                    self.collections()
                    break
                elif  decision == "4":
                    self.generators()
                    break
                elif  decision == "0":
                    break
                else:
                    raise Exception
            except:
                print("Error try again.")
    
    def tuple(self):
        import data.Tuple as Tuple
        Tuple.Tuple_Class(self.main)
    
    def list(self):
        import data.List as List
        List.List_Class(self.main)
        
    def collections(self):
        import data.Collections as Col
        Col.Collections_Class(self.main)
        
    def generators(self):
        import data.Generators as Gen
        Gen.Generators_Class(self.main)


if __name__ == '__main__':
    main_app = Main()

