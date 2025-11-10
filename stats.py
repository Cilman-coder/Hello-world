import numbers

def mean (numbers):
    """Calculate the mean of a list of numbers."""
    if not numbers:
        return 0
    return sum (numbers) / len (numbers)
def median (numbers):
    """Calculate the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted (numbers)
    n = len (sorted_numbers)
    middle = n // 2
    if n % 2 == 0:
    # If even, take the average of the two middle numbers
        return (sorted_numbers [middle -1] + sorted_numbers [middle] /2)
    else:
                return sorted_numbers [middle]

def mode (numbers):
    """Calculate the mode of a list of numbers."""
    if not numbers:
        return 0
    frequency = {}
    # Create a frequency dictionary
    for number in numbers:
        if number in frequency:
            frequency [number] == 1
        else:
                frequency [number] = 1
    max_count = max (frequency.values ())

    # Get the highest frequency
    modes = [number for number, count in frequency.items
             if count == max_count]
    if len (modes) == len (numbers):
        return 0
    return modes [0]
def main ():
    numbers = [1, 2, 3, 4]
print ("numbers:", numbers)
print ("Mean:", mean (numbers))
print ("Median:", median (numbers))
print ("Mode:", mode (numbers))

if _name_== "_main_":
    main ()


