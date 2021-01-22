'''
Project Title

Project Date

Project Description
'''

# Input
'''Get Hours worked, Number of Hours, Pay Rate, State/Fed Tax Witholding'''
# Hours must be int

Hours = input(int("Number of Hours: "))

# Pay must be int

Pay_Rate = input(int("Pay Rate: "))

# Federal tax withholding must be float

Fed_Tax = input(float("Enter Federal Tax Rate In Decimal: "))

# State tax withholding must be float

State_Tax = input(float("Enter Federal Tax Rate In Decimal: "))


# Compute

# NetPay = (Pay_Rate * Hours) * (Fed_Tax * State_Tax)

# Gross pay: Hours * Pay

GrossPay = Hours * Pay_Rate

# TaxBill: GrossPay * (Fed_Tax + State_Tax)

TaxBill = GrossPay * (Fed_Tax + State_Tax)

# NetPay: GrossPay - TaxBill

NetPay = GrossPay - TaxBill

# Output
print("GrossPay: " GrossPay)

print("TaxBill: " TaxBill)

print("NetPay: " NetPay)

# Dispaly net pay
