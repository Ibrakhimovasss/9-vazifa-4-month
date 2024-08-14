import os
os.system("cls")
#laptoplarni hamma ma'lumotlarini print qilish

class Laptop:
    def __init__ (self, firma: str, model = str, CPU = str, DDR = str, price = float):
        self.firma = firma
        self.model = model
        self.CPU = CPU
        self.ddr = DDR
        self.price = price

    def info (self):
        print(f"""***{self.model}***
        Firm :  {self.firma}
        CPU :   {self.CPU}
        DDR :   {self.ddr}
        Price : {self.price} $
            
""")
    
#qo'lda to'ldirilgan       
p1 = Laptop("Dell", "XPS 13 9310","Intel Core i7-1185G7", "16 GB LPDDR4x" , 1299)
p2 = Laptop("Apple", "MacBook Air (M2, 2022)", "Apple M2", "8 GB Unified Memory", 1199)
p3 = Laptop("Lenovo", "ThinkPad X1 Carbon (9th Gen)", "Intel Core i7-1165G7","16 GB LPDDR4x", 1499 )
p4 = Laptop("HP", "Spectre x360 14", "Intel Core i7-1255U", "16 GB LPDDR4x", 1249)
p5 = Laptop("Asus", "ROG Zephyrus G14", "AMD Ryzen 9 6900HS", "32 GB DDR5", 1699)

#info metod qilib olingan ekranga chiqarish uchun
p1.info()
p2.info()
p3.info()
p4.info()
p5.info()

