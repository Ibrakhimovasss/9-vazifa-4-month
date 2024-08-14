from os import system
system ("cls")
from colorama import Fore
#listti oxiridan elementni list bn o'chirirish

class List:
    def __init__ (self, lst):
        self.lst = lst
    
    #o'chirishga alohida metod yozvotti, pop oxiridan X qilad
    def delate(self):
        if self.lst:
            self.lst.pop()
        else:
            print(Fore.RED + "List bo'sh! :(")

lst = [10, 34, 5, 234, 542, 63, 45]
natija = List(lst)

print(Fore.BLUE + "Eski list :" , natija.lst)

natija.delate()
print(Fore.CYAN + "Yengi list : ", natija.lst)