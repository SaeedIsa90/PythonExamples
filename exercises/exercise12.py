
if __name__ == '__main__':
    sentence = input("Enter a sentence: ")
    letters = input("Enter letters: ")

    new_words = []
    for word in sentence.split():
        if word[0] not in letters:
            new_words.append(word)

    print(new_words)
