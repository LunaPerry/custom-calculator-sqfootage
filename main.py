number_of_rooms = 0

room_length = 0
room_width = 0
sum_area = 0
x = 0 #used to manipulate the while loop

#Gather number of rooms to use to break out of while loop
number_of_rooms = int(input("How many rooms are in your house? "))

#While loop gathers inputs for length/width of all rooms and calculates total area in inches
while x < number_of_rooms:
    room_length = int(input("What is the length of the room in inches? "))
    room_width = int(input("What is the width of the room in inches? "))
    
    sum_area = sum_area + (room_length * room_width)
    debug_message = f"Your total area is {sum_area} inches"
    print(debug_message)
    x += 1

#convert area from inches to feet and prints
sum_area /= 144
print(f"Your house is {sum_area} square feet!")