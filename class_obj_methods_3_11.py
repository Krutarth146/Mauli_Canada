class Bank():
    ROI = 3.5
    __bank_assets = 30000000000000000000   # Private Variable


    def __init__(self, full_name):   # Constuctor
        self.name = full_name  # Public
        self.balance = 0
        self._cheque_no = 506   # Protected Variable


    def Deposit(self, amount):
        if amount > 0 and amount<=50000:
            self.balance += amount
            print("Amount Deposited....",self._cheque_no)

    def show_details(self):
        print(self.name, self.balance)


mauli = Bank("Mauli Shah")
ama = Bank("Aman Patel")

mauli.Deposit(4000)

# mauli.show_details()   # None 4000

# print(ama.ROI)   # 3.5
# print(mauli.ROI)   # 3.5

# Bank.ROI = 4   # Class Variable

# print(ama.ROI)  # 4

print(mauli._cheque_no)   # 4

# print(Bank.__bank_assets)  # Error

print(Bank._Bank__bank_assets)   # 30000000000000000000