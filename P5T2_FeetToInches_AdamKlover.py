# This project I will convert feet into inches
# 07/06/18
# CTI-110 P5T2_FeetToInches
# Adam Klover


INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter a number in feet: '))

    print(feet, 'equals', feet_to_inches(feet), "inches.")

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
main()
