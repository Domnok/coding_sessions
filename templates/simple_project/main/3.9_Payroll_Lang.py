'''
Project Title

Project Date

Project Description
'''

# Input
'''Get Hours worked, Number of Hours, Pay Rate, State/Fed Tax Witholding'''

# Hours must be int

hours = int(input("Number of Hours: "))

# Pay

pay_rate = float(input("Pay Rate: "))

# Federal tax withholding must be float

fed_tax = float(input("Enter Federal Tax Rate In Decimal: "))


# State tax withholding must be float

state_tax = float(input("Enter State Tax Rate In Decimal: "))


# Compute

# NetPay = (pay_rate * Hours) * (fed_tax + state_tax)

# Gross pay: Hours * Pay

gross_pay = hours * pay_rate

# TaxBill: gross_pay * (fed_tax + state_tax)

tax_bill = gross_pay * (fed_tax + state_tax)

# NetPay: gross_pay - tax_bill

net_pay = gross_pay - tax_bill


# Output

print('Hours: {0}Hrs'.format(hours))

print('Pay: {0}/Hr'.format(pay_rate))

print('Gross Pay: ${0}'.format(gross_pay))

print('Tax Bill: ${0}'.format(tax_bill))

print('Net Pay: ${0}'.format(net_pay))

# Error