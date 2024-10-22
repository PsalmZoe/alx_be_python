# shopping_list_manager.py

def display_menu():
    """Displays the menu options to the user."""
    print(f"Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list."""
    shopping_list = []  # Start with an empty shopping list
    
    while True:
        display_menu()  # Show the menu options
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("No item entered. Please try again.")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
