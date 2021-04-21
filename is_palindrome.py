def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    return "Not palindrome"
st = input("Enter a string : ") 
check = is_palindrome(st)
print(check)