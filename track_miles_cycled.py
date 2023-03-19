from decimal import Decimal
from tracking import *

print("Hello! Welcome to the cycling tracker!")
new_miles = Decimal(input("How many miles did you cycle today? "))

def add_miles(miles, tracking.total, tracking.ride_count):
    tracking.total += miles
    tracking.ride_count += 1
    print(f"You cycled {miles} miles today, your total is {tracking.total}")
    return tracking.total, tracking.ride_count