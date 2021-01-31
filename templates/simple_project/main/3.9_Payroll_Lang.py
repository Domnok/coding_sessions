
'''This function takes user input as the number of hours worked and returns that value'''

def get_hours():
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

	return hours

'''This function takes user input as the dollar ammount paid hourly and returns that value'''

def get_pay_rate():
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
	return pay_rate
	
'''This function takes user input as federal tax as a percentage(excluding the "%")'''

def get_fed_tax_pcnt():
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

	return fed_tax

'''This function takes user input as state tax as a percentage(excluding the "%")'''

def get_state_tax_pcnt():
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
	return state_tax

'''This function calculates grosspay by multiplying hours(input) by hourly pay rate(input)'''
# def calc_gross_pay(hours, pay_rate):
def calc_gross_pay():
	gross_pay = get_hours() * get_pay_rate()
	# gross_pay = hours * pay_rate
	return gross_pay

'''This function calculates tax bill by multiplying grosspay(input) by fed and state tax rate combined value'''
# def calc_tax_bill(gross_pay, total_tax_rate):
def calc_tax_bill(gross_pay):
	tax_bill = gross_pay * (get_fed_tax_pcnt() + get_state_tax_pcnt())
	# tax_bill = gross_pay * total_tax_rate
	return tax_bill

'''This function calculates net pay by deducting the tax bill value from grosspay value'''
def calc_net_pay(gross_pay, tax_bill):
	# net_pay = calc_gross_pay() - calc_tax_bill()
	net_pay = gross_pay - tax_bill
	return net_pay

if __name__ == "__main__":

	gross_pay = calc_gross_pay()

	tax_bill = calc_tax_bill(gross_pay)
	
	net_pay = calc_net_pay(gross_pay, tax_bill)


	print('Gross Pay: ${0:.2f}'.format(gross_pay))

	print('Tax Bill: ${0:.2f}'.format(tax_bill))

	print('Net Pay: ${0:.2f}'.format(net_pay))
