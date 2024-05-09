def fibonacci(n):
    m = 1000000007
    
    if n == 0 or n == 1:
        return n
    
    else:
        val = [0] * (n + 1)
        val[0] = 0
        val[1] = 1
        for i in range(2, n + 1):
            val[i] = (val[i - 1] % m + val[i - 2] % m) % m

        return val[n]

n = int(input())
print(fibonacci(n))
