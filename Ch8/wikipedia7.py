from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


def cleanInput(input):
    # remove any Unicode characters
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')

    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i+n])
        if newNGram not in output:
            output[newNGram] = 0
        else:
            output[newNGram] += 1
    return output


content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=lambda t: t[1], reverse=True)
print(sortedNGrams)
