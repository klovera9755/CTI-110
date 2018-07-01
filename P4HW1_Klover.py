# CTI-110
# P4HW1
# Adam Klover
# 06/30/18


vehicleSpeed = float(input('What is the speed of the vehicle in mph?:'))
time = int(input('How many hours has the vehicle traveled?:'))



print('\nHour','\tMiles Traveled' )
for currentHour in range(1, time + 1):
    distanceTraveled = vehicleSpeed * currentHour
    print (currentHour,'\t',distanceTraveled )
