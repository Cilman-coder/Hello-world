def main ():
    # Prompt user for file name
    filename = input ("Enter the filename: ")

    # Read the file and store lines in list
    lines = []
    file_opened = False

    if filename
    with open (filename, 'r') as file:
        lines = filereadlines ()
        file_opened = True

        # Check if file opened successfully
        f file_opened:
            while True:
                print ("Number of lines in the file: {len (lines)}")

                line_number_input = input ("Enter a line number (1 to {},
                                           
                or 0 to quit: ".format (len(lines))))
        # Convert input to an integer
     if line_number_input.isdigit ():
                                           line_number = int (line_number_input)
                                           if line_number == 0
                                           print ("Exiting the program. :)
                                                  break
                                                elif 1 <= line_number <= len (lines):
        # Print the corresponding line, stripping nw line character

        
                                                    
                                print ("Line {line_number}: {lines [line_number - 1.strip ()}")
                                else:
                                    print ("Invalid line number. Please try again.")
                                    else:
                                        print ("Please enter a valid number. ")


            if _name_ == "_main_":
                main ()
