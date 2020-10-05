def vowel(str):
    vowels = "aeiouAEIOU"
    for letter in str:
         if letter in vowels:
            print([letter])

vowel("complex")
