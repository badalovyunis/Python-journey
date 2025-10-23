word = input("Enter a word: ")

length = len(word)
first_letter = word[0]
last_letter = word[-1]
upper_case = word.upper()
lower_case = word.lower()

print("\n--- Word Analysis ---")
print(f"Length: {length}")
print(f"First letter: {first_letter}")
print(f"Last letter: {last_letter}")
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")

if word.lower() == word[::-1].lower():
    print("✅ This word is a palindrome!")
else:
    print("❌ This word is not a palindrome.")