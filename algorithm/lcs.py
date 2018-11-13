def lcs(x_str, y_str):
    x_len = len(x_str)
    y_len = len(y_str)

    result_table = [[0 for _ in range(y_len+1)] for _ in range(x_len+1)]

    for n in range(1, x_len+1):
        for m in range(1, y_len+1):
            if x_str[n-1] == y_str[m-1]:
                result_table[n][m] = result_table[n-1][m-1] + 1
            else:
                result_table[n][m] = max(result_table[n][m-1], result_table[n-1][m])

    return result_table[n][m]


x = lcs("xyxxzxyzxy", "zxzyyzxxyxxz")
print(x)
