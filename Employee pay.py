
hourly_wage = float (input ( "Enter employee hourly wage: ")) 

regular_hours = float (input ("Enter the total regular hours worked: ")) 

overtime_hours = float (input ("Enter the total overtime hours worked: ")) 

# computer the overtime pay 

overtime_pay = regular_hours * hourly_wage * 1.5 * overtime_hours 

# compute total weekly pay 

weekly_pay = (regular_hours * hourly_wage) + overtime_pay

# Print total pay 

print ( " The total weekly pay is: ", weekly_pay , "dollars")
