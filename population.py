population = int (input ("Enter the initial number of organisms: "))
growth_rate = int (input ("Enter the growth rate [a real number >0]: "))
growth_hours = int ( input ("Enter the total number of hours to achieve growth: "))
total_hours = int (input ("Enter the total number of hours of growth: "))

#Initialize the rate of growth to be greater than 0

total_population = population
while growth_hours>= total_hours:
    population *= growth_rate
    total_population += population
    growth_hours += growth_hours

# Print the result

print ( "The total populaton is ", total_population, )
