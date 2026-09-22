def part_c(initial_deposit):
	#########################################################################
	cost_of_dream_home = 800000
	portion_down_payment = 0.25
	down_payment = cost_of_dream_home * portion_down_payment  # 200000
	months = 36
	tolerance = 100
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	# Edge Case 1: Initial deposit is already enough for down payment (within $100)
	if initial_deposit >= down_payment - tolerance:
	    r = 0.0
	    steps = 0
	# Edge Case 2: Impossible to reach target even with maximum 100% return rate (r = 1.0)
	elif initial_deposit * (1 + 1.0 / 12) ** months < down_payment - tolerance:
	    r = None
	    steps = 0
	else:
	    low = 0.0
	    high = 1.0
	    steps = 0
	    
	    while True:
	        r = (low + high) / 2
	        steps += 1
	        amount_saved = initial_deposit * (1 + r / 12) ** months
	        
	        # Check if amount saved is within $100 of the down payment
	        if abs(amount_saved - down_payment) <= tolerance:
	            break
	        elif amount_saved < down_payment:
	            # Need higher rate of return -> search upper half
	            low = r
	        else:
	            # Rate of return is too high -> search lower half
	            high = r
	
	print("Best savings rate:", r)
	print("Steps in bisection search:", steps)
	
	'''
	Bisection Search Explanation:
	We set the initial search bounds between low = 0.0 (0%) and high = 1.0 (100%).
	In each step, we test the midpoint rate r = (low + high) / 2 and compute amount_saved.
	If amount_saved is less than (down_payment - 100), our rate is too low, so we move right by setting low = r.
	If amount_saved is greater than (down_payment + 100), our rate is too high, so we move left by setting high = r.
	The search terminates when amount_saved falls within $100 of the required down payment.
	'''
	
	return r, steps