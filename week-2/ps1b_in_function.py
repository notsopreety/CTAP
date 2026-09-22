def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	portion_down_payment = 0.25
	down_payment = cost_of_dream_home * portion_down_payment
	r = 0.05
	amount_saved = 0.0
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while amount_saved < down_payment:
	    # Monthly investment return on savings at the start of the month
	    amount_saved += amount_saved * (r / 12)
	    # Monthly savings from current salary
	    monthly_salary = yearly_salary / 12
	    amount_saved += monthly_salary * portion_saved
	    # Increment month count
	    months += 1
	    # Apply semi-annual salary raise at the end of every 6 months
	    if months % 6 == 0:
	        yearly_salary += yearly_salary * semi_annual_raise
	
	print("Number of months:", months)
	
	return months