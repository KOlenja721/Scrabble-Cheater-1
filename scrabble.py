import argparse
import sys
import operator

with open('sowpods.txt', 'r') as f:
	sowpods = f.readlines()
words = [x.strip() for x in sowpods]

parser = argparse.ArgumentParser(description="get the rack")
parser.add_argument('RACK', help="word to be used as rack")
args = parser.parse_args()
RACK = (args.RACK).upper()

valid_words = []
def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK
	
for word in words:
	if anagramSolution1(word,RACK):
		valid_words.append(word)

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

score = 0
result = {}
for word in valid_words:
	for letter in list(word):
		score = score + scores[letter.lower()]
	result[word] = score	
#	print(str(score) + " " + word.lower())
	score = 0
sorted_x = sorted(result.items(), key = operator.itemgetter(1), reverse = True)
result = dict(sorted_x)
for word in result.keys():
	print("{} {}".format(result[word], word))