height = float (input ("Enter the initial height of the ball: "))
bounciness_index = float (input ("Enter the bounciness index of the ball:"))
bounces_number = int (input ("Enter the number of ball bounces:"))

# Initialize the distance with initial height

total_distance = height

#Calculate the distance for each bounce

for count in range (bounces_number):
    height *= bounciness_index
    total_distance += height * 2
    print ("The total distance travelled is: ", total_distance, "ft")
