
annual_salary = float(input("how much do you make a year?"))
portion_saved = float(input("What percent of your salary would you like to save?"))
total_cost = float(input("what is the cost of your dream home?"))


portion_down_payment = (.25 * total_cost)
current_savings = 0 
r = .04 
months = 0 

while current_savings < portion_down_payment:
    current_savings = current_savings + current_savings*r/12 + portion_saved*annual_salary/12
    months += 1

print(str(months) + "months until you can buy your house")
