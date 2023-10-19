# # C & Cpp Code

# class Student
# {
#     int id;
#     char name[20];
#     float marks;

#     void scan_details()
#     {

#     }

#     void print_details()
#     {

#     }
# };

# struct Hospital
# {
#     int id;
#     char name[20];
#     float marks;
# };




# void main()
# {
#             int     a;
#     struct Student mauli;
            #   Bank    kru;
# }

# Constructor

# int a;


class Bank:
    ROI = 4   # Class Variable

    # Constructor-----> To intialize Memeber Variable (Auto Calling)
    def __init__(mauli, name = 'None') -> None:  #  (No return Type and Special Function)
        # Variables ------> Class Variable & Instance Variable
        mauli.name = name
        mauli.balance = 0   # Instance Variable
        # print('Constructor Called',mauli)

    # Method ---> 1. Instance Method    2. class Variable    3. Static Method
    def display(self):
        print(self.name, self.balance)


    def Deposit(self,amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    @classmethod   # Decorator
    def show_ROI(cls):    # Class Method
        print(cls.ROI)


    @classmethod
    def edit_ROI(cls,new_roi):
        cls.ROI = new_roi
        print('Rate of Interest Changed',cls.ROI)


    @staticmethod
    def faster_method():   # Faster Execution
        print('Check Rate of Interest',Bank.ROI)



vinesh = Bank()
krutarth = Bank('Krutarth')


vinesh.display()
krutarth.display()   # Instance Method


print(krutarth.Deposit(500))
print(vinesh.Deposit(5300))

print(krutarth.ROI)   # 4
print(Bank.ROI)   # 4


print(Bank.ROI)
print(vinesh.ROI)
print(krutarth.ROI)


vinesh.ROI = 9



print(Bank.ROI)
print(vinesh.ROI)
print(krutarth.ROI)

print(vinesh.Deposit(300))  # 5600

vinesh.faster_method()


Bank.ROI = 10

print(Bank.ROI)  # 10   # Class Variable
print(vinesh.ROI)  # 9    # Instance Variable
print(krutarth.ROI)  # 10   # Class Variable


krutarth.edit_ROI(45)   # Class Method
Bank.edit_ROI(45)   # Class Method

print(Bank.ROI)   # 45

Bank.faster_method()