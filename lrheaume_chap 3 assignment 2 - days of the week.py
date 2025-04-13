# Program to display the day of the week based on user input (1-7)

# Get user input
user_input = input("Enter a number (1-7): ")

# Convert input to an integer (if possible)
try:
    day_number = int(user_input)
except ValueError:
    print("Error: Please enter a valid integer between 1 and 7.")
else:
    # Check if the input is within the valid range
    if 1 <= day_number <= 7:
        # Display the corresponding day
        if day_number == 1:
            print("Monday")
        elif day_number == 2:
            print("Tuesday")
        elif day_number == 3:
            print("Wednesday")
        elif day_number == 4:
            print("Thursday")
        elif day_number == 5:
            print("Friday")
        elif day_number == 6:
            print("Saturday")
        elif day_number == 7:
            print("Sunday")
            
   #input ("day_number") >=7
if day_number >=7:
       print("Error: Please enter a number between 1 and 7.")
