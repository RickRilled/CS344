"""
This module will create a sam filter based on Paul Graham’s A Plan for Spam.

Written by Royce Lloyd for CS 344 at Calvin College
3/8/2019
"""

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

ngood = len(spam_corpus)
nbad = len(ham_corpus)

emailContents = ["save", "on", "green", "eggs", "and", "spam", "do", "you", "like", "spam", "80", "$", "off", "click",
                 "here", "am", "I", "spamiam", "ham", "that", "i"]

def getprob(wordInQuestion):

    #Check for KeyErrors(Out of range of dict)
    try:
        g = (2 * goodHash[wordInQuestion])
    except KeyError:
        g = 0

    try:
        b = badHash[wordInQuestion]
    except KeyError:
        b = 0

    #Computer the possibility of spam
    if g + b > 1:
        return max(0.01, min(0.99, min(1.0, b/nbad) / (min(1.0, g/ngood) + min(1.0, b/nbad))))
    else:
        return 0

def isSpam(li):

    #Find prod
    prod = 1
    for value in li:
        prod = prod * value

    #Create a list f compliments
    complList = []
    for value in li:
        complList.append(1 - value)

    #Computer the product of those compliments
    compProd = 1
    for value in complList:
        compProd = compProd * value

    #Return the probability of the email being spam
    return prod / (prod + (compProd))


"""
This section takes our corpus(s) and creates a single list of tokens.

Big thank you to Alex Martelli on StackOverflow for lines 55-61
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

"""
Create a hash table(dictionary) for the number of times each word appears in the good and bad corpus
"""
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


"""
Use the function getprob to determine the possibility that an email containing these words
is spam or not.
"""
hashTotal = {}

for word in goodHash:
    hashTotal[word] = getprob(word)

for word in badHash:
    hashTotal[word] = getprob(word)


"""
Create a list of probabilities from emailContents.
These probabilities are the chances of that word being used in a spam email,
based on our corpus.
"""
probsTemp = {}
probs = []

for word in emailContents:
    probsTemp[word] = getprob(word)

for key in probsTemp:
    if probsTemp[key] != 0:
        probs.append(probsTemp[key])

print("A higher number means spam, a lower number means ham.")
print("The probability of these words being spam, based on the spam and ham corpus, are:", "\n", hashTotal)
# print(probsTemp)
# print(probs)
print("The probability of the email, gives the contents of emailContents, is spam, is: ", isSpam(probs))
