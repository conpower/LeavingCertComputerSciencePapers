# Question 16(b)
# Examination Number:

# A variable to store all the lower case letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

def is_strong(password): #(iv)
    strong = False
    
    lowerscore = False
    uppercase = False
    
    for character in password:
        if character in LOWER_CASE_LETTERS:
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPKRSTUVWXYZ":
            uppercase = True
            
    if len(password) > 7 and lowercase and uppercase:
        strong = True
    
    return strong


def calculate_score(password):

# The variables lowercase and uppercase indicate the presence or
# absence of lowercase and uppercase characters in the password
    lowercase = False #True if password contains a lowercase letter
    uppercase = False #True if password contains an uppercase letter

# Loop through each character in the password and ...
# ... check the password for specific characters
    for character in password:
        if character in LOWER_CASE_LETTERS:
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True

# Calculate the score based on the rules

    score = 0

# Rule 1
    if len(password) > 7:
        score = score + 5

# Rule 2
    if lowercase:
        score = score + 1

# Rule 3
    if lowercase and uppercase:
        score = score + 5

    return score

# Test driver
test_passwords = ["sun", "Sun", "Sunshine", "12345", "123456789"]
test_passwords[4] = "Moonlight" # (ii)

print(f'Score\tPassword') #(i)
print(f'-----\t--------') #(i)

lowest_score = 999 # (iii)
weakest_password = '' # (iii)

for password in test_passwords:
    pass_score = calculate_score(password)
    if pass_score < lowest_score:
        lowest_score = pass_score
        weakest_password = password
    print(f'{pass_score}\t{password}') #(i)
    
print(f'\nThe weakest password is: {weakest_password}')
print(f'Score: {lowest_score}')
print()
print('The strong passwords are: ')

for password in test_passwords: #(v)
    if is_strong(password):
        print(password)
    

    
