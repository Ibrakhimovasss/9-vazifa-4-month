from os import system
system ("cls")
from colorama import Fore
#listti boshiidan elementni list bn o'chirirish

class List:
    def __init__ (self, lst):
        self.lst = lst
    
    #o'chirishga alohida metod yozvotti, pop ga qiymat berse usha indeksidagini X qilad
    def brand_exists(self, lst):
       return lst in self.lst

lst = ["Kia", "BMW", "Mers", "Chevrolet", "BYD"]
natija = List(lst)

print(Fore.BLUE + str(natija.brand_exists('BMW')))

print(Fore.RED + str(natija.brand_exists('tayota')))