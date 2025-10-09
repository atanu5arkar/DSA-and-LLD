"""
- Every row is sorted in ascending order.
- The first integer in every row is greater than the last integer of the previous row.
"""


# O(m * log n)
def search_in_matrix(matrix: list[list[int]], target: int) -> bool:
    for i in range(len(matrix)):
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = l + (r - l) // 2
            val = matrix[i][mid]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
    return False


# O(log m * n)
def better_search_in_matrix(matrix: list[list[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    start = 0
    end = rows - 1

    while start <= end:
        mid = (start + end) // 2
        val_s = matrix[mid][0]
        val_e = matrix[mid][cols - 1]

        if target > val_s and target > val_e:
            start = mid + 1
        elif target < val_s and target < val_e:
            end = mid - 1
        else:
            l = 0
            r = cols - 1

            while l <= r:
                m = l + (r - l) // 2
                val = matrix[mid][m]

                if val == target:
                    return True
                elif val < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
    return False


matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 19

print(search_in_matrix(matrix, target))
print(better_search_in_matrix(matrix, target))
