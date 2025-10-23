numbers = input("Enter numbers separated by commas (e.g., 1,2,3,4): ")

total = 0
count = 0
current_num = ""
minimum = None
maximum = None

i = 0
while i < len(numbers):
    char = numbers[i]

    if char != ',':
        current_num += char
    else:
        num = int(current_num.strip())

        total += num
        count += 1

        if minimum is None or num < minimum:
            minimum = num
        if maximum is None or num > maximum:
            maximum = num

        current_num = ""  

    i += 1

if current_num != "":
    num = int(current_num.strip())
    total += num
    count += 1
    if minimum is None or num < minimum:
        minimum = num
    if maximum is None or num > maximum:
        maximum = num

average = total / count

print("\n--- Simple Statistics ---")
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
