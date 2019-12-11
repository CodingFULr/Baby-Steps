user = input("What do you want to translate: ")
trans_vowel = "o"

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + trans_vowel
        else:
            translation = translation + letter
    return translation

translate(user)