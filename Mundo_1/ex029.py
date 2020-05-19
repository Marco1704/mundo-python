print('The speed limit for this road is 80km/h')
velocity = float(input('What was the speed of the in km/h of the car on the radar? '))
overspeed = velocity - 80
if velocity > 80:
    print(f'You are over the approved speed limit by {overspeed:.0f}km/h \nYou will pay a fine of £{overspeed * 7:.0f}')
print('Have a nice day, drive safely.')