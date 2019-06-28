def linear_sum(S, n):
    if n == 0:
        return 0
    return linear_sum(S, n - 1) + S[n - 1]

S = [1, 5, 8, 9, 4, 9, 3]

print(linear_sum(S, len(S)))
