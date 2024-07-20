word = input('Enter a random word: ')

if word.lower() == "".join(reversed(word.lower())):
    print(f'{word} is a palindrome.')
else:
    print(f'{word} is not a palindrome.')