'''
Project Title

Project Date

Project Description
'''

# Input
'''Get Hours worked, Number of Hours, Pay Rate, State/Fed Tax Witholding'''
# Hours must be int

Hours = int(input("Number of Hours: "))

# Pay

Pay_Rate = float(input("Pay Rate: "))

# Federal tax withholding must be float

Fed_Tax = float(input("Enter Federal Tax Rate In Decimal: "))


# State tax withholding must be float

State_Tax = float(input("Enter State Tax Rate In Decimal: "))

if State_Tax and Fed_Tax != float:
	print("Error State_Tax and Fed_Tax Must Be Decimal Format")
	exit()



# Compute

# NetPay = (Pay_Rate * Hours) * (Fed_Tax + State_Tax)

# Gross pay: Hours * Pay

GrossPay = Hours * Pay_Rate

# TaxBill: GrossPay * (Fed_Tax + State_Tax)

TaxBill = GrossPay * (Fed_Tax + State_Tax)

# NetPay: GrossPay - TaxBill

NetPay = GrossPay - TaxBill

# Output
print("GrossPay: ")
print(GrossPay)

print("TaxBill: ")
print(TaxBill)

print("NetPay: ")
print(NetPay)
# Dispaly net pay

# Error
if State_Tax and Fed_Tax != float:
	print("Error State_Tax and Fed_Tax Must Be Decimal Format")
