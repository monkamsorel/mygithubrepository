import math
# question 3
"""num1= int(input("enter a first number "))
num2= int(input("enter a second number "))
num3= int(input("enter a third number "))
if num1 > num2 and num1 > num3 :
    print(num1)
elif num2 > num1 and num2 > num3 :
    print(num2)
elif num3 > num1 and num3 > num2 :
    print(num3)
else:
    print("error")
# question 4
num1 = int(input("enter a first number "))
for n in range(1,num1+1) :
    if num1 / n == num1 and num1 / num1 == 1:
        print("the number is a prime  number")
    else:
        print("the number is not a prime number")



 # question 5

num1 = int(input("enter a first number "))
m = 0
for n in range(0,num1) :
    m += n
    print(m)
def is_prime(n) :
    if n <= 1 :
        return False

    for i in range (2,int(n ** 0.5) +1):
        if n % i == 0 :
            return False
        return True

num1 = int(input("enter a number"))
if is_prime(num1):
    print(f"{num1} is a prime number")
else:
    print(f"{num1} is not a prime number")

userName = input("enter your name: ")
if len(userName) < 3:
    print("name must be at least 3 character.")
elif len(userName) > 7:
    print("name can be maximum 7 characters.")
else:
    print("name looks good!")

print("A weight conversion system")
user_weight = int(input("enter your weight: "))
user_unit = input("Choose  the unit (L)bs or (k)kg: ")
if user_unit.upper() == "L":
    converted = user_weight * 0.45
    print(f"you have {converted} kilos")
else:
    converted = user_weight / 0.45
    print(f"you have{converted} pounds")
guess_count = 0
secret = 9
guess_limitt = 3
while guess_count < guess_limitt:
    guess = int(input("guess our secret number: "))
    guess_count = guess_count + 1
    if guess == secret:
        print(" you win!")
        break
else:
     print(" sorry you loose!")
car game
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print(" Car started...")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
#start - to start the car.
#stop - to stop the car.
#quit - to exit the game.
  #      """)
"""elif command == "quit":
        break
    else:
        print("sorry, i don't understand you")"""
# for loop
num = int(input("enter a number"))
num2 = math.factorial(num)
print(num2)













