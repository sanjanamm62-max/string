def stringBuilder(s):
    stack = []
    curr_str = ""
    num = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append((curr_str, num))

            curr_str= ""
            num = 0
        elif ch == ']':

            prev_str, repeat = stack.pop()
            curr_str = prev_str + curr_str * repeat
        else:
            curr_str += ch
    return curr_str

print(stringBuilder("3[a]2[bc]"))
print(stringBuilder("3[a2[c]]"))
print(stringBuilder("2[abc]3[cd]ef"))

