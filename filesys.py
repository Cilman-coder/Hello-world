import os

# Function to list files in the current directory
def listDirectory():
    print("\nCurrent directory:", os.getcwd())
    files = os.listdir(os.getcwd())
    for f in files:
        print(" -", f)

# Function to find files that contain a target name
def findFiles(target, path):
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(findFiles(target, os.getcwd()))
            os.chdir("..")
    return files

# Function to view a file's contents
def viewFile():
    files = os.listdir(os.getcwd())
    print("\nFiles in current directory:")
    for f in files:
        if os.path.isfile(f):
            print(" -", f)

    filename = input("\nEnter the name of the file to view: ")

    # Error recovery using if/else (no try)
    if filename in files and os.path.isfile(filename):
        infile = open(filename, "r")
        contents = infile.read()
        infile.close()
        print("\nFile contents:\n")
        print(contents)
    else:
        print("\nError: File not found or invalid filename.")

# Main program menu
def main():
    while True:
        print("\nMenu:")
        print("1) List directory")
        print("2) Find files")
        print("3) View file")
        print("4) Quit")
        command = input("Enter command number: ")

        if command == "1":
            listDirectory()
        elif command == "2":
            target = input("Enter the file name or part of it to find: ")
            found = findFiles(target, os.getcwd())
            if len(found) > 0:
                print("\nFiles found:")
                for f in found:
                    print(" -", f)
            else:
                print("\nNo matching files found.")
        elif command == "3":
            viewFile()
        elif command == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1-4.")

# Run the program
main()
