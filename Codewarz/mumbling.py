

def accum(my_string):
    returnme = ''
    for pos, character in enumerate(my_string):
        returnme = returnme + (character.upper() + character.lower() * (pos))
        if pos < len(my_string) - 1:
            returnme = returnme + '-'
    return returnme


print(accum('HbideVbxncC'))
