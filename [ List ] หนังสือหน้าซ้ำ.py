def isPalindrome(s):
    return s == s[::-1]
palindromelist = []
num = 0
for i in range(int(input())) :
    s = input()
    ans = isPalindrome(s)
    if ans:
        palindromelist.append(s)
        num += 1
print(num)
print(palindromelist)