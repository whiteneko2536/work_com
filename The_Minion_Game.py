text = 'BANANA'
tex_list=[]
for i in text:
    #print(i)
    if i not in tex_list:
        tex_list.append(i)
print(tex_list)

Stuart_letters = list(filter(lambda x: x not in ['A', 'E', 'I', 'O', 'U'],tex_list))
Kevin_letters = list(filter(lambda x: x in ['A', 'E', 'I', 'O', 'U'],tex_list))
not_vowel=Stuart_letters
vowel=Kevin_letters
print(Stuart_letters)
print(Kevin_letters)


for i in Stuart_letters:
    if i[-1] in not_vowel:
        for j in Stuart_letters:
            str_ = i[-1]+j
            Stuart_letters.append(str_)
    elif i[-1] in not_vowel:
        for j in Stuart_letters:
            str_ = i[-1] + j
            Stuart_letters.append(str_)



print(Stuart_letters)

