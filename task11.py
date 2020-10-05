def common_letter(str1, str2):
    for letter in str1:
        if letter in str2:
            print([letter])


common_letter("competition", "complexion")
