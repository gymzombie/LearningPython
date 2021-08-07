from .piglatin import pig_latin


def pig_it(text):
    # split sentence into words

    # send each word to pig_latin
    for each word in text:
        pig_latin(word)

    # join back into a sentence

    # return that