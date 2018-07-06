# A program to show the grade of your average
# 07/06/18
# CTI-110 P5HW1-Test average and grade
# Adam Klover

def main():
    score1 = int(input('Enter your first score: '))
    score2 = int(input('Enter your second score: '))
    score3 = int(input('Enter your third score: '))
    score4 = int(input('Enter your fourth score: '))
    score5 = int(input('Enter your fifth score: '))

    avg=calculate_average(score1, score2, score3, score4, score5)
    determine_grade(avg)
    
def calculate_average(scoreA, scoreB, scoreC, scoreD, scoreE):
       average = int((scoreA + scoreB + scoreC + scoreD + scoreE)/5)
       return average

def determine_grade(average):
        print (average)
        A_score = 90 
        B_score = 80 
        C_score = 70 
        D_score = 60 
        F_score = 50 


        score = average
 
 
        if score >= A_score: 
            print('Your grade is: A') 
        elif score >= B_score: 
            print('Your grade is: B') 
        elif score >= C_score: 
            print('Your grade is: c') 
        elif score >= D_score: 
            print('Your grade is: D') 
        elif score >= F_score: 
            print('Your grade is: F')   
main()

