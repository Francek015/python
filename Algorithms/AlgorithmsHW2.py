import math

letters = 'ddddbhhhh'
strlen = math.ceil(len(letters)/2)
str1 = letters[:strlen:]
str2 = letters[strlen::]
reversed_string = str2 + str1

print(reversed_string)



def confirm_duplicates(string):
    return len(set(string)) < len(string)

print(confirm_duplicates('asdf'))



