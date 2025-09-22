def same_char_longest_substr_after_replacements(s: str, k: int) -> int:
    max_len = 1
    seen = {}
    start = 0

    # Space: O(26)
    for end in range(len(s)):
        seen[s[end]] = seen.get(s[end], 0) + 1

        while (end - start + 1 - max(seen.values())) > k:
            seen[s[start]] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    # Brute Force
    # for i in range(len(s)):
    #     seen = {}
    #     for j in range(i, len(s)):
    #         seen[s[j]] = seen.get(s[j], 0) + 1
    #         max_freq = max(seen.values())
    #         sub_len = j - i + 1
    #
    #         if (sub_len - max_freq) <= k:
    #             max_len = max(max_len, sub_len)
    #         else:
    #             break

    return max_len


print(same_char_longest_substr_after_replacements("BBABCCDD", 2))
