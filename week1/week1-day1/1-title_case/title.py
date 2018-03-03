def titlecase(title, exceptions):
    # convert exceptions to lowercase for comparison
    ex = []
    for e in exceptions:
        ex.append(e.lower())

    first_word = True

    result = []
    words = title.split()
    for word in words:
        new_word = word.lower()
        if first_word or word.lower() not in ex:
            char1 = word[0].upper()
            rest_of_word = word[1:].lower()
            new_word = char1 + rest_of_word

        result.append(new_word)
        first_word = False

    return ' '.join(result)

exceptions = ['jumps', 'the', 'over']
result = titlecase('the quick brown fox jumps over the lazy dog', exceptions)
#  "The Quick Brown Fox jumps over the Lazy Dog"
print(result)

exceptions = ['are', 'is', 'in', 'your', 'my']
result = titlecase('THE vitamins ARE IN my fresh CALIFORNIA raisins', exceptions)
#  "The Vitamins are in my Fresh California Raisins"
print(result)
