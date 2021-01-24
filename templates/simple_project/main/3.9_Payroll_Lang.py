
# Input
'''Get Hours worked, Number of Hours, Pay Rate, State/Fed Tax Witholding'''

# Hours must be int

try: 
	hours = float(input("Number of Hours: "))

except ValueError as err:
	print("INFO: Hours must be a number")
	print('DEBUG: {0}'.format(err))
	exit()
except Exception as err:
	print("Oops!, something went wrong.")
	print('DEBUG: {0}'.format(err))
	exit() 



# Pay
try:
	pay_rate = float(input("Dollars per hour: "))
except ValueError as err:
	print("INFO: Dollars per hour must be a number.")
	print('DEBUG: {0}'.format(err))
	exit()
except Exception as err:
	print("Oops!, something went wrong.")
	print('DEBUG: {0}'.format(err))
	exit()

# Federal tax withholding must be float
try:
	fed_tax_percent = float(input("Enter Federal Tax Rate As %: "))
	fed_tax = fed_tax_percent / 100
except ValueError as err:
	print("INFO: Federal Tax Rate Must be a number greater than 0.")
	print('DEBUG: {0}'.format(err))
	exit()
except Exception as err:
	print("Oops!, something went wrong.")
	print('DEBUG: {0}'.format(err))
	exit()





# State tax withholding must be float

try:
	state_tax_percent = float(input("Enter State Tax Rate As %: "))
	state_tax = state_tax_percent / 100
except ValueError as err:
	print("INFO: State Tax Rate Must be a number greater than 0.")
	print('DEBUG: {0}'.format(err))
	exit()
except Exception as err:
	print("Oops!, something went wrong.")
	print('DEBUG: {0}'.format(err))
	exit()

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

print('Pay: {0:.2f}/Hr'.format(pay_rate))

print('Gross Pay: ${0:.2f}'.format(gross_pay))

print('Tax Bill: ${0:.2f}'.format(tax_bill))

print('Net Pay: ${0:.2f}'.format(net_pay))
# Error
'''When entering numbers with spaces error: "cd: string not in pwd: -5" '''