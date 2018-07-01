# CTI-110
# P4T1c snowflake
# Adam Klover
# 06/30/18
import turtle

snowflake = turtle.Turtle()
snowflake.color('cyan')

snowflake.up()
snowflake.forward(90)
snowflake.left(45)
snowflake.down()
   
def branch():
    for i in range(3):
        for i in range(3):
            snowflake.forward(30)
            snowflake.backward(30)
            snowflake.right(45)
        snowflake.left(90)
        snowflake.backward(30)
        snowflake.left(45)
    snowflake.right(90)
    snowflake.forward(90)
for i in range(8):
    branch()
    snowflake.left(45)
    
                       
    

      
