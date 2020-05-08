# Problem set 1
# Name sun
# Time spent : 3
##1
balance  = input('Enter the outstanding balance on your credit card: ')
annual_rate = input('Enter the annual credit card interest rate as a decimal: ')
payment_rate = input('Enter the minimum monthly payment rate as a decimal:')
raw = balance
totalpaid = 0.0
for i in range(1,13):
	print ('month: ' , i)
	minPayment = round(float(payment_rate) * float(balance),2)
	totalpaid += minPayment
	print ('Minimum monthly payment:  ', minPayment)
	principal_pay = round(minPayment - (float(annual_rate)* float(balance))/12,2)
	print ('Principle paid: ', principal_pay)
	print ('Remaining balance: ', float(balance) - float(principal_pay))
	balance = round(float(balance) - principal_pay,2)
print ('Total amount paid: $' , totalpaid)
print ('Remaining balance: ' , balance)


#####2.



init_balance= float(input('the outstanding balance on the credit card: ' ))
annual_interest = float(input('Enter the annual credit card interest rate as a decimal: '))

# initialize state variables
monthlyPayment = 0
monthly_rate = annual_interest / 12
balance = init_balance

# Test increasing amount of monthlyPayment in increment of $10 
#until it can pay off in a year
while balance > 0:
    	
		monthlyPayment += 10
		balance = init_balance
		numMonths = 0

		# Simulate passage of time until outstanding balance is paid off
		#Each iteration represnets 1 month	
		while numMonths < 12 and balance > 0:
    			
			# count this as a new month
			numMonths += 1

			#interest for the month
			interest = monthly_rate * balance

			#subtract monthly payment from outstanding balance
			balance -= monthlyPayment

			# add interest
			balance += interest

# round float balance to 2 decimal places
balance = round(balance,2)

print("RESULT")
print ("Monthly payment to pay off debt in 1 year:", monthlyPayment)
print ("Number of months needed:", numMonths)
print ("Balance:",balance)

#####3.
init_balance= float(input('the outstanding balance on the credit card: ' ))
annual_interest = float(input('Enter the annual credit card interest rate as a decimal: '))

monthly_rate = annual_interest / 12
balance = init_balance

lower = balance / 12
upper = (balance * (1 + (annual_interest/12))**12)/12

while True:
    balance = init_balance
    monthly_Payment = (lower+ upper)/2

    #simulate passage of tiem until outstanding balance is paid odd
    # each iteration represents 1 month

    for month in range (1,13):
        interest = round(balance * annual_interest/12,2)
        balance += interest - monthly_Payment
        if balance <= 0:
            break
    
    if(upper - lower < 0.005):
        #Bisection search space is small enough
        #print result
        print ("RESULT")

        # round monthly payment up to the nearest cent
        monthly_Payment = round(monthly_Payment + 0.0049999, 2)
        print ("Monthly payment to pay off debt in 1 year:", round(monthly_Payment,2))

        # recompute remaining balance and the numeber of months needed

        balance = init_balance
        for month in range(1,13):
            interest = round(balance*annual_interest/12,2)
            balance += interest - monthly_Payment
            if balance <= 0:
                break;
        
        print ("Number of months needed:",month)
        print ("Balance:",round(balance, 2))
        break
    elif balance < 0:
        #paying too much
        upper = monthly_Payment
    else:
        lower = monthly_Payment

    
