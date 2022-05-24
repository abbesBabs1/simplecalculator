# A simple calculator

name = input("Enter Your name: ")
var_1 = int(input("Enter Your first_score: "))
var_2 = int(input("Enter Your second_score: "))
operators = input("Enter Arithmetic Operators: ")

if operators == "+":
    print("Dear "+name + " The RESULT of your addition is " +str(float(var_1) + float(var_2)))
elif operators == "-":
    print("Dear "+name + " The RESULT of your subtraction is " + str(float(var_1) - float(var_2)))
elif operators == "*":
    print("Dear "+name + " The RESULT of your multiplication is " + str(float(var_1) * float(var_2)))
elif operators == "/":
    print("Dear "+name + " The RESULT of your division is " + str(float(var_1) / float(var_2)))
elif operators == "//":
    print("Dear "+name + " The Result of your floor division is " + str(float(var_1) // float(var_2)))








































































