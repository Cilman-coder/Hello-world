
import string

printable = string.printable

# Get inputs

plainText = input ("Enter the message to encrypt: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    if ch in printable:
        # Shift character by distance
        new_index = (printable.index(ch)+ distance) % len (printable)
        code += printable [new_index]
    else:
        code += ch
        print ("Encrypted message:", code)
            
