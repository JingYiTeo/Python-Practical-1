#Conversion of Fahrenheit to Celsius

#Input temperature in fahrenheit
Location = input("Enter Location")
Temperature = float(input("Enter Temperature in Fahrenheit"))

#Calculate temperature in Fahrenheit
Celsius  = (5/9)*(Temperature - 32)

#Deriving the temperature
print(Celsius)
print("{0}'s Temperature is {1:2.1f} Degree Celsius".format(Location,Celsius))
