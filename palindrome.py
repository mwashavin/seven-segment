def is_palindrome(strng):
    n = len(strng)
    is_palindrome = True
    for i in range(n):
        if strng[i] != strng[n-1-i]:
            is_palindrome = False
    return is_palindrome
    
input_str = input("Enter a string: ")
input_str= input_str.replace(" ", "").upper()
if is_palindrome(input_str):
    print("It's a palindrome")
else:
    print("It's not a palindrome")