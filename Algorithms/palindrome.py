# def is_palindrome(s):
#     reversed_s = s[::-1]
#     if s == reversed_s:
#         return True
#     else:
#         return False
#
# test_case_pos = 'radar'
# test_case_neg = 'radax'
#
# result_pos = is_palindrome(test_case_pos)
# result_neg = is_palindrome(test_case_neg)
#
# print(result_neg)
# print(result_pos)



def is_almost_palindrome(s):
    for i in range(len(s)):
        current_str = s[:i] + s[i + 1:]
        if current_str == current_str[::-1]:
            return True
    return False


test_pos = 'radkar'
test_neg = 'radario'

result_pos = is_almost_palindrome(test_pos)
print(result_pos)

result_neg = is_almost_palindrome(test_neg)
print(result_neg)