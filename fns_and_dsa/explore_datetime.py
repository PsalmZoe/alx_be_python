# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    """Display the current date and time in the format 'YYYY-MM-DD HH:MM:SS'."""
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it as 'YYYY-MM-DD HH:MM:SS'
    print(f"Current date and time: {formatted_date}")
    return current_date  # Returning current date for future use

# Part 2: Calculate a Future Date
def calculate_future_date(current_date, days_to_add):
    """Calculate and display the future date after adding days_to_add to current_date."""
    future_date = current_date + timedelta(days=days_to_add)  # Add the specified number of days
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format it as 'YYYY-MM-DD'
    print(f"Future date: {formatted_future_date}")
    return future_date  # Return the future date if needed

def main():
    # Part 1: Display the current date and time
    current_date = display_current_datetime()

    # Part 2: Prompt user for number of days to add and calculate the future date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
