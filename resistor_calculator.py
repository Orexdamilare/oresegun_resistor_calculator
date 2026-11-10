# RESISTOR COMBINATION CALCULATOR
# Developed by ORESEGUN OLUWADAMILARE VICTOR

# Function to calculate resistance in series
def calculate_series(resistors):
    return sum(resistors)


# Function to calculate resistance in parallel
def calculate_parallel(resistors):
    total = 0

    for resistance in resistors:
        total += 1 / resistance

    return 1 / total


# Function to calculate current using Ohm's Law
def calculate_current(voltage, resistance):
    return voltage / resistance


# Function to display results
def display_results(series, parallel, voltage):
    print("\n========== CALCULATION RESULTS ==========")

    print(f"Total resistance in series: {series:.2f} ohms")
    print(f"Total resistance in parallel: {parallel:.2f} ohms")

    series_current = calculate_current(voltage, series)
    parallel_current = calculate_current(voltage, parallel)

    print(f"Current in series: {series_current:.2f} A")
    print(f"Current in parallel: {parallel_current:.2f} A")

    print("=========================================")


# Main program
print("=========================================")
print("       RESISTOR COMBINATION CALCULATOR")
print("=========================================")

print("\nThis program calculates resistance in")
print("series and parallel combinations.")

name = input("\nEnter your name: ")

print("\nWelcome,", name)

while True:
    try:
        number = int(input("\nHow many resistors do you want to use? "))

        if number >= 2:
            break
        else:
            print("Please enter at least 2 resistors.")

    except ValueError:
        print("Invalid input. Enter a whole number.")


# List for storing resistor values
resistors = []

for i in range(number):
    while True:
        try:
            resistance = float(
                input(f"Enter resistance of resistor {i + 1} (ohms): ")
            )

            if resistance > 0:
                resistors.append(resistance)
                break
            else:
                print("Resistance must be greater than zero.")

        except ValueError:
            print("Invalid input. Enter a numerical value.")


# Calculate total resistance
series_resistance = calculate_series(resistors)
parallel_resistance = calculate_parallel(resistors)


# Ask for supply voltage
while True:
    try:
        voltage = float(input("\nEnter supply voltage (V): "))

        if voltage > 0:
            break
        else:
            print("Voltage must be greater than zero.")

    except ValueError:
        print("Invalid input. Enter a numerical value.")


# Display calculation results
display_results(
    series_resistance,
    parallel_resistance,
    voltage
)


# Allow the user to calculate again
while True:
    choice = input("\nWould you like to calculate again? (yes/no): ").lower()

    if choice == "yes":
        print("\nPlease restart the program to perform another calculation.")
        break

    elif choice == "no":
        print("\nThank you for using the Resistor Combination Calculator.")
        break

    else:
        print("Invalid choice. Please enter yes or no.")