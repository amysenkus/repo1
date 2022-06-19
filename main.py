
# Online Python - IDE, Editor, Compiler, Interpreter

class Shark:  #defining class Shark
    def __init__(self, name):  #initializing self, name
        self.name = name

    def swim(self):  #defining the function swim
        print(self.name + " is swimming.")  #excecuted code 

    def be_awesome(self):  #defining the function be_awesome
        print(self.name + " is being awesome.")  #excecuted code


def main():  #defining the main program loop
    # Set name of Shark object
    sammy = Shark("Sammy")  #setting the shark name
    sammy.swim()  #calling the function swim
    sammy.be_awesome()  #calling the function be_awesome

if __name__ == "__main__":
    main() #runs the main loop
    
def main():  #defining the main program loop
    # Set name of Shark object
    Amy = Shark("Amy") #setting the shark name 
    Amy.swim()  #calling the function swim
    Amy.be_awesome()  #calling the function be_awesome

if __name__ == "__main__":
    main()