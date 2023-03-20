from decimal import Decimal


print("Hello! Welcome to the Cycling Tracker!\n")


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

is_on = True
while is_on:
    new_miles = Decimal(input("How many miles did you cycle today? \n"))    
    add_miles(new_miles)
    again = input("Would you like to add more miles? Y or N?\n")
    if again.lower() == "y":
        continue
    else:
        is_on = False