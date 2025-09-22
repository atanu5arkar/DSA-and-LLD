def are_anagrams(s: str, t: str) -> bool:
    seen = {}

    for i in range(len(s)):
        seen[s[i]] = seen.get(s[i], 0) + 1

    for j in range(len(t)):
        count = seen.get(t[j])
        if not count:
            return False

        seen[t[j]] -= 1
        if not seen[t[j]]:
            seen.pop(t[j])

    if len(seen):
        return False
    return True


print(are_anagrams("x", "xx"))
print(are_anagrams("bbcc", "ccbc"))