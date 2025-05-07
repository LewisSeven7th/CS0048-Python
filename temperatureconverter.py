def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

while True:
    print("\nMenu:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    try:
        choice = int(choice)  

        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Temperature in Fahrenheit: {fahrenheit}")
        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Temperature in Celsius: {celsius}")
        elif choice == 3:
            break  
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Temperature converter closed.")