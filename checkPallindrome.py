import math
word = '''A palindrome is a word, number, phrase, or other sequence of 
characters which reads the same backward as forward, such as madam, 
racecar. There are also numeric palindromes, including date/time stamps 
using short digits 11/11/11 11:11 and long digits 02/02/2020. Sentence-length 
palindromes may be written when allowances are made for adjustments to capital 
letters, punctuation, and word dividers, such as A man, a plan, a canal, Panama!.'''


def isPalindrom(word):
    length = len(word) 
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

def getAllPallindrome(allWord):
	wordList = word.split()
	result = []
	for i in wordList:
		if isPalindrom(i):
			result.append(i)
	return result
		
print(getAllPallindrome(word))
