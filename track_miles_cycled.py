from decimal import Decimal


print("Hello! Welcome to the Cycling Tracker!\n")
new_miles = Decimal(input("How many miles did you cycle today? \n"))

def add_miles(miles):
    total = read_miles()
    with open("tracking.txt", "w+") as track:
        try:            
            total += miles
            track.write(f"\n{total}")
            print(f"You cycled {miles} miles today, your total is {total}")
        except:           
     
            total = miles
            track.write(f"{total}")
            print(f"You cycled {miles} miles today, your total is {total}")
    return total

def read_miles():
    with open("tracking.txt", "r") as file:
        total = Decimal(file.read())
    return total

add_miles(new_miles)