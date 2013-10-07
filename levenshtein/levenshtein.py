def levenshtein_distance(a, b):
    """Returns the Levenshtein distance between two strings.

    Keyword argument(s):
    a - First string
    b - Second string
    """

    mat = {}

    if a == b:
        return 0

    len_a = len(a)
    len_b = len(b)

    if len_a == 0:
        return len_b
    if len_b == 0:
        return len_a

    for i in range(len_a + 1):
        mat[i, 0] = i

    for j in range(len_b + 1):
        mat[0, j] = j

    for j in range(1, len_b+1):
        for i in range(1, len_a+1):
            if a[i-1] == b[j-1]:  # zero-based indexes
                mat[(i, j)] = mat.get((i-1, j-1), 0)
            else:
                mat[(i, j)] = min(mat.get((i-1, j), 0) + 1,
                                  mat.get((i, j-1), 0) + 1,
                                  mat.get((i-1, j-1), 0) + 1)
    return mat[(i, j)]


def levenshtein_distance_recursive(a, b):
    """Returns the Levenshtein distance between two strings.

    Keyword argument(s):
    a - First string
    b - Second string
    """

    if a == b:
        return 0

    len_a = len(a)
    len_b = len(b)

    if len_a == 0:
        return len_b
    if len_b == 0:
        return len_a

    if a[-1] == b[-1]:
        cost = 0
    else:
        cost = 1

    return min(levenshtein_distance(a[:-1], b) + 1,
               levenshtein_distance(a, b[:-1]) + 1,
               levenshtein_distance(a[:-1], b[:-1]) + cost)
