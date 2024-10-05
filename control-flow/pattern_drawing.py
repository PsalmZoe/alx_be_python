# pattern_drawing.py

# Function to draw the square pattern
def draw_pattern(size):
    row = 0  # Initialize the row counter
    while row < size:  # Continue until we reach the desired number of rows
        for col in range(size):  # Loop through each column in the current row
            print("*", end="")  # Print an asterisk without advancing to a new line
        print()  # Move to the next line after finishing the row
        row += 1  # Increment the row counter

# Main program
if __name__ == "__main__":
    # Prompt the user for the pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Validate input
    if size > 0:
        draw_pattern(size)  # Call the function to draw the pattern
    else:
        print("Please enter a positive integer.")
