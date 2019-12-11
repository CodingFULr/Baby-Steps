def traslate(org_word):
    trans_letter = input("What do you want to vowels into: ")
    answer = ""
    for letter in org_word:
        if letter in "aeiou":
            letter = trans_letter.lower()
            answer += letter
        elif letter in "AEIOU":
            letter = trans_letter.upper()
            answer += letter
        else:
            answer += letter
    print(answer)

print("sENtenCe RaNDomIZer")
traslate(input("What do you want to destroy: "))
