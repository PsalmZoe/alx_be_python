# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 /5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def get_temperature():
    """Prompt the user to input a valid temperature and validate it."""
    while True:
        temp_str = input("Enter the temperature to convert: ").strip()
        try:
            temperature = float(temp_str)
            return temperature
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def get_unit():
    """Prompt the user to specify whether the temperature is in Celsius or Fahrenheit."""
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            return unit
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def main():
    """Main function to handle temperature conversion based on user input."""
    temperature = get_temperature()  # Get the temperature from the user
    unit = get_unit()  # Get the temperature unit from the user

    # Perform conversion based on the user's input
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")

if __name__ == "__main__":
    main()
