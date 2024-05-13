"""დაწერე პროგრამა რომელიც მიიღებს ორ რიცხვს მომხმარებლისგან და დაპრინტავს 
პირველი რიცხვი მეორეზე მეტია, ნაკლები თუ მისი ტოლი"""

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if num1 > num2:
    print("first number is greater than second number")
elif num1 < num2:
    print("first number is less than second number")       
else:
    print("first number equals second number")