

number = int(input("Enter a Number"))

if (number >= 0) and (number <= 1000):
    print(sum(int(digit) for digit in str(number)))

else:
    print("This is not within range")

