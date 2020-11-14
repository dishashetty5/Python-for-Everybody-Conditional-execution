""" Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:"""
hours=input("Enter hour: ")
rate=input("enter rate: ")
try:
    hour=float(hours)
    rate=float(rate)
    if hours<=40:
        pay=hours*rate
    else:
        pay=((hours-40)*(1.5*rate))+(40*rate)
        print("pay: ",pay)
except:
    print("error,please enter numeric input")
