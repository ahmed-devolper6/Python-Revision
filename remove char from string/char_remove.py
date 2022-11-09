def remove_char(word,char):
    word_without_char = []
    for setnece in word:
        if setnece != char:
            word_without_char.append(setnece)
    return "".join(word_without_char)


print(remove_char('my name is ahmead jamal bbb','b'))