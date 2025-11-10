import math

# Ask user for input

smaller = int (input ("Enter the smaller number: "))
larger = int (input ("Enter the larger number: "))

# Calculate the maximum number of guesses using binary search formula

max_guesses = math.ceil (math.log2 (larger-smaller + 1))
print (" I can guess your number in count tries!")

low = smaller
high = larger
count  = 0

print (f"Think of a number between {smaller} and {larger}, and I will try and guess it.")

while count <= max_guesses:
    count += 1
    guess = (low + high) //2

    hint = input ("Is it too high, H ")
    hint = input ("Is it too low, L")
    hint = input ("Is it correct, C")

    if hint =='C':
                  print ("I've guessed your number {guess} in {count} tries!")
    break

    elif hint == 'H':
                      high = guess -1
    elif hint =='L':
                      low = guess +1
else:
                      print ("Invalid input! Please enter H, L or C. ")

# Detect cheating

if low > high:
    print ("Hmm...someting does not quite add up. ")
    break

                      
                      




            
