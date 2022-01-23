def isPalindrome(word):
    palindrome = True
    length=len(word)

    i=0
    while i < length/2:
        if word[i] != word[length-1-i]:
            palindrome = False
        i = i+1

    return palindrome

input_word = input("Type a word: ")

if(isPalindrome(input_word)):
    print("The word " + input_word + " is a palindrome!")
else:
    print("The word " + input_word + " is not a palindrome!")
        