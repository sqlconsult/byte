def remove_duplicate(string):
    result = []
    removed_chars = []

    pos = 0

    while pos < len(string):
        char1 = string[pos : pos+1]
        next_char = string[pos+1 : pos+2]
        if char1 == next_char:
            removed_chars.append(char1)
        else:
            result.append(char1)
        pos += 1

    retVal1 = ''.join(result)
    retVal2 = ''.join(removed_chars)

    return retVal1, retVal2

orig_str = 'aabbccddeded'
str1, str2 = remove_duplicate(orig_str)
print('original string: ', orig_str)
print('duplicates removed: ', str1)
print('characters removed: ', str2)

orig_str = 'flabby aapples'
str1, str2 = remove_duplicate(orig_str)
print('original string: ', orig_str)
print('duplicates removed: ', str1)
print('characters removed: ', str2)

