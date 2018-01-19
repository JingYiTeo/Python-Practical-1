#Enter Information

Name = input("Please Enter Employee's Name: ")

Hours = float(input("Please Enter Weekly Working Hours: "))

Pay = float(input("Please Enter Hourly Pay Rate: "))

CPF = float(input("Please Enter CPF Contribution Rate(%): "))

#Calculation:
Gross_Pay = Hours * Pay

CPF_Contribution = ((Gross_Pay) / 100) * CPF

Net_Pay = Gross_Pay - CPF_Contribution

#Main
print("Payroll statement for {}".format(Name))
print("Number of Hours Worked in a Week: {:.1f} Hrs".format(Hours))
print("Hourly Pay Rate: ${:.2f}".format(Pay))
print("Gross Pay = ${:.2f}".format(Gross_Pay))
print("CPF Contribution at {:.2f}% = ${:.2f}".format(CPF,CPF_Contribution))
print("Net Pay = ${:.2f}".format(Net_Pay))

