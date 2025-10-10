num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"\n--- Before swapping ---")
print(f"First number: {num1}")
print(f"Second number: {num2}")

temp = num1
num1 = num2
num2 = temp

print(f"\n--- After swapping ---")
print(f"First number: {num1}")
print(f"Second number: {num2}")