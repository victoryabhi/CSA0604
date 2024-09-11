'''
6. Word Break Problem
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words.
Consider the following dictionary 
{ i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango}
Input:  ilike
Output: Yes 
The string can be segmented as "i like".
Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" or "i like sam sung".

'''
def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return "Yes" if dp[n] else "No"

dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
print(word_break("ilike", dictionary))  
print(word_break("ilikesamsung", dictionary))  
