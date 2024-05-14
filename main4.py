def count_ways(n, memo):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    memo[n] = count_ways(n - 1, memo) + count_ways(n - 2, memo) + count_ways(n - 3, memo)
    return memo[n]

def print_ways(n):
    memo = [-1] * (n + 1)
    count_ways(n, memo)
    stack = [(n, [])]
    print("Formas posibles de subir la escalera con", n, "peldaños:")
    while stack:
        current_n, path = stack.pop()
        if current_n == 0:
            print(path)
        else:
            if current_n >= 1:
                stack.append((current_n - 1, path + [1]))
            if current_n >= 2:
                stack.append((current_n - 2, path + [2]))
            if current_n >= 3:
                stack.append((current_n - 3, path + [3]))

# Valor fijo de n=3
n = 3
print_ways(n)

# Valor fijo de n=6
n = 6
print_ways(n)

# Valor fijo de n=5
n = 5
print_ways(n)

# Valor fijo de n=4
n = 4
print_ways(n)

# Valor fijo de n=7
n = 7
print_ways(n)
