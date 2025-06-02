# # function :-in python functions ar blocks of reuseable bloks od code that perform specific task or calculations 

# # def function_name():
#     # block of code that is use again and again
# # declearation of function
# Postational ----> sequences metter
# Keyword arguments ----> we pass key to every arguments
# default arguments --->
#       when we do not know, user pass value or not.
#       at function decleartion time

# veriable length perameters:
#     user when you do not know how many elements user pass.

# *args --> convert all arguments in tuple.
# **kwargs --> convert all keyword arguments in dictionry

# def print_something():
#     print("this is a functionnnnn codeee....")
# # -----------------------------------------------------------------------------------------------------------------
# def say_hello():
#     print("Hello, World!")

# say_hello()
# def hyy_pyhton():

#   print("this is a python function.")
#   print("you learn from the eagle eye tutorials.")

#   print("this is a python function.")
#   print("you learn from the eagle eye tutorials.")

#   print("this is a python function.")
#   print("you learn from the eagle eye tutorials.")
# # -----------------------------------------------------------------------------------------------------------------
# # Parameters are variables defined in the function signature that accept values when the function is called.

# # Arguments are the actual values you pass to the function when calling it

# def greet(name):  # 'name' is a parameter
#     print(f"Hello, {name}!")

# greet("Alice")  
# # -----------------------------------------------------------------------------------------------------------------
# # Type of perameters and arguments:
# #       1) Postational Perameters
# #       2) keyword perameters
# #       3) Default perameters
# #       4) Veriable length perameters
# #             1) *args
# #             2) **kwargs

# def abc (a,b):
#     c = a+b
#     print(c)
# abc(10,20)
# # ---------------------------------------------------------------------------------------------------------------
# def xyz(q, w, e):
#     print(f"your name is {q}, you age is {w} and you number is {e}")
# xyz("kriss moris", 20, 982346826)
# # ----------------------------------------------------------------------------------------------------------------
# #  2) keyword perameters

# def hello(x, y):
#     print(f"name {x} and age is {y}")
# hello("joe", 20)
# hello(18, "moris")
# hello(y = 18, x = "moris")
# # ----------------------------------------------------------------------------------------------------------------
# # 3) Default perameters
#     # use when you do not know, user pass value or not
# def xyz(x = 10, y = 40):
#     c = x + y
#     print(c)
# xyz(1, 6)
# # ----------------------------------------------------------------------------------------------------------------------
# # 4) Veriable length perameters
# #         1) *args
# #         2) **kwargs


# # use when you don't how many elements user pass.


# # 1) *args --> arbitrary posatioanl arguments

# def sumthis(*args):
#     print(args)
# sumthis(12, 34, 56, 34)

# # def xyz(*x):
# #     print(x)
# # xyz(34, 546, 67, 78, 90)
# # -----------------------------------------------------------------------------------------------------------------------------
# # sum calculator

# def xyz(x, y):
#     c = x + y
#     print(c)

# xyz(12, 5)
# # ---------------------------------------------------------------------------------------------------------------------
# def xyzq(*userinput):
#       # print(userinput)

#       summ = 0
#       multi = 1
#       for i in userinput:
#           summ = summ + i
#           multi = multi * i

#       print(summ)
#       print("Mutliplication is : ", multi)
    
# 2) **kwargs --> keyword arbitrary postational arguments

def userinfo(**x):
      print(x)
userinfo()
userinfo(name = "heloo", age = 20, email = "xyz@gmail.com")