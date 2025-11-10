# Get the purchase price from the  user

purchase_price = float (input ("Enter the purchase price: "))

# Constants

down_payment_rate = 0.10 # 10% down payment
annual_interest_rate = 0.12 # 12% annual interest
monthly_payment_rate = 0.05 # 5% of purchase price

# Calculate down payment and initial balance

down_payment = purchase_price * down_payment_rate
balance = purchase_price - down_payment
monthly_payment = purchase_price * monthly_payment_rate

#Print table headers

print (f"{'Month' :<6} {'Balance':<12} {'Interest':<12} {'Principal':<12}
       {'Payment':<12} {'Remaining':<12}")
       
print ("-" * 70)                      

                        month = 1

# Loop until the balance is paid off
                        while balance >0:
                            
# Calculate interest for this month

interest = balance * annual_interest_rate /12

# Calculate principal

principal = monthly_payment - interest

# Remaining balance after payment

balance -= principal

# Print current months details

print (f"{month: <6} {balance + principal: <12.2f} {interest:<12.2f}
       month += 1



                        
       
