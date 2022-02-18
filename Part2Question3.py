#LongestPalindrome
def LongestPalindrome(s):
    n = len(s)
    ms = [0,0]
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n-i):
            if i==0:
                dp[j][j]=1
            elif i==1:
                if s[j]==s[j+i]:
                    dp[j][j+i]=1
                    if j+i-j+1 > ms[1]-ms[0]+1:
                        ms = [j,j+i]
            elif s[j]==s[j+i] and dp[j+1][j+i-1]==1:
                dp[j][j+i]=1
                if j+i-j+1 > ms[1]-ms[0]+1:
                    ms = [j,j+i]
    return s[ms[0]: ms[1]+1]

print(LongestPalindrome(input()))
