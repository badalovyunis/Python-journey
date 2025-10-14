def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    print("=== Temperature Converter ===")
    scale = input("Enter the scale you want to convert from (C/F): ").upper()

    try:
        temp = float(input("Enter the temperature: "))

        if scale == "C":
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")

        elif scale == "F":
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")

        else:
            print("Error")

    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
