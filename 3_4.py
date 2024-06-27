def single_root_words(root_word,*other_words):
    same_words = []
    for word in other_words:
        if str(root_word).lower() in str(other_words).lower():
            same_words.append(word)
        if str(word).lower() in str(root_word).lower():
            same_words.append(word)
    return(same_words)

res = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(res)