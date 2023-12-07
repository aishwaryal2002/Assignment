def shortest_palindrome(s):
    i = len(s) - 1
    while i >= 0 and not s[:i + 1] == s[:i + 1][::-1]:
        i -= 1
    return s[i + 1:][::-1] + s

print(shortest_palindrome("aacecaaa"))  
print(shortest_palindrome("abcd"))      
