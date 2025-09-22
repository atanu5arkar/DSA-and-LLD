def permutation_exists_in_other_str(s1: str, s2: str) -> bool:
    # Checks whether an anagram of s1 exists in s2
    # Assumes the strings to have lowercase characters only
    seen_s1 = {}
    seen_s2 = {}
    start = 0

    if len(s2) < len(s1):
        return False

    # O(m)
    for c in s1:
        seen_s1[c] = seen_s1.get(c, 0) + 1

    # O(26n)
    for end in range(len(s2)):
        seen_s2[s2[end]] = seen_s2.get(s2[end], 0) + 1

        if (end - start + 1) == len(s1):
            # O(26) since the input charset is fixed
            if seen_s2 == seen_s1:
                return True

            seen_s2[s2[start]] -= 1
            if not seen_s2[s2[start]]:
                seen_s2.pop(s2[start])
            start += 1

    return False


print(permutation_exists_in_other_str("abc", "lecabee"))
print(permutation_exists_in_other_str("baa", "lecaabee"))
print(permutation_exists_in_other_str("abc", "lecaabee"))
