# CTI-110
# P4HW3 Factorial
# Adam Klover
# 06/30/18


userNumber = int(input("Enter a number:"))

factorial = 1

while userNumber < 1:
    userNumber = int(input("Enter a positive number: "))
    
for currentNumber in range( 1, userNumber + 1):
    factorial = factorial * currentNumber

print("\nThe factorial of", userNumber, "is", factorial )
