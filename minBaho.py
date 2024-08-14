import os
os.system("cls")

class Book:
    def __init__ (self, name: str, surname: str, grade = int):
        self.name = name
        self.surname = surname
        self.grade = grade

    
    def info (self):
        print(f"""
            ***{self.name}***
            Familiya : {self.surname} 
            BAho:      {self.grade}

""")
        
p1 = Book("Baxtiyor", "Ibroximov", 4)
p2 = Book("Bobur", "Ibroximov", 3)
p3 = Book("Nurmuhammad", "Ibroximov", 5)

odamlar = [p1, p2, p3]


min = odamlar[0]
for odam in odamlar[1:]:
    if odam.grade < min.grade:
        min = odam

min.info()