def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    print("Temperature Converter")
    print("Choose the temperature scale you want to convert from:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    scale = input("Enter the number (1, 2, or 3): ")

    if scale not in ['1', '2', '3']:
        print("Invalid selection. Please choose 1, 2, or 3.")
        return
    
    try:
        temp = float(input("Enter the temperature value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for the temperature.")
        return

    conversion_functions = {
        '1': lambda temp: (
            f"{temp} °C = {celsius_to_fahrenheit(temp)} °F",
            f"{temp} °C = {celsius_to_kelvin(temp)} K"
        ),
        '2': lambda temp: (
            f"{temp} °F = {fahrenheit_to_celsius(temp)} °C",
            f"{temp} °F = {fahrenheit_to_kelvin(temp)} K"
        ),
        '3': lambda temp: (
            f"{temp} K = {kelvin_to_celsius(temp)} °C",
            f"{temp} K = {kelvin_to_fahrenheit(temp)} °F"
        )
    }
    results = conversion_functions[scale](temp)
    for result in results:
        print(result)

if __name__ == "__main__":
    convert_temperature()
