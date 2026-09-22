def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	portion_down_payment = 0.25
	down_payment = cost_of_dream_home * portion_down_payment
	r = 0.05
	amount_saved = 0.0
	monthly_salary = yearly_salary / 12
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while amount_saved < down_payment:
	    # Monthly investment return on the savings present at the start of the month
	    amount_saved += amount_saved * (r / 12)
	    # Additional savings contributed from this month's salary
	    amount_saved += monthly_salary * portion_saved
	    # Increment month count
	    months += 1
	
	print("Number of months:", months)
	return months