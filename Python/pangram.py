
import string

def pangram(sentence):
    myDict = {}
    alpha = string.ascii_lowercase
    for letter in alpha:
        myDict[letter]=0
        
    for letter in sentence.lower():
        if letter in myDict:
            myDict[letter] +=1
    
    retVal = 'pangram'
    for key, value in myDict.items():
        if value < 1:
            retVal = 'not pangram'
            break
            
    return retVal
    
def pangram2(sentence):
    mySet = set(sentence.lower())
    alpha = set(string.ascii_lowercase)
    
    if alpha.issubset(mySet):
        return 'a pangram'
    else:
        return 'not a pangram'
    
    
    
    
# Define a main() function 
def main():
    sentence = 'We promptly judged antique ivory buckles for the next prize'
    print('sentence', sentence, ' is' ,pangram2(sentence))    # pangram
    
    sentence = 'We promptly judged antique ivory buckles for the prize'
    print('sentence', sentence, ' is' ,pangram2(sentence))    # not pangram
    
    sentence = 'The quick brown fox jumped over the lazy dogs back'
    print('sentence', sentence, ' is' ,pangram2(sentence))    # pangram
    
            
    sentence = 'Two driven jocks help fax my big quiz'
    print('sentence', sentence, ' is' ,pangram2(sentence))    # pangram
            
    sentence = 'Pack my box with five dozen liquor jugs'
    print('sentence', sentence, ' is' ,pangram2(sentence))    # pangram
        
    sentence = 'The five boxing wizards jump quickly'
    print('sentence', sentence, ' is' ,pangram2(sentence))    # pangram

# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
    
    
    
    