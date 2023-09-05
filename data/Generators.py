import os

class Generators_Class():
    def __init__(self,main_obj):
        
        self.main = main_obj
        
        self.pick_panel()
    
    def pick_panel(self):
        os.system('cls')
        
        while True:
            print("*-. Pick one .-*",end="\n\n") 
            print("1. Example")
            print("2. Infinite Generator")
            print("3. Yield from")
            print("4. List and Generator comprehension")
            print("5. List vs Generator")
            print("0. Go back",end="\n\n")
            
            try:
                decision = input("Respond: ")
                if  decision == "1":
                    os.system('cls')
                    self.example()
                    os.system('cls')
                elif  decision == "2":
                    os.system('cls')
                    self.infinite_Generator()
                    os.system('cls')
                elif  decision == "3":
                    os.system('cls')
                    self.yield_from()
                    os.system('cls')
                elif  decision == "4":
                    os.system('cls')
                    self.comprehension()
                    os.system('cls')
                elif  decision == "5":
                    os.system('cls')
                    self.list_vs_generator()
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
    def example(self):
        def generator():
            yield "First iteration"
            
            return "Iteration stoped"

        gen_1 = generator()
        print(next(gen_1))
        #print(next(gen_1))

        def generator2():
            yield "one"
            yield "two"
            yield "three"
            yield "four"
            yield "five"

        for i in generator2():
            print(i)
        
        #===============
        exit = input()
        os.system("cls")
        #===============
    
    def infinite_Generator(self):
        #This generator never ends. : "StopIteration"

        from itertools import islice

        def infinite_generator():
            i = 0
            while True:
                yield i
                i += 1
                
        gen1 = infinite_generator()

        cut = input("How much do you want to take from generator?: ")
        list_1 = islice(gen1, int(cut))
        print(list(list_1))

        other_cut = islice(gen1,10,20,3)
        print(list(other_cut))
        print("When we decide to extract data from the generator again, we do not start from the beginning but from the end of the previous iteration")
        
        #===============
        exit = input()
        os.system("cls")
        #===============
        
    def yield_from(self):
        def generator1(it1, it2):
            yield from it1
            yield from it2
            
        gen1 = generator1(range(3), "test")
        print(list(gen1))
        
        #===============
        exit = input()
        os.system("cls")
        #===============
        
    def comprehension(self):
        def example():
            list_1 = [2 ** i for i in range(20)]
            gen_1 = (2 ** i for i in range(20))
            
            print(list_1)
            
            for i in gen_1:
                print(i, end=", ")

        example()
        
        #===============
        exit = input()
        os.system("cls")
        #===============
        
    def list_vs_generator(self):
        #bezpośrednie porównanie generatora z listą

        class Example_1():
            def __init__(self):
                pass
            
            def simple_range(self,dec):
                def generator(x):
                    i = 0
                    while i < x:
                        yield i
                        i += 1
                        
                def list_1(x):
                    i = 0
                    wynik = []
                    while i < x:
                        wynik.append(i)
                        i += 1
                    return wynik
                
                
                def decider():
                    if dec == "1":
                        print("Generator")
                        for i in generator(99999999):
                            if i != 0 and i % 123 == 0 and i % 401 == 0 and i % 589 == 0:
                                print(i)
                    else:
                        print("List")
                        for i in list_1(99999999):
                            if i != 0 and i % 123 == 0 and i % 401 == 0 and i % 589 == 0:
                                print(i)
                        
                
                decider()
                    

        exampl = Example_1()

        print("Select options to find numbers on complex terms:")
        print("1. Generator (do math)")
        print("2. List (set your computer on fire)")
        decision = input("Pick: ")
        if decision == "1":
            exampl.simple_range("1")
        else:
            exampl.simple_range("2")
            
        print("What is the difference?")
        print("The list is first created and then returned, which means that each number is added to the list.")
        print("We are unnecessarily trying to generate unnecessary numbers, of which there are many in this case.")

        #===============
        exit = input()
        os.system("cls")
        #===============
