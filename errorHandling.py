def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: Invalid argument. Please don't divide by 0.")

print(divide(10, 5))
print(divide(561435453153, 3))
print(divide(50, 0))
print(divide(400, 10))
print(divide(48, 16))