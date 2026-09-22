## 6.100A PSet 1: Part B
## Name: Badaila Samir
## Time Spent: 20 Min
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
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

