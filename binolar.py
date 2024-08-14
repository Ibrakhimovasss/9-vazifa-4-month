import os
os.system("cls")
#balandligi 50 dan balandlarini ekranga chiqarish

class Bino:
    def __init__ (self, height: float, color = str):
        self.height = height
        self.color = color

    def info (self):
        print(f"""
            Balandligi: {self.height}
            Rangi:       {self.color}
""")
    
#qo'lda to'ldirilgan       
p1 = Bino(455, 'Yashil')
p2 = Bino(70, "Oq")
p3 = Bino(341, "Ko'k")
p4 = Bino(24, "asfsdafd")
p5 = Bino(49.99, "ploijhugc")

binolar = [p1, p2, p3, p4, p5]

#balamdligi 50dan kottalarini ragini chiqarilgan
for bino in binolar:
    if bino.height > 50:
        print("Rangi: ",bino.color)
