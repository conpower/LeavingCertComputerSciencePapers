# Ceist 16(a)
# Scrúduimhir: 
from random import randint

def guess_game(max_guesses_allowed):
    
    secret_number = randint(1, 5)
    guess_count = 0
    user_guess = 0
    
    while (user_guess != secret_number):
        
        user_guess = int(input("Cuir isteach do thomhas: "))
        guess_count += 1   # méadú guess_count faoi 1
        if user_guess == secret_number:
            print("Comhghairdeas! Bhuaigh tú!")

print("Fáilte go dtí an cluiche tomhais!")
guess_game(3)
