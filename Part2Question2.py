#GrammerCheckerQuestion#2
def wordBreak(wordList, word):
    if word == '':
        return True
    else:
        wordLen = len(word)
        x=[(word[:i] in wordList) and wordBreak(wordList, word[i:]) for i in range(1, wordLen+1)]
        print(x)
        return any(x)
print(wordBreak(["Ate" , "I", "Dinner", "For", "Chicken" ,"Rice", "And"],"IAteChickenAndRiceForDinner"))
