def longest_substring_without_duplicates(s: str) -> int:
    max_len = 0
    start = 0
    state = {}

    if len(s) == 0:
        return 0

    for end in range(len(s)):
        end_ch = s[end]
        state[end_ch] = state.get(end_ch, 0) + 1

        while state[end_ch] > 1:
            state[s[start]] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len


result = longest_substring_without_duplicates("pwwkew")
print(result)

# Brute Force: O(n^2)
# for i in range(len(s)):
#     state = {s[i]}
#     for j in range(i + 1, len(s)):
#         state.add(s[j])
#         substr_len = len(s[i:j + 1])
#
#         if len(state) != substr_len:
#             break
#         else:
#             max_len = max(max_len, substr_len)
