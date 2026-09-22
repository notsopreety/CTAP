## 6.100A PSet 1: Part A
## Name: Badaila Samir
## Time Spent: 20 Min
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
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
