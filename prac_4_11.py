
# # x = 90   # Global Var
# # def fun2():
# #     # x = "Manoj"
# #     # x+="Good"
# #     global x
# #     c = x + 10
# #     print("c",c)  # 100

# #     b = 10   # Local Var
# #     x = x +  b  # 100
# #     print("x",x)    # 100

# # fun2()  
# # print("x",x) # 100

# # # print(b)   # name 'b' is not defined




# # def Mauli():
# #     def kru():
# #         return 56
# #     print('Mauli Function')
# #     return kru()  # 56


# # x = Mauli()
# # print(x)

# username = "maUli"
# password = "123"

# def login():
#     u_name = input("Enter UserName: ")
#     pass1 = input("Enter Password: ") 

#     if u_name == username and pass1 == password:
#         print("Login Successfull")
#         return 1,"Aman", (10,20)
#     else:
#         print("Cred. Invalid") 
#         return 0,"Not Valid"  


# # print(login())
# # exit()
# if login()[0] == 1:   # 1 == 1
#     print('Welcome to Zerodha Dashboard!')
# else:
#     print("Try Again")


def Aman(raina):
    def Ashok(khushi):
        print("Ashok Function")
        khushi()
    return Ashok(raina)



@Aman    # Custom Decorator
def Maulii():
    print("Mauli function")

# Aman(Maulii)


def Aman():
    print("Aman Function")

    def Ashok():
        print('Ashok Function')

    return Ashok

x = Aman()
x()