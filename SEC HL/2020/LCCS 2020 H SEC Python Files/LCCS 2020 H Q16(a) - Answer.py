# Question 16(a)
# Examination Number:

# Prompt the user to enter a password and store the ...
# value entered in the variable password
password = input("Enter a password: ")

# A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #(iii)
DIGITS = "0123456789" #(v)

# The variables lowercase and uppercase indicate the presence or ...
# absence of lowercase and uppercase characters in the password
lowercase = False # True if password contains a lowercase letter
uppercase = False # True if password contains an uppercase letter
digits = False #(v)

# Loop through each character in the password and ...
# check the password for specific characters
for character in password:
    if character in LOWER_CASE_LETTERS:
        lowercase = True
    if character in UPPER_CASE_LETTERS:
        uppercase = True
    if character in DIGITS: #(v)
        digits = True #(v)

# Calculate the score based on the rules

score = 0 #initialise score (i)

# Rule 1
if len(password) > 7:
    score = score + 5
elif len(password)<=7 and len(password)>=4:
    score = score + 2
else:
    score = score - 2

# Rule 2
if lowercase:
     score = score + 1

# Rule 3
if lowercase and uppercase:
     score = score + 5

# Rule 4 (iv)
if uppercase:
    score = score + 2

# Rule 5 (v)
if digits:
    score = score + 5

# Rule 6 (vi)
if password[0] in DIGITS: #This checks the first value in password
    score = score + 1
if password[-1] in DIGITS: # This check last value in password
    score = score + 1
if password[0] in DIGITS and password[-1] in DIGITS: # This checks both first and last
    score = score + 2

# Rule 7 (vii)

if digits and not lowercase and not uppercase: #Checks in they are all digits
    score = score - 10

# Display the score
#(ii)
print(f'Password: {password}')
print(f'Score: {score}')