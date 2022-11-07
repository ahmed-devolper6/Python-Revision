def longest_word(setence):
    word_list = setence.split(" ")
    count = 0
    for word in word_list:
        if len(word) > count:
            count = len(word)
            long_word = word
    return long_word


print(longest_word('junir django devsdasadasdasd'))
