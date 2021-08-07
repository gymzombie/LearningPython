

def pig_latin(input_word):
    input_word = input_word.lower()
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                  "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    if any(char.isdigit() for char in input_word) is True:
        return None
    elif input_word == "":
        return None
    elif any(item in input_word for item in vowels) is False:
        return input_word + "ay"
    elif input_word[0] in vowels:
        return input_word + "way"
    else:
        while input_word[0] in consonants:
            input_word = input_word[1:] + input_word[:1]
        return input_word + "ay"

print(pig_latin("ay"))
