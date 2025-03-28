# Question 16(b)
# Examination Number:

# A variable to store all the lower case letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

def is_strong(password): #(iv)
    strong = False
    
    lowercase = False #True if password contains a lowercase letter
    uppercase = False #True if password contains an uppercase letter
    
    for character in password:
        if character in LOWER_CASE_LETTERS:
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True
            
    if len(password) > 7 and uppercase and lowercase:
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
test_passwords[4] = 'Moonlight' #(ii)
lowest_score = 9999 #(iii)
weakest_password = '' #(iii)
print('Score\tPassword') #(i)
print('-----\t--------') #(i)
for password in test_passwords:
    pass_score = calculate_score(password)
    if pass_score < lowest_score: #(iii)
        lowest_score = pass_score
        weakest_password = password
    print(f'{pass_score}\t{password}') #(i)
    
print(f'\nThe weakest password is: {weakest_password}') #(iii)
print(f'Score: {lowest_score}') #(iii)

print('\nThe strong passwords are: ') #(v)
for password in test_passwords:
    if is_strong(password):
        print(password)