print("Text in a line. \nText in the next line") # \n = space
print()
print("Text in a line. \n\nText in the next line") # \n\n = two spaces

print("-------------------")

tall = input("Write a whole number: ")

if tall.isnumeric(): # You can check if an input value is a whole number with isnumeric()
    print("Så bra at du skrev inn er heltall")
else: 
    print("Det du skrev var ikke en heltall")