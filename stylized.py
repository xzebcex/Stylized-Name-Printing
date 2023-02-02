# Stylized Name Printing.

# Prompt the user to enter their name.
name = input('Enter name: ')

# Print the string "###Hello###".
#print('###Hello###')
print('Hello'.center(10, '#'))

# Iterate through each letter in the entered name.
for i in name:
    # Print each letter surrounded by asterisks.
    #print('****'+i+'****') 
    print(i.center(10, '*')) 
