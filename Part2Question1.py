#CheckIfStringIsPanagram
def isPangram (pangram):
    c=0
    s=set()
    for xx in pangram.lower():
        x=ord(xx)-ord('a')
        if x not in s and x>=0 and x<26:
            c+=1
            s.add(x)
            if c==26:
                break;
    return c==26

print(isPangram(input()))
