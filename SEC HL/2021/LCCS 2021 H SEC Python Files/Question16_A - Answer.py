# Question 16(a)
# Student name:

#function definition used in part (v)
def is_anagram(w1,w2):
    if sorted (w1) == sorted(w2):
        return True
    else:
        return False
    
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ") #(i)

#test whether the sorted string are the same as each other
#if the sorted strings are the same then they must be anagrams
if (sorted(word1.lower())==sorted(word2.lower())): #(iv)
    print(f"{word1} is an anagram of {word2}") #(ii)
else:
    print(f"{word1} is NOT an anagram of {word2}") #(iii)
    
if is_anagram(word1.lower(),word2.lower()): #(v)
    print(f"{word1} is an anagram of {word2}")
else:
    print(f"{word1} is NOT an anagram of {word2}")
  
#(vi)
phrase = input('Enter a phrase: ')
phrase_no_spaces = phrase.replace(' ','')

if is_anagram(word1.lower(),phrase_no_spaces.lower()):
    print(f"{word1} is an anagram of {phrase}")
else:
    print(f"{word1} is NOT an anagram of {phrase}")
    
if is_anagram(word2.lower(),phrase_no_spaces.lower()):
    print(f"{word2} is an anagram of {phrase}")
else:
    print(f"{word2} is NOT an anagram of {phrase}")