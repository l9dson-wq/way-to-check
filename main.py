#My way to check the data of a variable

#We need to import the library " re " to use the function 
import re

print(
'''
dP .d888b.       dP                            
88 Y8' `88       88                            
88 `8bad88 .d888b88 .d8888b. .d8888b. 88d888b. 
88     `88 88'  `88 Y8ooooo. 88'  `88 88'  `88 
88 d.  .88 88.  .88       88 88.  .88 88    88 
dP `8888P  `88888P8 `88888P' `88888P' dP    dP
'''
)

#Function to check the data
def Verification(variable):
    check = (bool(re.search(r'\d', variable)))
    return check

#We ask the data to the user
variable = input("Type something: ")

if Verification(variable): #The function return True if the data contain numbers
    print("The data contain numbers")
else: #and False if not contain numbers
    print("the data not contain numbers")