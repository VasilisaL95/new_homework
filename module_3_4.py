def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        i = i.lower()
        if root_word in i:
            same_words.append(i)
            continue

    for j in other_words:
        j = j.casefold()
        root_word = root_word.casefold()
        if j in root_word:

            same_words.append(j)
            continue
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
