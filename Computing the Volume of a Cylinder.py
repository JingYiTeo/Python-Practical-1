#Finding Volume of Cylinder

#Keying in base values: r and l
Radius = float(input("Enter Radius of Cylinder in metres"))
Length = float(input("Enter Length of Cylinder in metre"))

#Finding Volume of Cylinder
import math
Area = Radius * Radius * math.pi
Volume = Area * Length

#Printing Volume
print(Volume)
print("The Volume of Cylinder is {:.2f} Cubic metres".format(Volume))


