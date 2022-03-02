import json
from random import random, randrange
import sys


word1 = ""
word2 = ""
word3 = ""
if len(sys.argv) < 2:
    word1 = input()
    word2 = input()
    word3 = input()
else:
    word1 = str(sys.argv[1])
    word2 = str(sys.argv[2])
    word3 = str(sys.argv[3])

words = [word1,word2,word3]
s = set()

for word in words:
    for letter in word:
        s.add(letter)

set_letters = list(s)

d = {}
for e in s:
    d[e] = 1


def validate_state(word1, word2, word3, d, previous_results):
    
    if str(d) in previous_results:
        return False
    
    smaller_word = word1 if len(word1) < len(word2) else word2
    index = -1
    remainder = 0
    while abs(index) <= len(smaller_word):
        letter1 = word1[index]
        letter2 = word2[index]
        result_letter = word3[index]
    
        sum = remainder + d[letter1] + d[letter2]
    
        remainder = sum // 10
        result_digit = sum % 10 

        if d[result_letter] != result_digit:
            return False
    
        index -= 1

    while abs(index) <= len(word1):
        letter1 = word1[index]
        sum = remainder + d[letter1]
    
        remainder = sum // 10
        result_digit = sum % 10 

        if d[result_letter] != result_digit:
            return False
    
        index -= 1

    while abs(index) <= len(word2):
        letter2 = word2[index]
        sum = remainder + d[letter2]
    
        remainder = sum // 10
        result_digit = sum % 10 

        if d[result_letter] != result_digit:
            return False
    
        index -= 1
    
    if remainder != d[word3[0]]:
        return False

    return True

word3_first_digit_must_be_one = False
if len(word3) > len(word1) and len(word3) > len(word2):
    word3_first_digit_must_be_one = True
    d[word3[0]] = 1

previous_results = []
index_letter = 0
while len(previous_results) < 4:
    while not validate_state(word1, word2, word3, d, previous_results):
        used_nums = set()
        if word3_first_digit_must_be_one:
            used_nums.add(1)
        d = dict()
        if word3_first_digit_must_be_one:
            d[word[0]] = 1
        for key in set_letters:
            if (word3_first_digit_must_be_one and key != word3[0]) or not word3_first_digit_must_be_one:
                temp = randrange(10) 
                while temp in used_nums:
                    temp = randrange(10) 
                used_nums.add(temp)
                d[key] = temp
    previous_results.append(str(d))

print(f"{word1}\n{word2}\n{word3}\n")

for r in previous_results:
    json_string = r.replace("'","\"")
    result_dict = json.loads(json_string)
    equation = ""
    for word in words:
        for letter in word:
            equation += str(result_dict[letter])
        equation += "\n"
    
    print(result_dict)
    print(equation)