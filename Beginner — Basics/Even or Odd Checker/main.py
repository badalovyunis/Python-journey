def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    print("=== Even or Odd Checker ===")
    choice = input("Check a single number or multiple numbers?: ").lower()

    if choice == "single":
        try:
            num = int(input("Enter a number: "))
            print(f"{num} is {check_even_odd(num)}")
        except ValueError:
            print("Error: Please enter a valid integer!")

    elif choice == "multiple":
        try:
            nums = input("Enter numbers separated by space: ").split()
            nums = [int(n) for n in nums]
            for n in nums:
                print(f"{n} is {check_even_odd(n)}")
        except ValueError:
            print("Error: Please enter valid integers!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
