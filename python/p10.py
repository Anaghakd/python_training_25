#Program to check if the Alphabet is Vowel or Consonant
alphabet=input('Enter the alphabet:')
if alphabet.lower() in 'aeiou':
    print('Vowel')
else:
    print('Consonant')