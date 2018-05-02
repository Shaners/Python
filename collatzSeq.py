def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

while True:
    try:
        print("Please provide a number.")
        num = int(input('> '))
    except ValueError:
        print("Error: Invalid argument. You did not provide a number.")
        continue
    else:
        break

while collatz(num) != 1:
    print(collatz(num))
    num = collatz(num)

print(collatz(num))