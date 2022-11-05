#A data entry operator has a faulty keyboard. 
# The keys 00 and 11 are very unreliable. 
# Sometimes they work, sometimes they don't. 
# While entering phone numbers into a database, the operator uses the letter 'l' as a replacement for 1 
# and 'o' as a replacement for 00 whenever these binary digits let him down. Both 'l' and 'o' are in lower case. 
# 'l' is the first letter of the word 'land', and not capital 'i'.

#Accept a ten-digit number as input. 
# Find the number of places where the numbers 00 and 11 have been replaced by letters. 
# If there are no such replacements, print the string No mistakes. 
# If not, print the number of mistakes (replacements) and in the next line, print the correct phone number.

pno = input()
cpno = ''
count = 0
for char in pno:
    if char == 'l':
        count += 1
        cpno = cpno + '1'
    elif char == 'o':
        count += 1
        cpno = cpno + '0'
    else: 
        cpno = cpno + char

if count == 0:
    print ("No mistakes")
else: 
    print (count, "mistakes")
    print (cpno)
        