code = input ("Enter a line of code: ")
distance = int (input ("Enter the distance value: "))

    
import string

printable = string.printable

# Get inputs

code = input ("Enter the message to decrypt: ")
distance = int(input("Enter the distance value: "))
plainText = ""
for ch in plainText:
    if ch in printable:
        # Shift character by distance
        new_index = (printable.index(ch)- distance) % len (printable)
        code += printable [new_index]
    else:
        code += ch
        print ("Decrypted message:", plainText)
