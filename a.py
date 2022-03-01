
def validate_state(index, word1, word2, word3, d, previous_results):
    
    if str(d) in previous_results:
        return False
    
    smaller_word = word1 if len(word1) < len(word2) else word2
    remainder = 0
    while abs(index) <= len(smaller_word):
        letter1 = word1[index]
        letter2 = word2[index]
        result_letter = word3[index]

        if letter1 == letter2 and d[letter1] != d[letter2]:
            return False

        if letter1 == letter2 and letter1 != result_letter and d[letter1] == 0:
            return False

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
index = -1
while not validate_state(index, word1, word2, word3, d, previous_results):
    
    if word3_first_digit_must_be_one:
        d[word3[0]] = 1       
    

                
               
    previous_results.append(str(d))
