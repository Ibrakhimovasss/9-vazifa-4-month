from os import system 
system("cls")

class Person:
    def __init__ (self, string = ""):
        self.string = string 

    def info(self):
        return f"{self.string}"
    
    def get(self):
        self.string = input("String kiriting: ")

    def update_string(self):
        if len(self.string) > 0:
            self.string = self.string[0].upper() + self.string[1:-1] + self.string[-1].upper()


person = Person()
person.get()
person.update_string()

print(person.info())

