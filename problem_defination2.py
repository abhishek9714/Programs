def isPalindrome(s):
    s=s.lower()
    return s == s[::-1]
 
 
# Driver code
string = str(input())
string.lower()
ans = isPalindrome(string)
 
if ans:
    print("Yes")
else:
    print("No")
    
    
    
'''Read me
step1: provide input as a string example: Dad'''