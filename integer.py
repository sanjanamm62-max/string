
# # a = [1,2,3,4,5,10,11]
# # b = [2,3,1,0,5]
# # b_set = set(b)

# # result = [x for x in a if x not in b_set]

# # print(*result)
# StringProgram
# def stringBuilder(s):
#     stack = []
#     curr_str = ""
#     num = 0

#     for ch in s:
#         if ch.isdigit():
#             num = num * 10 + int(ch)
#         elif ch == '[':
#             stack.append((curr_str, num))

#             curr_str= ""
#             num = 0
#         elif ch == ']':

#             prev_str, repeat = stack.pop()
#             curr_str = prev_str + curr_str * repeat
#         else:
#             curr_str += ch
#     return curr_str
# print(stringBuilder("3[a]2[bc]"))
# print(stringBuilder("3[a2[c]]"))
# print(stringBuilder("2[abc]3[cd]ef")) 

# def isHappy(n):
#     seen = set()
#     while n != 1:
#         if n in seen:
#             return False
#         seen.add(n)

#         n = sum(int(digit) ** 2 for digit in str(n))

#     return True 
# n = int(input("Enter number:"))
# print(isHappy(n))

# from collections import Counter

# def commonChars(words):
#     common_count = Counter(words[0])

#     for word in words[1:]:
#         common_count &= Counter(word)

#     result = []
#     for char, count in common_count.items():
#         result.extend([char] * count)
#     return result

# words = ["bella","label","roller"]
# words = ["cool", "lock", "cook"]
# print(commonChars(words))

def count_salutes(A):
    salutes = 0
    right_moving = 0

    for soldier in A:
        if soldier == '>':

            right_moving += 1
        elif soldier == '<':
             salutes += right_moving
    return salutes 

A='<>'

print(count_salutes(A))

       

    
    



