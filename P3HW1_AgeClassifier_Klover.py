# CTI-110 
# P3HW1 - Age Classifier 
# Adam Klover
# 06/24/18
userAge = int(input("Please enter your age."))
if userAge <=1:
    print("\n You are an infant" )
elif userAge < 13:
    print(" \nYou are a child" )
elif userAge < 20:
    print(" \nYou are a teenager" )
elif userAge >= 20:
    print(" \nYou are an adult" )
