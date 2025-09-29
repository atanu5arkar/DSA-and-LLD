def decode_string(s: str) -> str:
    stack = []
    # Sequence to be decoded currently
    current_str = ""
    # No. of times the sequence is to be repeated
    current_num = 0

    for char in s:
        if char == "[":
            stack.append(current_str)
            stack.append(current_num)
            current_str = ""
            current_num = 0
        elif char == "]":
            count = stack.pop()
            prev_str = stack.pop()
            current_str = prev_str + current_str * count
        elif char.isdigit():
            current_num = current_num * 10 + int(char)
        else:
            current_str += char

    return current_str


print(decode_string("3[a2[c]]"))
print(decode_string("3[a]2[bc]"))
print(decode_string("2[abc]3[cd]ef"))
print(decode_string("100[leetcode]"))
print(decode_string("3[z]2[2[y]pq]ef"))
