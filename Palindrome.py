#Palindrome

user_word = input('Enter a word to check if it is a palindrome:\n').lower()

check_word = user_word.replace(' ',  '').lower()
inverted_word = check_word[ : :-1]
print(inverted_word)

if check_word == inverted_word:
	print(f'{user_word.capitalize()} is a palindrome!')
else:
	print(f'{user_word.capitalize()} is not a palindrome')