# daily_reminder.py

# Function to get task details and provide a reminder
def get_task_details():
    # Prompt the user for the task description
    task = input("Enter a task description: ")
    
    # Prompt for the task's priority
    priority = input("Enter the task's priority (high, medium, low): ").lower()
    
    # Ask if the task is time-sensitive
    time_bound = input("Is the task time-bound? (yes or no): ").lower()

    # Generate the reminder based on priority
    match priority:
        case "high":
            reminder = f"Your task '{task}' is of high priority."
        case "medium":
            reminder = f"Your task '{task}' is of medium priority."
        case "low":
            reminder = f"Your task '{task}' is of low priority."
        case _:
            reminder = "The priority level you entered is not recognized."

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " That requires immediate attention today!"

    print(reminder)

# Main program
if __name__ == "__main__":
    get_task_details()
