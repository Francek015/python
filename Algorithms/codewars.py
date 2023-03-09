# from solution import fields
#
# def spin_words(sentence, ):
#     words_spun = spin_words(sentence)
#     print(words_spun)
#
# spin_words(sentence('hey there'))

# s = 'python'
# stringlength = len(s)
# slicedString = s[stringlength::-1]
#
# print(slicedString)


def spin_words(s):
    stringlength = len(s)
    slicedString = s[stringlength, :1-1]
    print(slicedString)


spin_words('python')