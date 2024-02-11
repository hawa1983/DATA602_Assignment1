#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95  # High score threshold
 
# Get the test scores.
test1 = input('Enter the score for test 1: ') # Get the test scores as integer
test2 = input('Enter the score for test 2: ') # Get the test scores as integers

# test3 is needed to calculate the average
test3 = int(input('Enter the score for test 3: '))  # Added missing test3 input

# Calculate the average test score.
# Calculate the average test score correctly by summing all scores before dividing
# This is done by placing sum in parenthesis
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)

# Check if the average is a high score and congratulate the user.
# Variables are case sensitive. By convention, constant variables are uppercased.
if average >= HIGH_SCORE:  # Corrected variable name to match the constant's name.
    print('Congratulations! That is a great average!') # The print statements can be combined.


#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

# Ask for dimensions of rectangle 1
length_rectangle1 = float(input("Enter the length of rectangle 1: "))
width_rectangle1 = float(input("Enter the width of rectangle 1: "))

# Calculate area of rectangle 1
area_rectangle1 = length_rectangle1 * width_rectangle1

# Ask for dimensions of rectangle 2
length_rectangle2 = float(input("Enter the length of rectangle 2: "))
width_rectangle2 = float(input("Enter the width of rectangle 2: "))

# Calculate area of rectangle 2
area_rectangle2 = width_rectangle2 * width_rectangle2

# Print the areas
print(f"The area of rectangle 1 is: {area_rectangle1}")
print(f"The area of rectangle 2 is: {area_rectangle2}")

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  
name = input("Enter your first name: ")
age = int(input("Enter your age: "))  # Convert age to integer

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
print(f"Happy birthday, {name}! You are {age} years old today!")

