"""
This module will create a sam filter based on Paul Graham’s A Plan for Spam.

Written by Royce Lloyd for CS 344 at Calvin College
3/8/2019
"""

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

ngood = len(spam_corpus)
nbad = len(ham_corpus)

emailContents = []


"""
Big thank you to Alex Martelli on StackOverflow
https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
"""
spamWords = []
hamWords = []

for sublist in spam_corpus:
    for item in sublist:
        spamWords.append(item)

for sublist in ham_corpus:
    for item in sublist:
        hamWords.append(item)

goodHash = {}
badHash = {}

for word in hamWords:
    goodCount = 0
    for checkWord in hamWords:
        if word == checkWord:
            goodCount += 1
    goodHash[word] = goodCount


for word in spamWords:
    badCount = 0
    for checkWord in spamWords:
        if word == checkWord:
            badCount += 1
    badHash[word] = badCount


probs = {}


"""
TODO
1)Solve lambda function
2)Populate probs hash with words and their prop of being evil
"""

def getprob(wordInQuestion):
    g = 2 * goodHash[wordInQuestion] or 0
    b = badHash[wordInQuestion] or 0
    if g + b > 1:
        return max(0.01, min(0.99, min(1.0, b/nbad) / (min(1.0, g/ngood) + min(1.0, b/nbad))))
    else:
        return 0

# def function2():
#     prod = 1
#     for key in probs:
#         prod = prod * probs[key]
#     return (prod / (prod + ( lambda x: )))



print(spamWords)
print(hamWords)
print(goodHash)
print(badHash)





