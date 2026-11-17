def count_vowels_and_consonants(text:str):
    vowels="aeuio"
    vowel=0
    consonant=0
    for let in text.lower():
        if let.isalpha():
            if let in vowels:
               vowel+=1
            else:
               consonant+=1
    return{
        "unli":vowel,
        "undosh":consonant
}
matn=input("text= ")
result=count_vowels_and_consonants(matn)
print(result)