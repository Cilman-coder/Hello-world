source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

with open(source_file, 'r') as infile:
        contents = infile.read()

with open(destination_file, 'w') as outfile:
        outfile.write(contents)

print("File copied successfully!")


