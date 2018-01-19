Number = int(input("Please enter a Number: "))

if Number <= 127 and Number >= 0:
    print(chr(Number))
else:
    Number2 = int(input("Please enter a Number between 0 to 127, You have 1 more try : "))
    print(chr(Number2))
