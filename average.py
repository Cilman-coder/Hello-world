def read_numbers_from_file (filename):
    """Reads numbers from a text file and returns them as a list."""
    with open (filename, 'r') as file:
        return file.readlines ()

def compute_average (numbers):
    """Computes the  average of a list of numbers."""
    total = sum (numbers)
    count = len (numbers)
    return total / count if count > 0 else 0

def main (filename):

    # Read numbers from a specified file

    lines = read_numbers_from_file (filename)

    # Convert lines to floats, filtering non-numeric values

    numbers = list (filter (lambda x: x.strip ().replace ('.', ' ',
                                                          1).isdigit (),
                            map (str.strip, lines )))
    numbers = list (map (float, numbers))

    # Calculate the average

    average = compute_average (numbers)

    print (" The average of the numbers is: {average} ")

    if_name_ == "_main_"
    main ('numbers.txt')
