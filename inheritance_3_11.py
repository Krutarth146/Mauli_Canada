class Alto():   # Parent Class
    def __init__(self, small_price):
        print('Alto Class Const.')
        self.small_price = small_price


    def seats(self):
        print('There are 4 Seats',self.small_price)

    def Brake(self):
        print("Alto Brake System")

 
class Innova(Alto):   # Child Class
    def __init__(self, price, small_price):
        super().__init__(small_price)
        print("Innova Class Constructor",price)

    def Airbag(self):
        print('There are 4 airbags')

    def safety_Features(self):
        print("Good Safety Fea.")


# class Ferrari(Innova):
#     def Sensors(self):
#         print("Many Sensors")


# a1 = Alto()
# a1.seats()


i1=  Innova(1000000, 350000)
# i1.Airbag()
i1.seats()

# f1 = Ferrari()

# f1.Brake()
# f1.Airbag()