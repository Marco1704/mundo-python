distance = float(input('Enter the total number of kilometers: '))
day_rented = int(input('Enter the total number of rented days: '))
cost_distance = distance * 0.15
cost_days = day_rented * 60
total_cost = cost_days + cost_distance
print(f'The car was rented for {day_rented} days and runned over {distance:.0f}km with total cost of £{total_cost:.2f}')