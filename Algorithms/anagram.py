def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


test_str1 = 'bacd'
test_str2 = 'dcba'

result = is_anagram(test_str1, test_str2)
print(result)
