def wait_before_warmer(temps: list[int]) -> list[int]:
    n = len(temps)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            top = stack.pop()
            result[top] = i - top
        stack.append(i)

    return result


temps = [30, 38, 30, 36, 35, 40, 28]
print(wait_before_warmer(temps))

temps = [22, 21, 20]
print(wait_before_warmer(temps))
